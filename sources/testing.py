import numpy as np
import simpleaudio as sa

BINARY_INT = 2**15 - 1

frequency = 440
fs = 11025
seconds = 1
t = np.linspace(0, seconds, seconds * fs, False)
note = np.sin(frequency * t * 2 * np.pi)
np.savetxt("note.txt",note)
print("note max: ",np.max(np.abs(note)))
print("result 1ft:  ",(BINARY_INT) / np.max(np.abs(note)))
audio = (note) * (BINARY_INT) / np.max(np.abs(note))
np.savetxt("audio.txt",audio)
audio = audio.astype(np.int16)
play_obj = sa.play_buffer(audio, 1, 2, fs)
play_obj.wait_done()
print("finalizado")