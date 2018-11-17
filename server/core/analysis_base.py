#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from abc import ABCMeta


class AnalysisBase(metaclass=ABCMeta):
    verb_dic = []
    nominative_dic = []
    warn_word_dic = []
    cp = None
    _DEBUG: bool = True
    # _DEBUG: bool = False

    def __init__(self,
                 term_text: str) -> None:
        self.term_text = term_text
        return None


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
