import numpy

class WaveForm:
    def __init__(self,amplitude = 1,frequency = 10,phase = 0):
        self.amplitude = amplitude
        self.frequency = 10
        self.phase = 0
        self.y = lambda x : self.amplitude*numpy.sin(2*numpy.pi*self.frequency + numpy.deg2rad(self.phase))

    def y(self,t):
        return self.amplitude * numpy.sin(2 * numpy.pi * self.frequency*t + numpy.deg2rad(self.phase))