import main
import pytest
from pytest import approx

@pytest.mark.parametrize(
    'fahrenheit, celsius', [
        (212,100),
        (98.6,37),
        (70,21.11111),
        (32,0),
        (0,-17.77778),
        (-40,-40)
        ]
    
    )
    
def test_fahrenheit_to_celsius(fahrenheit,celsius):
    assert main.fahrenheit_to_celsius(fahrenheit) == approx(celsius)