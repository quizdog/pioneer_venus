
"""support for Pioneer Venus Orbiting Instrument
   Ultraviolet Spectrometer (OUVS)"""

import numpy as np

def get_spectrum(orbit, time):
    """get spectrum for given orbit number and time"""
    
    length, offset, peaks = 256, 1, 9
    if orbit < 105:
        scale = 2
    else:
        scale = 1
    
    spectrum = np.random.rand(length) * scale + offset
 
    index = np.int16(np.random.uniform(0, length, size=(peaks, )))
    spectrum[index] += 2 * scale
    index = np.int16(np.random.uniform(0, length, size=(peaks, )))
    spectrum[index] += 1 * scale
    index = np.int16(np.random.uniform(0, length, size=(peaks, )))
    spectrum[index] += 3 * scale
    return spectrum

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    s = get_spectrum(10, 33423)
    plt.xlabel('Wavelength')
    plt.ylabel('UV Radiance')
    plt.plot(s)
