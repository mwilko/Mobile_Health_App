'''
Constructed at login/register on app start, available in every page after (via self.app.user).
User class to hold ALL of the user data including but not limited to:
- first name
- last name
- username
- sex
- age
- etc etc (more details from questions in app etc)
'''
#-------------------------------------------------------------------------------------------------------#
import json
import toga

from healthapp.config import USER_DATA_FILE
#-------------------------------------------------------------------------------------------------------#

class User:
    def __init__(self, app: toga.App, first: str = "", last: str = "", username: str = "", sex: bool = False) -> None:
        self.app = app
        self.first = first
        self.last = last
        self.username = username
        self.sex = sex  # True = Male, False = Female

        # These could be None as filled by the user whenever.
        self.age = None
        self.height = None
        self.weight = None
        self.sleep = None
        self.bmi = None
        self.calories = None
        self.heart_rate = None
        self.exercise = None
        self.cognitive = 0
        # add other info from the user here.
    
    	# For heart-disease MLA
        self.highbp = 0 #[1,0]
        self.highcol = 0 #[1,0]
        self.smoker = 0 #[1,0]
        self.stroke = 0 #[1,0]
        self.diabetes = 0 #[1,0]
        self.physact = 0 #[1,0]
        self.alcohol = 0 #[1,0]
        self.physhealth = 0 #[Int]
        self.diffwalking = 0 #[1,0]


    # When user enters their height and weight this updates the BMI    
    def update_bmi(self):
        if self.height is not None and self.weight is not None:
   		    # Convert height to meters
            height_meters = self.height / 100  # Assuming height is in centimeters

    	    # Calculate BMI
            self.bmi = round(self.weight / (height_meters ** 2))
        else:
            self.bmi = None


    def save(self) -> None:
        data = {
            "first": self.first,
            "last": self.last,
            "username": self.username,
            "sex": self.sex,
            "age": self.age,
            "height": self.height,
            "weight": self.weight,
            "sleep": self.sleep,
            "bmi": self.bmi,
            "calories": self.calories,
            "heart_rate": self.heart_rate,
            "exercise": self.exercise,
            "cognitive": self.cognitive,

            # For heart-disease MLA
            "highbp": self.highbp,
            "highcol": self.highcol,
            "smoker": self.smoker,
            "stroke": self.stroke,
            "diabetes": self.diabetes,
            "physact": self.physact,
            "alcohol": self.alcohol,
            "physhealth": self.physhealth,
            "diffwalking": self.diffwalking
        }
        data = json.dumps(data).encode("utf-8")
        
        try:
            filepath = self.app.paths.data.joinpath(USER_DATA_FILE)
            filepath.resolve().write_bytes(data)
        except IOError as e:
            print(f"Error saving user data: {e}")

    def load(self) -> None:
        filepath = self.app.paths.data.joinpath(USER_DATA_FILE)
        
        try:
            if filepath.is_file():
                data = filepath.resolve().read_bytes().decode("utf-8")
                data = json.loads(data)
                self.first = data["first"]
                self.last = data["last"]
                self.username = data["username"]
                self.sex = data["sex"]
                
                # Optionals:
                self.age = data.get("age", None)
                self.height = data.get("height", None)
                self.weight = data.get("weight", None)
                self.sleep = data.get("sleep", None)
                self.bmi = data.get("bmi", None)
                self.calories = data.get("calories", None)
                self.heart_rate = data.get("heart_rate", None)
                self.exercise = data.get("exercise", None)
                self.cognitive = data.get("cognitive", 0)

                # For heart-disease MLA
                self.highbp = data.get("highbp", 0)
                self.highcol = data.get("highcol", 0)
                self.smoker = data.get("smoker", 0)
                self.stroke = data.get("stroke", 0)
                self.diabetes = data.get("diabetes", 0)
                self.physact = data.get("physact", 0)
                self.alcohol = data.get("alcohol", 0)
                self.physhealth = data.get("physhealth", 0)
                self.diffwalking = data.get("diffwalking", 0)
        except IOError as e:
            print(f"Error loading user data: {e}")

    def __str__(self) -> str:
        return f"User[first: {self.first}, last: {self.last}, username: {self.username}, sex: {self.sex}, age: {self.age}, height: {self.height}, weight: {self.weight}, sleep: {self.sleep}, bmi: {self.bmi}, calories: {self.calories}, heart_rate: {self.heart_rate}, exercise: {self.exercise}, cognitive: {self.cognitive}, highbp: {self.highbp}, highcol: {self.highcol}, smoker: {self.smoker}, stroke: {self.stroke}, diabetes: {self.diabetes}, physact: {self.physact}, alcohol: {self.alcohol}, physhealth: {self.physhealth}, diffwalking: {self.diffwalking}]"
