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
 
  simpleLM <code> https://github.com/skerit/cmusphinx/tree/master/SimpleLM </code>
 
  cmuclmtk <code> http://cmusphinx.sourceforge.net/wiki/tutoriallm </code>
           <code> http://www.speech.cs.cmu.edu/SLM/toolkit_documentation.html </code>

2. Training Acoustic Model

