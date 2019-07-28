import sys
import os
sys.path.append('../../software/models/')
from utilFunctions import wavread

"""
A1-Part-2: Basic operations with audio

Write a function that reads an audio file and returns the minimum and the maximum values of the audio 
samples in that file.

The input to the function is the wav file name (including the path) and the output should be two floating 
point values returned as a tuple.

If you run your code using oboe-A4.wav as the input, the function should return the following output:  
(-0.83486432, 0.56501967)
"""
def minMaxAudio(inputFile):
    """
    Input:
        inputFile: file name of the wav file (including path)
    Output:
        A tuple of the minimum and the maximum value of the audio samples, like: (min_val, max_val)
    """
    (fs, x) = wavread(inputFile)
    min = x[0]
    max = x[0]
    for val in x:
        if val <= min:
            min = val
        if val >= max:
            max = val

    max_min = (min, max)
    return (max_min)
