#!/usr/bin/env python
import sys,os

def decodeSpeech(hmmd,lmdir,dictp,wavfile):
        """
        Decodes a speech file
        """
        try:
                import pocketsphinx as ps
                import sphinxbase
        except:
                print """Pocket sphinx and sphixbase is not installed
                in your system. Please install it with package manager.
                """
        
        speechRec = ps.Decoder(hmm = hmmd, lm = lmdir, dict = dictp)
        wavFile = file(wavfile,'rb')
        wavFile.seek(44)
        speechRec.decode_raw(wavFile)
        result = speechRec.get_hyp()

        return result[0]


if __name__ == "__main__":
        hmdir = ""
        lmd = ""
        dictd = ""
        wavfile = ""
        recognised = decodeSpeech(hmdir,lmd,dictd,wavfile)
        print recognised
