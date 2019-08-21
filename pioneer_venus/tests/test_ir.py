from ..ir_radiometer import get_radiance
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
    s = get_radiance(1000, 34)
    assert np.all(s < 200)
    assert np.all(s >= 0)

def test_structure():
    s = get_radiance(1000, 34)
    assert len(s) == 100

