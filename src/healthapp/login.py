import toga
from toga.style import Pack
from toga.style.pack import COLUMN

LOGIN_FILE = "secure_login"


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
        print("init - signup")

def getAuthPage(app: toga.App):
    return _LoginPage(app)
    # If the user login file exists, we need to login not signup.
    if app.paths.data.joinpath(LOGIN_FILE).resolve().exists():
        return _SignupPage(app)
    else:
        return _LoginPage(app)
