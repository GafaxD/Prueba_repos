import matplotlib.pyplot as plt
import numpy as np
import colorednoise as cn
import simpleaudio as sa
from time import sleep

class Functions:

    def __init__(self,seconds = 1, graph = False, load = False) -> None:
        self.seconds = seconds
        self.graph = graph
        self.load = load
        self.fs = 44100
    
    def pink_noise_gen(self):
        if self.load:
            note = np.loadtxt("note.txt")
        else:
            note = 0.00001*cn.powerlaw_psd_gaussian(1, self.fs * self.seconds)
            #np.savetxt("note.txt", note)

        if self.graph != False:
            tiempo = np.linspace(0, self.seconds, self.seconds * self.fs, False)
            frequency = np.fft.rfftfreq(len(tiempo))
            note_f = np.abs(np.fft.rfft(note))
            self.graphing_log(note_f,frequency)
            self.graphing(note, tiempo)
        
        self.listen(note, self.fs)
        

    def sine_gen(self, frequency=440):
        note = np.sin(frequency * self.seconds * 2 * np.pi)
        self.listen(note, self.fs)
        if self.graph != False:
            tiempo = np.linspace(0, self.seconds, self.seconds * self.fs, False)
            self.graphing(note,tiempo)

    def listen(self,note, samples):
        audio = note * (2**15 - 1) / np.max(np.abs(note))
        audio = audio.astype(np.int16)
        play_obj = sa.play_buffer(audio, 1, 2, samples)
        play_obj.wait_done()

    def graphing(self, note, tiempo):
        plt.plot(tiempo, note, color='pink', linewidth=1)
        plt.grid(True)
        plt.title('Colored Noise for β=')
        plt.xlabel('Samples (time-steps)')
        plt.ylabel('Amplitude(t)', fontsize='large')
        plt.show()

    def graphing_log(self, note, frequency):
        plt.figure(figsize=(8, 8))
        plt.loglog(frequency, note, color="pink")
        plt.legend(['pink'])
        plt.ylim([1e-3, None])
        plt.show()

def main():
    TIEMPOS = 3
    Functions(TIEMPOS).pink_noise_gen()

if __name__ == "__main__":
    main()