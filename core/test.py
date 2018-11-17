#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from term_analysis_base import TermAnalysisBase


class TestCoreTermAnalysisBase(unittest.TestCase):
    sentence = '当社はユーザーからあらゆる情報を取得します'
    analysis = TermAnalysisBase(sentence, dic=None)
    tree = analysis.cp.parse(sentence)

    def test__to_tokens(self):
        tokens = self.analysis._to_tokens(self.tree)
        tokens = list(map(lambda x: x.surface, tokens))
        self.assertEqual(tokens,
                         ['当社', 'は', 'ユーザー', 'から', 'あらゆる',
                          '情報', 'を', '取得', 'し', 'ます'])

    def test__find_verb(self):
        tokens = self.analysis._to_tokens(self.tree)
        verb = self.analysis._find_verb(tokens)
        self.assertEqual(verb.surface, '取得')

        tokens = self.analysis2._to_tokens(self.tree2)
        verb = self.analysis2._find_verb(tokens)
        self.assertEqual(verb.surface, '譲渡')

    def test__find_nominative_case(self):
        tokens = self.analysis._to_tokens(self.tree)
        verb = self.analysis._find_verb(tokens)
        verb_head_id = self.analysis._get_chunk_id_of(verb, tokens)
        nominative = self.analysis._find_nominative_case(verb_head_id, tokens)
        nominative_case = self.analysis._concat_tokens(nominative, tokens)
        # print(nominative.surface)
        # print(nominative_case)
        self.assertEqual(nominative.surface, '当社')
        self.assertEqual(nominative_case, '当社は')

        tokens = self.analysis2._to_tokens(self.tree2)
        verb = self.analysis2._find_verb(tokens)
        verb_head_id = self.analysis2._get_chunk_id_of(verb, tokens)
        nominative = self.analysis2._find_nominative_case(verb_head_id, tokens)
        nominative_case = self.analysis2._concat_tokens(nominative, tokens)
        # print(nominative.surface)
        # print(nominative_case)
        self.assertEqual(nominative.surface, 'ユーザー')
        self.assertEqual(nominative_case, 'ユーザーは、')

    def test__find_object_case(self):
        tokens = self.analysis._to_tokens(self.tree)
        verb = self.analysis._find_verb(tokens)
        verb_head_id = self.analysis._get_chunk_id_of(verb, tokens)
        object = self.analysis._find_object_case(verb_head_id, tokens)
        object_case = self.analysis._concat_tokens(object, tokens)
        # print(object.surface)
        # print(object_case)
        self.assertEqual(object.surface, '情報')
        self.assertEqual(object_case, '情報を')

        tokens = self.analysis._to_tokens(self.tree2)
        verb = self.analysis._find_verb(tokens)
        verb_head_id = self.analysis._get_chunk_id_of(verb, tokens)
        object = self.analysis._find_object_case(verb_head_id, tokens)
        object_case = self.analysis._concat_tokens(object, tokens)
        # print(object.surface)
        # print(object_case)
        self.assertEqual(object.surface, '権利')
        self.assertEqual(object_case, '権利を、')

    def test_run(self):
        self.analysis.run()
        msgs = self.analysis.out()
        self.assertEqual(msgs[0]['text'], '当社は情報を取得します')

        self.analysis2.run()
        msgs = self.analysis2.out()
        self.assertEqual(msgs[0]['text'], 'ユーザーは、権利を、譲渡します')


if __name__ == '__main__':
    unittest.main()
