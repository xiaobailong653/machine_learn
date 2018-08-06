#!/usr/bin/env python
# -*- coding:utf-8 -*-


import pynlpir

pynlpir.open()
s = '怎么才能把电脑里的垃圾文件删除'
segments = pynlpir.segment(s, pos_names='all', pos_english=False)
for segment in segments:
    print segment[0], '\t', segment[1]

key_words = pynlpir.get_key_words(s, weighted=True)
for key_word in key_words:
    print key_word[0], '\t', key_word[1]

pynlpir.close()

