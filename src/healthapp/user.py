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
import json
import toga

from healthapp.config import USER_DATA_FILE


class User:
    def __init__(self, app: toga.App, first: str = "", last: str = "", username: str = "", sex: 0|1 = 0) -> None:
        self.app = app
        self.first = first
        self.last = last
        self.username = username
        self.sex = sex # 1 = Male, 0 = Female

        # These could be None as filled by user whenever.
        self.age = None
        # add other info from user here.

    def save(self) -> str:
        data = {
            "first": self.first,
            "last": self.last,
            "username": self.username,
            "sex": self.sex,

            "age": self.age
        }
        data = json.dumps(data).encode("utf-8")
        self.app.paths.data.joinpath(USER_DATA_FILE).resolve().write_bytes(data)

    def load(self):
        data = self.app.paths.data.joinpath(USER_DATA_FILE).resolve().read_bytes().decode("utf-8")
        data = json.loads(data)
        self.first = data["first"]
        self.last = data["last"]
        self.username = data["username"]
        self.sex = data["sex"]
        self.age = data["age"]

    def __str__(self) -> str:
        return f"User[first: {self.first}, last: {self.last}, username: {self.username}, sex: {self.sex}, age: {self.age}]"
