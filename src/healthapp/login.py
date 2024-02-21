import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from toga.validators import MinLength
from hashlib import sha512

from healthapp.user import User

LOGIN_FILE = "secure_auth"     # The file (&sub directory) to store login information (username/password)
USER_DATA_FILE = "secure_data" # The file (&sub directory) to store the user data

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

def getAuthPage(app: toga.App):
    print(app.paths.data.joinpath(LOGIN_FILE).resolve())
    # If the user login file exists, we need to login not signup.
    if app.paths.data.joinpath(LOGIN_FILE).resolve().exists():
        return _LoginPage(app)
    else:
        return _SignupPage(app)


## -- Private classes / functions -- ##


class _LoginPage:
    def __init__(self, app: toga.App):
        self.app = app

    def getContent(self) -> toga.Box:

        main_container = toga.Box(style=Pack(direction=COLUMN))

        header_box = toga.Box(style=Pack(direction = COLUMN, padding=20))
        main_box = toga.Box(style=Pack(direction = COLUMN, padding=20))

        # title label
        title_label = toga.Label("Health App", style=Pack(font_size=20, padding=(20)))
        header_box.add(title_label)

        # entry inputs
        self.username_entry = toga.TextInput("username", placeholder="Username", style=Pack(padding=(10, 5)), validators=[MinLength(USERNAME_REQUIREMENTS["min_length"], allow_empty=False)])
        self.password_entry = toga.PasswordInput("password", placeholder="Password", style=Pack(padding=(0, 5)), validators=[MinLength(PASSWORD_REQUIREMENTS["min_length"], allow_empty=False)])

        # login button.
        login_button = toga.Button('Login', on_press=self.loginButtonHandler, style=Pack(padding=20))

        # add components to the main box.
        main_box.add(self.username_entry)
        main_box.add(self.password_entry)
        main_box.add(login_button)

        # add all boxes to container.
        main_container.add(header_box)
        main_container.add(main_box)

        return main_container
    
    def loginButtonHandler(self, _) -> None:
        if not self.username_entry.is_valid or not self.password_entry.is_valid:
            self.app.main_window.error_dialog("Error!", "Unable to login,\nPlease check details and try again.")
            return

        data = self.app.paths.data.joinpath(LOGIN_FILE).resolve().read_bytes()
        data = data.decode("utf-8").splitlines()

        username = sha512(self.username_entry.value.encode()).hexdigest()
        password = sha512(self.password_entry.value.encode()).hexdigest()

        if username != data[0] or password != data[1]:
            self.app.main_window.error_dialog("Error!", "Unable to login, please check details and try again.")
            return

        # TODO: Load user information from file.
        self.app.login_handler(User("First Name", "Last Name", "username", 1))


class _SignupPage:
    def __init__(self, app: toga.App):
        self.app = app
    
    def getContent(self) -> toga.Box:

        main_container = toga.Box(style=Pack(direction=COLUMN))

        header_box = toga.Box(style=Pack(direction = COLUMN, padding=20))
        main_box = toga.Box(style=Pack(direction = COLUMN, padding=20))

        # title label
        title_label = toga.Label("Health App", style=Pack(font_size=20, padding=(20)))
        header_box.add(title_label)

        # entry inputs
        self.fname_entry = toga.TextInput("first_name", placeholder="First Name", style=Pack(padding=(0, 15, 0)), validators=[MinLength(2, allow_empty=False)])
        self.lname_entry = toga.TextInput("last_name", placeholder="Last Name", style=Pack(padding=(10, 15, 0)), validators=[MinLength(2, allow_empty=False)])
        self.sex_entry = toga.Selection("sex", items=["Male", "Female"], style=Pack(padding=(10, 15, 0)))

        self.username_entry = toga.TextInput("username", placeholder="Username", style=Pack(padding=(20, 15, 0)), validators=[self._validUsername])
        self.password_entry = toga.PasswordInput("password", placeholder="Password", style=Pack(padding=(10, 15, 0)), validators=[self._validPassword])
        self.cpassword_entry = toga.PasswordInput("cpassword", placeholder="Confirm Password", style=Pack(padding=(10, 15, 0)), validators=[self._validPassword, self._checkConfirm])

        # register button.
        register_button = toga.Button('Register', on_press=self.registerButtonHandler, style=Pack(padding=(25, 15, 0)))

        # add components to the main box.
        main_box.add(self.fname_entry)
        main_box.add(self.lname_entry)
        main_box.add(self.sex_entry)
        main_box.add(self.username_entry)
        main_box.add(self.password_entry)
        main_box.add(self.cpassword_entry)
        main_box.add(register_button)

        # add all boxes to container.
        main_container.add(header_box)
        main_container.add(main_box)

        return main_container
    
    def registerButtonHandler(self, widget) -> None:
        # Its possible for password matching to lose sync.
        self.cpassword_entry._validate()
        if not self.username_entry.is_valid or not self.password_entry.is_valid or not self.cpassword_entry.is_valid:
            self.app.main_window.error_dialog("Error!", "Unable to register, please check information.")
            return

        # TODO Save user details such as first name etc.

        # Save login information (hash secured)
        username = sha512(self.username_entry.value.encode()).hexdigest()
        password = sha512(self.password_entry.value.encode()).hexdigest()
        self.app.paths.data.joinpath(LOGIN_FILE).resolve().write_bytes((username + "\n" + password).encode("utf-8"))

        self.app.login_handler(User(self.fname_entry.value, self.lname_entry.value, self.username_entry.value, 1 if self.sex_entry.value == "Male" else 0))

    def _checkConfirm(self, password: str):
        if password != self.password_entry.value:
            return "Passwords do not match"

        return None

    def _validUsername(self, username: str):
        spaces = sum(c.isspace() for c in username)

        if not USERNAME_REQUIREMENTS["spaces_allowed"] and spaces > 0:
            # Spaces found!
            return "Spaces are not allowed!"

        if len(username) > USERNAME_REQUIREMENTS["max_length"]:
            # Too long!
            return "Username too long, maximum length is " + str(USERNAME_REQUIREMENTS["max_length"])

        if len(username) < USERNAME_REQUIREMENTS["min_length"]:
            # Too small!
            return "Username is not long enough, minimum length is " + str(USERNAME_REQUIREMENTS["min_length"])

        return None

    def _validPassword(self, password: str):
        numbers = sum(c.isdigit() for c in password)
        letters = sum(c.isalpha() for c in password)
        spaces  = sum(c.isspace() for c in password)

        if not PASSWORD_REQUIREMENTS["spaces_allowed"] and spaces > 0:
            # Spaces found!
            return "Spaces are not allowed!"

        if len(password) > PASSWORD_REQUIREMENTS["max_length"]:
            # Too long!
            return "Password too long, maximum length is " + str(PASSWORD_REQUIREMENTS["max_length"])

        if len(password) < PASSWORD_REQUIREMENTS["min_length"]:
            # Too small!
            return "Password is not long enough, minimum length is " + str(PASSWORD_REQUIREMENTS["min_length"])

        if PASSWORD_REQUIREMENTS["numbers_required"] != 0 and numbers < PASSWORD_REQUIREMENTS["numbers_required"]:
            # Not enough numbers.
            return "Password does not contain enough numbers, minimum amount is " + str(PASSWORD_REQUIREMENTS["numbers_required"])

        if PASSWORD_REQUIREMENTS["special_required"] != 0 and len(password)-(numbers + letters + spaces) < PASSWORD_REQUIREMENTS["special_required"]:
            # Not enough special.
            return "Password does not contain enough special characters, minimum amount is " + str(PASSWORD_REQUIREMENTS["special_required"])

        return None
