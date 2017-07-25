"""
Testing for the math module
"""

import super_duper_funicular as fcm 
import pytest

def test_add():
    assert fcm.math.add(5, 2) == 7
    assert fcm.math.mult(2, 5) == 10

def test_mult():
    assert fcm.math.mult(2, 3) == 6
