from ..uv_spectrometer import get_spectrum
import numpy as np

def setup_module():
    pass 

def teardown_module():
    pass

def setup_function():
    pass
 
def teardown_function():
    pass    


#------- actual test cases -------------------------------

def test_values():    
    s = get_spectrum(1000, 34)
    assert np.all(s < 10)
    assert np.all(s >= 0)

def test_structure():
    s = get_spectrum(2000, 491)
    assert len(s) == 256

