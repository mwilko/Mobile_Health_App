from pathlib import Path
import pytest

class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)

def test_mla_valid():
    "Test the MLA perform_prediction using demo app"
    
    # Since the app is not running, we need to mock the app object
    app = {
        "paths": Struct(**{
            "app": Path("src/healthapp")
        })
    }

    input_data = [[1, 1, 100, 1, 1, 1, 1, 1, 1, 1, 1, 70]] # Sample input data
    from src.healthapp.machine_learning import perform_prediction
    prediction = perform_prediction(Struct(**app), input_data)
    assert prediction is not None
    assert prediction >= 0 and prediction <= 100

def test_mla_invalid():
    # Since the app is not running, we need to mock the app object
    "Test the MLA perform_prediction using demo app"
    
    # Since the app is not running, we need to mock the app object
    app = {
        "paths": Struct(**{
            "app": Path("src/healthapp")
        })
    }

    input_data = [[1, 1, 100, 1, 1, 1, None, 1, 1, 1, 1, 70]] # Sample input data
    from src.healthapp.machine_learning import perform_prediction
    pytest.raises(ValueError, perform_prediction, Struct(**app), input_data)
