#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 16:11:52 2018

@author: root
"""

import spacy
nlp = spacy.load('en')

tokens = nlp(u'dog cat horse apple banana peach')

for token1 in tokens:
    for token2 in tokens:
        print(token1, token2, token1.similarity(token2))