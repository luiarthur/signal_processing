import numpy as np

A4 = 440.0
C0 = A4*pow(2, -4.75)
#name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
name = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    
### NOT CORRECT!!!
def pitch_unvec(freq):
    h = 12 * np.log(freq/A4) / np.log(2)
    octave = int(round(h) // 12 + 4)
    n = int(round(h % 12))
    n = n if n < 12 else 0
    return name[n] + str(octave)

pitch = np.vectorize(pitch_unvec)

piano_freq = []
with open("piano_freq.txt") as f:
    for line in f.readlines():
        piano_freq += [ float(line) ]
    f.close()

piano_freq.reverse()
print pitch(piano_freq)
assert len(set(pitch(piano_freq))) == len(pitch(piano_freq)) == 88


#pitch(559)

### All the pitches on piano
#from collections import OrderedDict
#p_set = pitch(np.arange(28,4188))


