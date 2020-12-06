#!/usr/bin/env python
#-*- coding:utf-8 -*-

import random

sentence_list = [
    '千里之行，始于足下',
    '悟以往之不鉴，知来者之可追',
    ''
    '我想不出来啦！'
]

def get_sentence():
    return sentence_list[random.randrange(len(sentence_list))]
