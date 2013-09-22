#!/bin/env python

import nltk

sents = nltk.corpus.gutenberg.sents('bible-kjv.txt')
with open('bible_corpus.txt', 'a') as bc:
	for sent in sents:
		sent_no_punct = []
		for word in sent:
			if word.isalpha():
				sent_no_punct.append(word)
		bc.write(' '.join(sent_no_punct) + '\n')


