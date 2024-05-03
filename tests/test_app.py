from pathlib import Path
import pytest

from src.healthapp.machine_learning import perform_prediction

class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)

# Since the app is not running, we need to mock the app object
app = Struct(**{
    "paths": Struct(**{
        "app": Path("src/healthapp")
    })
})

def test_mla_valid():
    "Test the MLA perform_prediction using demo app"
    
    input_data = [[1, 1, 100, 1, 1, 1, 1, 1, 1, 1, 1, 70]] # Sample input data
    prediction = perform_prediction(app, input_data)

    assert prediction is not None
    assert prediction >= 0 and prediction <= 100

def test_mla_invalid():
    "Test the MLA perform_prediction using demo app"
    
    input_data = [[1, 1, 100, 1, 1, 1, None, 1, 1, 1, 1, 70]] # Sample input data
    pytest.raises(ValueError, perform_prediction, app, input_data)
