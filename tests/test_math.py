"""
Testing for the math module
"""

import super_duper_funicular as fcm 
import pytest

def test_add():
    assert fcm.math.add(5, 2) == 7
    assert fcm.math.mult(2, 5) == 10

testdata = [
    (2, 5, 10),
    (1, 2, 2)
    ]
@pytest.mark.parametrize("a, b, expected", testdata)
def test_mult(a, b, expected):
    assert fcm.math.mult(a, b) == expected
