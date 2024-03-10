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
        # add other info from the user here.

    def save(self) -> None:
        data = {
            "first": self.first,
            "last": self.last,
            "username": self.username,
            "sex": self.sex,
            "age": self.age,
            "height": self.height,
            "weight": self.weight,
            "sleep": self.sleep
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
        except IOError as e:
            print(f"Error loading user data: {e}")

    def __str__(self) -> str:
        return f"User[first: {self.first}, last: {self.last}, username: {self.username}, sex: {self.sex}, age: {self.age}, height: {self.height}, weight: {self.weight}, sleep: {self.sleep}]"