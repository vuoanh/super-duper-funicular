"""
Testing for the math module
"""

import super_duper_funicular as fcm 
import pytest

def test_add():
    assert fcm.math.add(5, 2) == 7
    assert fcm.math.mult(2, 5) == 10

testdata1 = [
    (2, 5, 10),
    (1, 2, 2)
    ]

testdata2 = [
    (4, 2),
    (0, 0),
    (-5, 0)
    ]
@pytest.mark.parametrize("a, b, expected", testdata1)
def test_mult(a, b, expected):
    assert fcm.math.mult(a, b) == expected

@pytest.mark.parametrize("a, expected", testdata2)
def test_sqrt(a, expected):
    assert fcm.math.sqrt(a) == expected

