import numpy as np

A4 = 440
C0 = A4*pow(2, -4.75)
name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    
### NOT CORRECT!!!
def pitch_unvec(freq):
    h = int(12 * np.log2(freq/C0))
    octave = h // 12
    n = h % 12
    return name[n] + str(octave)

pitch = np.vectorize(pitch_unvec)

piano_freq = []
with open("piano_freq.txt") as f:
    for line in f.readlines():
        piano_freq += [ float(line) ]
    f.close()

piano_freq.reverse()

#pitch(559)

### All the pitches on piano
#from collections import OrderedDict
#p_set = pitch(np.arange(28,4188))
