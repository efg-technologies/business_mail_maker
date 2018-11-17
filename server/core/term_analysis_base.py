#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
利用規約解析クラス
'''

# TODO: chunkは別途でクラスにした方が扱いやすい
# TODO: あらかじめ同意したものとみなす系も取りたい

import CaboCha
import re
from abc import ABCMeta


class TermAnalysisBase(metaclass=ABCMeta):
    verb_dic = []
    nominative_dic = []
    warn_word_dic = []
    ヲ格 = ['を', 'に対し']
    カラ格 = ['から']
    ガ格 = ['が', 'は']
    cp = None
    _DEBUG: bool = True
    # _DEBUG: bool = False

    def __init__(self,
                 term_text: str,
                 dic: str='./lib/mecab-ipadic-neologd') -> None:
        '''警告すべき文章を返す
        :param str term_text: 足される値。
        :param str dic: 用いる辞書のpath
        '''
        self.dic = dic
        if dic:
            self.cp = CaboCha.Parser('-d ' + self.dic)
        else:
            self.cp = CaboCha.Parser()
        self.term_text = term_text
        self.msgs = []  # 警告文の配列を初期化
        return None

    def _analysis(self, sentence):
        ''' 1つの文を解析する '''
        tree = self.cp.parse(sentence)
        tokens = self._to_tokens(tree)
        verb = self._find_verb(tokens)
        if not verb:
            return None
        verb_head_id = self._get_chunk_id_of(verb, tokens)
        nominative = self._find_nominative_case(verb_head_id, tokens)
        object = self._find_object_case(verb_head_id, tokens)
        if object is None or nominative is None:  # どちらかを取得出来なければパス
            return None
        if nominative.surface not in self.nominative_dic:
            return None

        short = self._concat_tokens(nominative, tokens, 'nominative') \
            + self._concat_tokens(object, tokens, 'object') \
            + self._concat_tokens(verb, tokens, 'verb')
        data = {
                'S': nominative.surface,
                'Obj': object.surface,
                'V': verb.surface,
                }

        sentence_type = 'info'
        for word in self.warn_word_dic:
            if sentence.find(word) > 0:
                sentence_type = 'warn'
        if self._DEBUG:
            print('short: ', end='')
            print(short)
        self.msgs.append({'text': short, 'data': data, 'row': sentence,
                          'type': sentence_type, 'detail': sentence})

    def _find_verb(self, tokens: []):
        ''' 特定の動詞を見つける '''
        for t in tokens:
            # TODO: fix: 品詞の動詞判定を行っていない
            if t.surface in self.verb_dic and t.chunk is not None:
                return t
        return None

    def _find_nominative_case(self, verb_head_id: int, tokens: []):
        ''' 動詞の主格を見つける '''
        for t in tokens:
            if t.chunk is not None and t.chunk.link == verb_head_id:
                for node in self._get_tokens_in_chunk(t, tokens):
                    features = node.feature.split(",")
                    if features[0] == '助詞' and node.surface in self.ガ格:
                        return t
        return None

    def _find_object_case(self, verb_head_id: int, tokens: []):
        ''' 動詞の目的格を見つける '''
        for t in tokens:
            if t.chunk is not None and t.chunk.link == verb_head_id:
                for node in self._get_tokens_in_chunk(t, tokens):
                    features = node.feature.split(",")
                    if features[0] == '助詞' and node.surface in self.ヲ格:
                        return t
        return None

    def _get_chunk_id_of(self, token, tokens):
        ''' トークンを含むチャンクヘッダのidを取得 '''
        chunk_i = -1
        for t in tokens:
            if self._has_chunk(t):
                chunk_i += 1
            if t.surface == token.surface:
                return chunk_i
        return None

    def _has_chunk(self, token):
        '''
        チャンクがあるかどうか
        '''
        return token.chunk is not None

    def _get_tokens_in_chunk(self, head, tokens) -> []:
        '''
        チャンク内のtokensを取得
        '''
        start_pos = head.chunk.token_pos
        c_size = head.chunk.token_size
        return [tokens[start_pos + i] for i in range(c_size)]

    def _concat_tokens(self, head, tokens, a='no'):
        if head is None or head.chunk is None:
            print('Error: ', end='')
            print(a)
            return ''
        tokens_in_chunk = self._get_tokens_in_chunk(head, tokens)
        words = map(lambda x: x.surface, tokens_in_chunk)
        return ''.join(words)

    def _to_tokens(self, tree) -> []:
        ''' 解析済みの木からトークンを取得する '''
        return [tree.token(i) for i in range(0, tree.size())]

    def _split_one_sentence(self) -> [str]:
        ''' 文章を文に切り分ける '''
        sentence = self._sentence_clean(self.term_text)
        sentences = re.split('[。\n]', sentence)
        return sentences

    def _sentence_clean(self, sentence: str) -> str:
        ''' 文のなかの()を除去 '''
        a = '（'
        b = '）'
        while a in sentence:
            head = sentence.split(a)[0]
            tail = a.join(sentence.split(a)[1:])
            for (i, s) in enumerate(tail):
                if s == b:
                    tail = tail[i+1:]
                    break
            sentence = head + tail
        return sentence

    def run(self):
        ''' 解析を実行 '''
        if self._DEBUG:
            print('含まれている文 =>', end='')
            print(len(self._split_one_sentence()))
        for s in self._split_one_sentence():
            if self._DEBUG:
                print('one: {0}'.format(s))
            self._analysis(s)

    def out(self) -> [str]:
        ''' 警告すべき文の構文情報付き要約文を返す '''
        return self.msgs
