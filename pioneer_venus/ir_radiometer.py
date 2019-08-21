
"""support for Pioneer Venus Orbiting Instrument
   Infrared Radiometer (OIR)"""

import numpy as np

def get_radiance(orbit, time):
    """get IR radiance for given orbit number and time"""
    
    length, scale, offset, peaks = 100, 20, 25, 16
    
    values = np.random.rand(length) * scale + offset
 
    index = np.int16(np.random.uniform(0, length, size=(peaks, )))
    values[index] += 2 * scale
    index = np.int16(np.random.uniform(0, length, size=(peaks, )))
    values[index] += 1 * scale
    index = np.int16(np.random.uniform(0, length, size=(peaks, )))
    values[index] += 3 * scale
    return values

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    s = get_radiance(110, 342)
    plt.xlabel('Wavelength')
    plt.ylabel('IR Radiance')
    plt.plot(s)