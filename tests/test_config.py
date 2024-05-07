from pathlib import Path
import src.healthapp.config as config

app_path = Path("src/healthapp")

def test_keys_exist():
    "Test all config keys exist."

    assert hasattr(config, "LOGIN_FILE")
    assert hasattr(config, "USER_DATA_FILE")
    assert hasattr(config, "USERNAME_REQUIREMENTS")
    assert 'min_length' in config.USERNAME_REQUIREMENTS
    assert 'max_length' in config.USERNAME_REQUIREMENTS
    assert 'spaces_allowed' in config.USERNAME_REQUIREMENTS
    assert hasattr(config, "PASSWORD_REQUIREMENTS")
    assert 'min_length' in config.PASSWORD_REQUIREMENTS
    assert 'max_length' in config.PASSWORD_REQUIREMENTS
    assert 'spaces_allowed' in config.PASSWORD_REQUIREMENTS
    assert 'numbers_required' in config.PASSWORD_REQUIREMENTS
    assert 'special_required' in config.PASSWORD_REQUIREMENTS
    assert hasattr(config, "COGNITIVE_SPELLING_FILE")
    assert hasattr(config, "ML_MODEL_FILES")
    assert 'heart_disease' in config.ML_MODEL_FILES
    assert hasattr(config, "POSE_DETECTION_TYPE")
    assert hasattr(config, "POSE_DETECTION_CONFIDENCE")
    assert hasattr(config, "POSE_PHOTO_RESULTS_FILE")
    assert hasattr(config, "POSE_VIDEO_RESULTS_FILE")

def test_values():
    "Test all the config values to see if they are of correct type/range."

    assert isinstance(config.LOGIN_FILE, str)
    assert len(config.LOGIN_FILE) > 0


    assert isinstance(config.USER_DATA_FILE, str)
    assert len(config.USER_DATA_FILE) > 0


    assert isinstance(config.USERNAME_REQUIREMENTS['min_length'], int)
    assert config.USERNAME_REQUIREMENTS['min_length'] > 0

    assert isinstance(config.USERNAME_REQUIREMENTS['max_length'], int)
    assert config.USERNAME_REQUIREMENTS['max_length'] > 0
    assert config.USERNAME_REQUIREMENTS['max_length'] >= config.USERNAME_REQUIREMENTS['min_length']

    assert isinstance(config.USERNAME_REQUIREMENTS['spaces_allowed'], bool)


    assert isinstance(config.PASSWORD_REQUIREMENTS['min_length'], int)
    assert config.PASSWORD_REQUIREMENTS['min_length'] > 0

    assert isinstance(config.PASSWORD_REQUIREMENTS['max_length'], int)
    assert config.PASSWORD_REQUIREMENTS['max_length'] > 0
    assert config.PASSWORD_REQUIREMENTS['max_length'] >= config.PASSWORD_REQUIREMENTS['min_length']

    assert isinstance(config.PASSWORD_REQUIREMENTS['spaces_allowed'], bool)

    assert isinstance(config.PASSWORD_REQUIREMENTS['numbers_required'], int)
    assert config.PASSWORD_REQUIREMENTS['numbers_required'] >= 0

    assert isinstance(config.PASSWORD_REQUIREMENTS['special_required'], int)
    assert config.PASSWORD_REQUIREMENTS['special_required'] >= 0


    assert isinstance(config.COGNITIVE_SPELLING_FILE, str)
    assert len(config.COGNITIVE_SPELLING_FILE) > 0
    assert Path.exists(app_path / config.COGNITIVE_SPELLING_FILE)


    assert isinstance(config.ML_MODEL_FILES['heart_disease'], str)
    assert len(config.ML_MODEL_FILES['heart_disease']) > 0
    assert Path.exists(app_path / config.ML_MODEL_FILES['heart_disease'])


    assert isinstance(config.POSE_DETECTION_TYPE, str)
    assert config.POSE_DETECTION_TYPE in ['lightning', 'thunder']


    assert isinstance(config.POSE_DETECTION_CONFIDENCE, float)
    assert config.POSE_DETECTION_CONFIDENCE > 0.0
    assert config.POSE_DETECTION_CONFIDENCE < 1.0


    assert isinstance(config.POSE_PHOTO_RESULTS_FILE, str)
    assert len(config.POSE_PHOTO_RESULTS_FILE) > 0


    assert isinstance(config.POSE_VIDEO_RESULTS_FILE, str)
    assert len(config.POSE_VIDEO_RESULTS_FILE) > 0