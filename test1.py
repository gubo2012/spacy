#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 15:57:07 2018

@author: root
"""

import spacy
nlp = spacy.load('en')
doc = nlp(u"U.S. stocks ended the week with a deep selloff, leaving them lower for the five days as the White House’s latest trade bluster rattled global financial markets.")
print([(w.text, w.pos_) for w in doc])

#for token in doc:
##    print(token.text)
#    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
#          token.shape_, token.is_alpha, token.is_stop)
    
# NER
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)