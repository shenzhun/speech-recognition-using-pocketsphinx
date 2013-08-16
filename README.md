speech-recognition-using-pocketsphinx
=====================================

Using pocketsphinx and NLTK to build speech recognition system

Installation
------------
1. Decoder:pocketsphinx and sphinxbase
sudo apt-get install gstreamer0.10-pocketsphinx libpocketsphinx-dev libpocketsphinx1 libpython-dbg libpython2.7-dbg libsphinxbase1 pocketsphinx-hmm-en-hub4wsj pocketsphinx-hmm-en-tidigits pocketsphinx-hmm-tidigits pocketsphinx-hmm-wsj1 pocketsphinx-hmm-zh-tdt pocketsphinx-lm-en-hub4 pocketsphinx-lm-wsj pocketsphinx-lm-zh-hans-gigatdt pocketsphinx-lm-zh-hant-gigatdt pocketsphinx-utils python-dbg python-pocketsphinx python-pocketsphinx-dbg python-sphinxbase python2.7-dbg

2. Language Model Training Tool:muclmtk
tar -xvfz cmuclmtk-{version}.tar.gz
cd cmuclmtk-{version}/
sh autogen.sh
./configure
make install

3. Acoustic Model Training:sphinxtrain 
tar -xvfz sphinxtrain-{version}.tar.gz
cd sphintrain-{version}/
sh autogen.sh
./configure
make install (only python, perl scripts)


Training
-------------

1. TIMIT speech corpus
2. Lanuage Model
3. Acoustic Model

