import toga
from toga.style import Pack
from toga.style.pack import COLUMN

LOGIN_FILE = "secure_auth"


class _LoginPage:
    def __init__(self, app: toga.App):
        self.app = app

    def getContent(self) -> toga.Box:

        main_container = toga.Box(style=Pack(direction=COLUMN))

        header_box = toga.Box(style=Pack(direction = COLUMN, padding=20))
        main_box = toga.Box(style=Pack(direction = COLUMN, padding=20))

        # title label
        title_label = toga.Label("Health Application", style=Pack(font_size=20, padding=(20)))
        header_box.add(title_label)

        # entry inputs
        username_entry = toga.TextInput("username", placeholder="Username", style=Pack(padding=(10, 5)))
        password_entry = toga.PasswordInput("password", placeholder="Password", style=Pack(padding=(0, 5)))

        # login button.
        login_button = toga.Button('Login', on_press=self.loginButtonHandler, style=Pack(padding=20))

        # add components to the main box.
        main_box.add(username_entry)
        main_box.add(password_entry)
        main_box.add(login_button)

        # add all boxes to container.
        main_container.add(header_box)
        main_container.add(main_box)

        return main_container
    
    def loginButtonHandler(self, widget) -> None:
        print("login button pressed")
        self.app.login_handler(["real name", "username"])


class _SignupPage:
    def __init__(self, app: toga.App):
        self.app = app
    
    def getContent(self) -> toga.Box:

        main_container = toga.Box(style=Pack(direction=COLUMN))

        header_box = toga.Box(style=Pack(direction = COLUMN, padding=20))
        main_box = toga.Box(style=Pack(direction = COLUMN, padding=20))

        # title label
        title_label = toga.Label("Health Application", style=Pack(font_size=20, padding=(20)))
        header_box.add(title_label)

        # entry inputs
        fname_entry = toga.TextInput("first_name", placeholder="First Name", style=Pack(padding=(0, 15, 0)))
        lname_entry = toga.TextInput("last_name", placeholder="Last Name", style=Pack(padding=(10, 15, 0)))

        username_entry = toga.TextInput("username", placeholder="Username", style=Pack(padding=(20, 15, 0)))
        password_entry = toga.PasswordInput("password", placeholder="Password", style=Pack(padding=(10, 15, 0)))
        cpassword_entry = toga.PasswordInput("cpassword", placeholder="Confirm Password", style=Pack(padding=(10, 15, 0)))

        # register button.
        register_button = toga.Button('Register', on_press=self.registerButtonHandler, style=Pack(padding=(25, 15, 0)))

        # add components to the main box.
        main_box.add(fname_entry)
        main_box.add(lname_entry)
        main_box.add(username_entry)
        main_box.add(password_entry)
        main_box.add(cpassword_entry)
        main_box.add(register_button)

        # add all boxes to container.
        main_container.add(header_box)
        main_container.add(main_box)

        return main_container
    
    def registerButtonHandler(self, widget) -> None:
        print("Register button pressed")
        self.app.login_handler(["real name", "username"])

def getAuthPage(app: toga.App):
    # If the user login file exists, we need to login not signup.
    if app.paths.data.joinpath(LOGIN_FILE).resolve().exists():
        return _LoginPage(app)
    else:
        return _SignupPage(app)
