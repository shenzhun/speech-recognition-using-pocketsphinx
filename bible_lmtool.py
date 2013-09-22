#!/bin/env python

import nltk

sents = nltk.corpus.gutenberg.sents('bible-kjv.txt')
for i in sents:
	for j in i:
		if j.isalpha() == False:
			i.remove(i.index(j))
		print i

