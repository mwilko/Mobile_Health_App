#-------------------------------------------------------------------------------------------------------#
import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from toga.validators import MinLength
from hashlib import sha512

from healthapp.user import User
from healthapp.app import HealthApp
from healthapp.config import *

from healthapp.style import create_border
#-------------------------------------------------------------------------------------------------------#

def showAuthPage(app: HealthApp):
    # uncomment this to skip login:
    user = User(app)
    user.load()
    app.login_handler(user)
    return
    
    # If the user login file exists, we need to login not signup.
    if app.paths.data.joinpath(LOGIN_FILE).resolve().exists() and app.paths.data.joinpath(USER_DATA_FILE).resolve().exists():
        _LoginPage(app)
    else:
        _RegisterPage(app)


## -- Private classes / functions -- ##

class _LoginPage:
    def __init__(self, app: HealthApp):
        self.app = app
        self.app.update_content(self.get_content())

    def get_content(self) -> toga.Box:

        content = toga.Box(style=Pack(direction=COLUMN, background_color="#e0965e"))

        header_box = toga.Box(style=Pack(direction=COLUMN, padding=(20, 15)))
        
        main_black_box = toga.Box(style=Pack(direction=COLUMN, padding=(0, 18, 18), background_color="black"))
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=(2, 2), background_color="#fbf5cc"))

        # title label
        title_label = toga.Label("Health App", style=Pack(font_size=28, font_weight="bold", padding=(10, 5), color="black"))
        header_box.add(title_label)

        # entry inputs
        self.username_entry = toga.TextInput("username", placeholder="Username", style=Pack(background_color="#fbf5cc"), validators=[MinLength(USERNAME_REQUIREMENTS["min_length"], allow_empty=False)])
        username_box = create_border(self.username_entry, inner_color="#fbf5cc")
        
        self.password_entry = toga.PasswordInput("password", placeholder="Password", style=Pack(background_color="#fbf5cc"), validators=[MinLength(PASSWORD_REQUIREMENTS["min_length"], allow_empty=False)])
        password_box = create_border(self.password_entry, inner_color="#fbf5cc")

        # login button.
        login_button = toga.Button('Login', on_press=self.login_button_handler, style=Pack(padding=(-3), background_color="#fbf5cc"))
        login_box = create_border(login_button, inner_color="#fbf5cc", padding=(5, 20, 20))

        # add components to the main box.
        main_box.add(toga.Label(""))  # Creates a space in background color. ("Spacer")
        main_box.add(username_box)
        main_box.add(password_box)
        main_box.add(toga.Label(""))  # Creates a space in background color. ("Spacer")
        main_black_box.add(main_box)

        # add all boxes to the container.
        content.add(header_box)
        content.add(main_black_box)
        content.add(login_box)

        return content
    
    def login_button_handler(self, _) -> None:
        if not self.username_entry.is_valid or not self.password_entry.is_valid:
            self.app.main_window.error_dialog("Error!", "Unable to login,\nPlease check details and try again.")
            return

        data = self.app.paths.data.joinpath(LOGIN_FILE).resolve().read_bytes().decode("utf-8").splitlines()

        username = sha512(self.username_entry.value.encode()).hexdigest()
        password = sha512(self.password_entry.value.encode()).hexdigest()

        if username != data[0] or password != data[1]:
            self.app.main_window.error_dialog("Error!", "Unable to login, please check details and try again.")
            return

        # Load user information from file.
        user = User(self.app)
        user.load()
        self.app.login_handler(user)


class _RegisterPage:
    def __init__(self, app: HealthApp):
        self.app = app
        self.app.update_content(self.get_content())

    def get_content(self) -> toga.Box:
        main_container = toga.Box(style=Pack(direction=COLUMN, background_color="#e0965e"))

        header_box = toga.Box(style=Pack(direction=COLUMN, padding=(20, 15)))
        main_black_box = toga.Box(style=Pack(direction=COLUMN, padding=(0, 18, 18), background_color="black"))
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=(2, 2), background_color="#fbf5cc"))

        # title label
        title_label = toga.Label("Health App", style=Pack(font_size=28, font_weight="bold", padding=(10, 5), color="black"))
        header_box.add(title_label)

        # entry inputs, in a black box to make an illusion of border. (https://github.com/beeware/toga/issues/849)
        self.fname_entry = toga.TextInput("first_name", placeholder="First Name", style=Pack(background_color="#fbf5cc"), validators=[MinLength(2, allow_empty=False)])
        fname_box = create_border(self.fname_entry, inner_color="#fbf5cc")

        self.lname_entry = toga.TextInput("last_name", placeholder="Last Name", style=Pack(background_color="#fbf5cc"), validators=[MinLength(2, allow_empty=False)])
        lname_box = create_border(self.lname_entry, inner_color="#fbf5cc")

        self.sex_entry = toga.Selection("sex", items=["Male", "Female"])
        sex_box = create_border(self.sex_entry, inner_color="#fbf5cc")

        self.username_entry = toga.TextInput("username", placeholder="Username", style=Pack(background_color="#fbf5cc"), validators=[self._valid_username])
        username_box = create_border(self.username_entry, inner_color="#fbf5cc", padding=(30, 13, 0))

        self.password_entry = toga.PasswordInput("password", placeholder="Password", style=Pack(background_color="#fbf5cc"), validators=[self._valid_password])
        password_box = create_border(self.password_entry, inner_color="#fbf5cc")

        self.cpassword_entry = toga.PasswordInput("cpassword", placeholder="Confirm Password", style=Pack(background_color="#fbf5cc"), validators=[self._valid_password, self._check_confirm])
        cpassword_box = create_border(self.cpassword_entry, inner_color="#fbf5cc")

        # register button.
        register_button = toga.Button('Register', on_press=self.register_button_handler, style=Pack(padding=(-3), background_color="#fbf5cc"))
        register_box = create_border(register_button, inner_color="#fbf5cc", padding=(50, 20, 20))
        # add components to the main box.
        main_box.add(toga.Label(""))  # Creates a space in background color. ("Spacer")
        main_box.add(fname_box)
        main_box.add(lname_box)
        main_box.add(sex_box)
        main_box.add(username_box)
        main_box.add(password_box)
        main_box.add(cpassword_box)
        main_box.add(toga.Label(""))  # Spacer
        main_black_box.add(main_box)  # Outer black border.

        # add all boxes to the container.
        main_container.add(header_box)
        main_container.add(main_black_box)
        main_container.add(register_box)

        return main_container

    def register_button_handler(self, widget) -> None:
        # It's possible for password matching to lose sync.
        self.cpassword_entry._validate()
        if not self.username_entry.is_valid or not self.password_entry.is_valid or not self.cpassword_entry.is_valid:
            self.app.main_window.error_dialog("Error!", "Unable to register,\nPlease check information.")
            return

        # Save user details such as first name etc.
        user = User(self.app, self.fname_entry.value, self.lname_entry.value, self.username_entry.value, 1 if self.sex_entry.value == "Male" else 0)
        user.save()

        # Save login information (hash secured)
        username = sha512(self.username_entry.value.encode()).hexdigest()
        password = sha512(self.password_entry.value.encode()).hexdigest()
        self.app.paths.data.joinpath(LOGIN_FILE).resolve().write_bytes((username + "\n" + password).encode("utf-8"))

        self.app.login_handler(user)

    def _check_confirm(self, password: str):
        if password != self.password_entry.value:
            return "Passwords do not match"

        return None

    def _valid_username(self, username: str):
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

    def _valid_password(self, password: str):
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
