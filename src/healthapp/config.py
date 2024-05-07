# All application configuration options are stored here!

LOGIN_FILE = "secure_auth"     # The file (&sub directory) to store login information (username/password)
USER_DATA_FILE = "user_data"   # The file (&sub directory) to store the user data

USERNAME_REQUIREMENTS = {
    "min_length": 6,           # Min length of username (<= max)
    "max_length": 99,          # Max length of username (>= min)
    "spaces_allowed": False    # False/True
}

PASSWORD_REQUIREMENTS = {
    "min_length": 8,           # Min length of password (<= max)
    "max_length": 99,          # Max length of password (>= min)
    "spaces_allowed": False,   # False/True
    "numbers_required": 0,     # Numbers required (0 for none required)
    "special_required": 0      # Special characters (any non a-Z 0-9 characters) required (0 for none required)
}

# Cognitive spelling file
COGNITIVE_SPELLING_FILE = "resources/questions.txt"

# The machine learning model files
ML_MODEL_FILES = {
    "heart_disease": "resources/machine_learning/HeartDisease-1.1.3.pkl",
}

# Pose detection type: (thunder = bigger slower accurate / lightning = smaller faster less-accurate)
POSE_DETECTION_TYPE = "lightning"
# Confidence score for pose detection, 1 = 100% confidence, 0 = 0% confidence
POSE_DETECTION_CONFIDENCE = 0.4

POSE_PHOTO_RESULTS_FILE = "pose-results.png"
POSE_VIDEO_RESULTS_FILE = "pose-results.gif"