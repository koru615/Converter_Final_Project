from new_method import *
from decimal import *

def test_decimal():
    assert convert_length("inches", "feet", 12) == 1
    assert convert_length("yards", "miles", 456) == 0.259
    assert convert_length("millimeter", "inches", 32) == 1.26