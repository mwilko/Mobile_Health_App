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


class User:

    def __init__(self, first: str, last: str, username: str, sex: 0|1) -> None:
        self.first = first
        self.last = last
        self.username = username
        self.sex = sex # 1 = Male, 0 = Female

        # These could be None as filled by user whenever.
        self.age = None
        # add other info from user here.

    def __str__(self) -> str:
        return f"User[first: {self.first}, last: {self.last}, username: {self.username}, sex: {self.sex}, age: {self.age}]"
    