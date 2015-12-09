""" Synthesizes a blues solo algorithmically """

from Nsound import *
import numpy as np
from random import choice

def add_note(out, instr, key_num, duration, bpm, volume):
    """ Adds a note from the given instrument to the specified stream

        out: the stream to add the note to
        instr: the instrument that should play the note
        key_num: the piano key number (A 440Hzz is 49)
        duration: the duration of the note in beats
        bpm: the tempo of the music
        volume: the volume of the note
	"""
    freq = (2.0**(1/12.0))**(key_num-49)*440.0
    stream = instr.play(duration*(60.0/bpm),freq)
    stream *= volume
    out << stream


# this controls the sample rate for the sound file you will generate
sampling_rate = 44100.0
Wavefile.setDefaults(sampling_rate, 16)

bass = GuitarBass(sampling_rate)	# use a guitar bass as the instrument
solo = AudioStream(sampling_rate, 1)

""" these are the piano key numbers for a 3 octave blues scale in A
	See: http://en.wikipedia.org/wiki/Blues_scale """
blues_scale = [20,23,25,28,30,31,32,35,37,40,42,43,44,47,49,52,54,55,56]
beats_per_minute = 45				# Let's make a slow blues solo
curr_note = choice([0,4,8,12])


licks = [[[2,1.6],[2,0.4],[2,1.6],[2,0.4]], [[-2,1],[-2,1],[-2,1],[-2,1]], [[1,0.7],[1,0.3],[1,0.7],[1,0.3]], [[-1,1.4],[-1,0.6],[-1,1.4],[-1,0.6]], [[2,1.6],[4,0.4],[-1,1.6],[-1,0.4]], [[-1,1.6],[-1,0.4],[4,1.6],[2,0.4]], [[2,1],[-1,1],[4,1],[-1,1]], [[1,0.4],[1,1.6],[4,0.4],[-2,1.6]], [[-2,1],[1,1],[-4,1],[1,1]], [[-1,0.2],[-1,0.8],[-4,0.8],[-2,0.2]], [[1,1],[1,1],[-4,1],[-2,1]], [[-2,0.7],[-4,0.3],[1,0.7],[1,0.3]]]
volume = [0.9, 1, 1.1]

for i in range(16):
    if curr_note == 0:
        lick = choice([licks[0],licks[2],licks[4],licks[6],licks[7]])
    elif curr_note == 4:
        lick = choice([licks[0],licks[2],licks[3],licks[4],licks[5],licks[6],licks[7]])
    elif curr_note == 12:
        lick = choice([licks[1],licks[2],licks[3],licks[5],licks[6],licks[8],licks[9],licks[10],licks[11]])       
    elif curr_note == 16:
        lick = choice([licks[1],licks[3],licks[8],licks[9],licks[11]])
    else:
        lick = choice(licks)
    for note in lick:
        curr_note += note[0]
        add_note(solo, bass, blues_scale[curr_note], note[1], beats_per_minute, choice(volume))


backing_track = AudioStream(sampling_rate, 1)
Wavefile.read('backing.wav', backing_track)


m = Mixer()

solo *= 1.0           # adjust relative volumes to taste
backing_track *= 3.0

m.add(2.25, 0, solo)    # delay the solo to match up with backing track    
m.add(0, 0, backing_track)

m.getStream(500.0) >> "slow_blues.wav"
