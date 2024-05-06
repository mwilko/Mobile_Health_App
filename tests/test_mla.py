from pathlib import Path
from random import randint, seed
import time
import pytest

from src.healthapp.machine_learning import perform_prediction

# Since the app is not running, we need to mock the app object
@pytest.fixture
def app():
    class Struct:
        def __init__(self, **entries):
            self.__dict__.update(entries)

    return Struct(**{
        "paths": Struct(**{
            "app": Path("src/healthapp")
        })
    })

def generate_random_data():
    seed(time.time_ns()) # Truly random.
    return [[randint(0,1), randint(0,1), randint(0,100), randint(0,1), randint(0,1), randint(0,1), randint(0,1), randint(0,1), randint(0,100), randint(0,1), randint(0,1), randint(1,120)]]

def test_valid_random(app):
    "Test the MLA perform_prediction using random valid data"
    # Test the MLA 10'000x with random data each time.
    for _ in range(10000):
        input_data = generate_random_data()
        prediction = perform_prediction(app, input_data)
        assert prediction is not None
        assert prediction > 0 and prediction < 100

def test_valid_fixed(app):
    "Test the MLA perform_prediction using demo app"
    
    input_data = [[1, 1, 100, 1, 1, 1, 1, 1, 1, 1, 1, 70]] # Sample input data
    prediction = perform_prediction(app, input_data)

    assert prediction is not None
    assert prediction >= 0 and prediction <= 100

def test_invalid(app):
    "Test the MLA perform_prediction using demo app"
    
    input_data = [[1, 1, 100, 1, 1, 1, None, 1, 1, 1, 1, 70]] # Sample input data
    pytest.raises(ValueError, perform_prediction, app, input_data)
