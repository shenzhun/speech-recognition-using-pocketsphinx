1. find the installation directory

/usr/local/bin

2. the tools below will be used to train the language model

allen@allenalux:/usr/local/bin$ ls -l | grep m
-rwxr-xr-x 1 root root 12997 Aug 16 17:21 binlm2arpa
-rwxr-xr-x 1 root root 27855 Aug 16 17:21 evallm
-rwxr-xr-x 1 root root 42843 Aug 16 17:21 idngram2lm
-rwxr-xr-x 1 root root 16023 Aug 16 17:21 idngram2stats
-rwxr-xr-x 1 root root 43286 Aug 16 17:21 lm_combine
-rwxr-xr-x 1 root root 35982 Aug 16 17:21 lm_interpolate
-rwxr-xr-x 1 root root 18165 Aug 16 17:21 mergeidngram
-rwxr-xr-x 1 root root 17886 Aug 16 17:21 ngram2mgram
-rwxr-xr-x 1 root root 17351 Aug 16 17:21 text2idngram
-rwxr-xr-x 1 root root 18809 Aug 16 17:21 text2wngram
-rwxr-xr-x 1 root root 25899 Aug 16 17:21 wngram2idngram


Given a large corpus of text in a file a.text, but no specified vocabulary

Compute the word unigram counts 

cat a.text | text2wfreq > a.wfreq
Convert the word unigram counts into a vocabulary consisting of the 20,000 most common words 

cat a.wfreq | wfreq2vocab -top 20000 > a.vocab
Generate a binary id 3-gram of the training text, based on this vocabulary

cat a.text | text2idngram -vocab a.vocab > a.idngram
Convert the idngram into a binary format language model 

idngram2lm -idngram a.idngram -vocab a.vocab -binary a.binlm
Compute the perplexity of the language model, with respect to some test text b.text

evallm -binary a.binlm
Reading in language model from file a.binlm
Done.
evallm : perplexity -text b.text 
Computing perplexity of the language model with respect 
to the text b.text 
Perplexity = 128.15, Entropy = 7.00 bits 
Computation based on 8842804 words. 
Number of 3-grams hit = 6806674 (76.97%) 
Number of 2-grams hit = 1766798 (19.98%) 
Number of 1-grams hit = 269332 (3.05%) 
1218322 OOVs (12.11%) and 576763 context cues were removed from the calculation. 
evallm : quit
Alternatively, some of these processes can be piped together:

cat a.text | text2wfreq | wfreq2vocab -top 20000 > a.vocab
cat a.text | text2idngram -vocab a.vocab | \
   idngram2lm -vocab a.vocab -idngram - \
   -binary a.binlm -spec_num 5000000 15000000
echo "perplexity -text b.text" | evallm -binary a.binlm 
