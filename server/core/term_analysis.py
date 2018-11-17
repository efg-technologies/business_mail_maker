#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
利用規約解析クラス
'''

# TODO: chunkは別途でクラスにした方が扱いやすい
# TODO: あらかじめ同意したものとみなす系も取りたい

# import CaboCha
from core.term_analysis_base import TermAnalysisBase
# import re


class TermAnalysis(TermAnalysisBase):
    # TODO: 辞書をcsvに変換
    # TODO: 漢字をひらがなに変換した単語を辞書に自動追加
    # TODO: 取りこぼしている助詞の収集
    verb_dic = [
                '獲得',
                '授与',
                '得る',
                '取得',
                '与える',
                '供与',
                '委譲',
                '与える',
                '譲る',
                '提供',
                '捧げる',
                '譲渡',
                '行使']

    nominative_dic = [
            '利用者',
            '会員',
            '契約者',
            'ユーザー',
            '登録者',
            '投稿者',
            'お客様',
            'メンバー',
            '貴方',
            '者',
            '乙',
            'お客さま']
    ヲ格 = ['を', 'に対し']
    カラ格 = ['から']
    ガ格 = ['が', 'は']
    cp = None
    _DEBUG: bool = False
    # _DEBUG: bool = True
