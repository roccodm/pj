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
