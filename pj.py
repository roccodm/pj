########################################################################
# PJ - Peak Jumper
#-----------------------------------------------------------------------
# Simple python utility that analyzes all the wavefiles into a directory
# to discover RMS level variation of a given ratio.
# It is possible to specify the chunck size (in seconds) that will be
# analyzed.
# Has been specifically developed in PAM acquisition field to discover
# particular events that could occours (Airgun explotion, hydrophone out
# of water, etc.)
# The output is in csv-like format (\t separator) from stdout
#-----------------------------------------------------------------------
# Author: Rocco De Marco (roccodm @ github)
# License: CC 3.0 IT, BY NC
#-----------------------------------------------------------------------
import scipy
import struct
import scipy.fftpack
import matplotlib.pyplot as plt
from scipy.io import wavfile
import glob
# parameters, change it as you need
#-----------------------------------------------------

#chunk size, in seconds. Can be also a float value
chunk_size=3

#trigger level, between 0 and 1
trigger_level=0.05

# end parameters, below this line you shouldn't edit
#-----------------------------------------------------

# list all wavefiles into current directory
files=glob.glob("*.wav")


print ("Filename\tOffset\tRMS\tVar")
#MainLoop
for file in files:
   samplerate,wav = wavfile.read(file)
   res=int(str(wav.dtype)[3:])
   wavData=wav/(2.**(res-1))
   bufferSize=int(samplerate*chunk_size)
   n_chunck=int(len(wavData)/bufferSize)
   # the wavefile is splitted in chunks
   for i in range(1,(n_chunck)):
      chunck=wavData[(1+bufferSize*(i-1)):(bufferSize*i+1)]
      rms=scipy.sqrt(scipy.mean(scipy.square(chunck)))
      if i==1:
         prev=rms
      else:
         var=1-(rms/prev)
         if var>=trigger_level:
            pos=float(i)*chunk_size
            print "%s\t%f\t%f\t%f" % (file, pos, rms, var)
         prev=rms



