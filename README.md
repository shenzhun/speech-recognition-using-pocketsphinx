speech-recognition-using-pocketsphinx
=====================================

Using pocketsphinx and NLTK to build speech recognition system

Overview
--------
   CMU Sphinx toolkit <code> http://cmusphinx.sourceforge.net/wiki/tutorialoverview </code>

   Backgroud <code> http://cmusphinx.sourceforge.net/wiki/tutorialbeforestart </code>

Download
--------
   CMU Sphinx Downloads <code> http://cmusphinx.sourceforge.net/wiki/download</code>
   
   The DARPA TIMIT Acoustic-Phonetic Continuous Speech Corpus(TIMIT) -- Training and Test Data NIST Speech Disc CD1-1.1
   <code> http://www.ldc.upenn.edu/Catalog/catalogEntry.jsp?catalogId=LDC93S1 </code>


Installation
------------
1. Decoder: pocketsphinx and sphinxbase
   
   Install Guide <code>http://cmusphinx.sourceforge.net/wiki/tutorialpocketsphinx</code> 

   Install on Ubuntu <code> sudo apt-get install pocketsphinx sphinxbase</code>
   
   Details about the installed packages <code>https://launchpad.net/ubuntu/+source/pocketsphinx</code>
  
2. Language Model Training Tool: cmuclmtk

   Install Guide <code>http://cmusphinx.sourceforge.net/wiki/cmuclmtkdevelopment</code>

3. Acoustic Model Training: sphinxtrain 

   Same as cmuclmtk 

Using pocketsphinx
------------------
1. Acoustic Model <code>/usr/share/pocketsphinx/model/hmm/wsj1/</code>
2. Language Model <code>/usr/share/pocketsphinx/model/lm/wsj/wlist5o.3e-7.vp.tg.lm.DMP</code>
3. Dictionary     <code>/usr/share/pocketsphinx/model/lm/wsj/wlist5o.dic</code>
4. Corpus <code>timit/test/dr1/faks0</code>
5. Accurancy  average = 80.31%   min = 56.52%  max = 100%

Training
---------
1. Training Language Model

  lmtool <code> http://www.speech.cs.cmu.edu/tools/lmtool.html </code>
  + create corpus .txt file
  + open http://www.speech.cs.cmu.edu/tools/lmtool.html, submit the corpus .txt file and download the .tar.gz file
  + decompress the .tar.gz file and find .lm, .dic, 
 
  simpleLM <code> https://github.com/skerit/cmusphinx/tree/master/SimpleLM </code>
 
  cmuclmtk <code> http://cmusphinx.sourceforge.net/wiki/tutoriallm </code>
           <code> http://www.speech.cs.cmu.edu/SLM/toolkit_documentation.html </code>
  Given a large corpus of text in a file a.text, but no specified vocabulary
  + Compute the word unigram counts 

   cat a.text | text2wfreq > a.wfreq
  + Convert the word unigram counts into a vocabulary consisting of the 20,000 most common words 

   cat a.wfreq | wfreq2vocab -top 20000 > a.vocab
  + Generate a binary id 3-gram of the training text, based on this vocabulary

   cat a.text | text2idngram -vocab a.vocab > a.idngram
  + Convert the idngram into a binary format language model 

   idngram2lm -idngram a.idngram -vocab a.vocab -binary a.binlm
  + Compute the perplexity of the language model, with respect to some test text b.text

   evallm -binary a.binlm

   Alternatively, some of these processes can be piped together:

   cat a.text | text2wfreq | wfreq2vocab -top 20000 > a.vocab
   cat a.text | text2idngram -vocab a.vocab | \
   idngram2lm -vocab a.vocab -idngram - \
   -binary a.binlm -spec_num 5000000 15000000
   echo "perplexity -text b.text" | evallm -binary a.binlm 

2. Training Acoustic Model
  
   <code> http://cmusphinx.sourceforge.net/wiki/tutorialam </code>

Testing
---------
1. TIMIT corpus

2. Capture sound

Using python to capture sound <code>http://people.csail.mit.edu/hubert/pyaudio/</code>

