#-------------------------------------------------------------------------------------------------------#
import time
import toga
import numpy as np
from toga.style import Pack
from toga.style.pack import COLUMN
from PIL import Image, ImageDraw

from healthapp.style import create_border
from healthapp.app import HealthApp
#-------------------------------------------------------------------------------------------------------#

# Confidence score for pose detection, 1 = 100% confidence, 0 = 0% confidence
SCORE = 0.5
PHOTO_FILE = "picture.png"
RESULTS_FILE = "pose-results.png"

MODEL_OPTION = "thunder"  # thunder or lightning (thunder is bigger, slightly slower but more accurate & lightning is smaller, faster but less accurate)

class AnalysePose():
    def __init__(self, app: HealthApp):
        print("Analyse Gait page loaded!")
        self.app = app 
        self.app.update_content(self.get_content())

    def get_content(self) -> toga.Box:
        content = toga.Box(style=Pack(direction=COLUMN, background_color="#e0965e"))

        header_box = toga.Box(style=Pack(direction=COLUMN, padding=(20, 20, 0)))
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=(2, 2), background_color="#fbf5cc"))
        main_black_box = toga.Box(style=Pack(direction=COLUMN, padding=(0, 18, 18), background_color="black"))
        footer_box = toga.Box(style=Pack(padding=20))

        if (self.app.paths.data / RESULTS_FILE).exists():
            self.image = toga.ImageView(str(self.app.paths.data / RESULTS_FILE), style=Pack(width=256, height=256, direction=COLUMN, padding=20))
        elif (self.app.paths.data / PHOTO_FILE).exists():
            img = Image.open(str(self.app.paths.data / PHOTO_FILE))
            img = _add_image_border(img)
            self.image = toga.ImageView(img, style=Pack(width=256, height=256, direction=COLUMN, padding=20))
            img.close()
        else:
            img = Image.new("RGB", (256, 256), (255, 0, 0))
            ImageDraw.Draw(img).text((10, 10), "No image found\nPress button to take a picture", fill=(255, 255, 255))
            self.image = toga.ImageView(img, style=Pack(width=256, height=256, direction=COLUMN, padding=20))
            img.close()

        # button for pose analysis
        analyse_gait_button = toga.Button('Analyse Pose', on_press=self.analyse_pose_handler, style=Pack(background_color="#fbf5cc"))
        analyse_gait_box = create_border(analyse_gait_button, inner_color="#fbf5cc")

        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(background_color="#fbf5cc"))
        back_box = create_border(back_button, inner_color="#fbf5cc")

        header_box.add(toga.Label("Pose Analysis", style=Pack(font_size=20, padding=(5, 10))))
        main_box.add(self.image)
        main_box.add(analyse_gait_box)
        main_box.add(toga.Label("")) # Creates a space in background colour. ("Spacer")      
        main_black_box.add(main_box)
        footer_box.add(back_box)

        for box in [header_box, main_black_box, footer_box]:
            content.add(box)

        return content

    async def analyse_pose_handler(self, widget):
        print("Analyse Pose button pressed!")

        if await self.app.camera.request_permission():
            photo = await self.app.camera.take_photo()
            if photo is None:
                return
            file = str(self.app.paths.data) + "/picture.png"
            photo.save(file)
            img = Image.open(str(self.app.paths.data / PHOTO_FILE))
            img = _add_image_border(img)
            self.image.image = img
            img.close()
            print("starting pose analysis on file - " + str(file))
            if self.run_analysis(file) == True:
                self.app.main_window.info_dialog("Success!", "Pose analysis complete!")
                self.image.image = str(self.app.paths.data / RESULTS_FILE)
            else:
                self.app.main_window.info_dialog("Error", "Pose analysis failed!")
        else:
            self.app.main_window.info_dialog("Oh no!", "You have not granted permission to take photos")

    def back_handler(self, widget):
        print("Back button pressed!")
        self.app.show_menu()

    def run_analysis(self, file):
        import tflite_runtime.interpreter as tflite

        model_file = str((self.app.paths.app / f"resources/machine_learning/singlepose-{MODEL_OPTION}-tflite-float16-v4.tflite"))

        print(f"Running pose analysis model '{model_file}' on file '{file}'")
        
        interpreter = tflite.Interpreter(model_path=model_file)
        interpreter.allocate_tensors()

        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()

        # NxHxWxC, H:1, W:2
        height = input_details[0]['shape'][1]
        width = input_details[0]['shape'][2]
        img = Image.open(file)
        img = _add_image_border(img).resize((width, height))

        # add N dim
        input_data = np.expand_dims(img, axis=0)

        interpreter.set_tensor(input_details[0]['index'], input_data)

        start_time = time.time()
        interpreter.invoke()
        stop_time = time.time()

        output_data = interpreter.get_tensor(output_details[0]['index'])

        results = np.squeeze(output_data) # opposite of expand_dims
        # 17 rows, [x, y, confidence score] (all 0.0-1.0)
        # [nose, left eye, right eye, left ear, right ear, left shoulder, right shoulder, left elbow,
        # right elbow, left wrist, right wrist, left hip, right hip, left knee, right knee, left ankle, right ankle]
        # NOTE, The graphics interface uses the same coordinate system as PIL itself, with (0, 0) in the upper left corner.

        data = {
            "nose": results[0],
            "left_eye": results[1],
            "right_eye": results[2],
            "left_ear": results[3],
            "right_ear": results[4],
            "left_shoulder": results[5],
            "right_shoulder": results[6],
            "left_elbow": results[7],
            "right_elbow": results[8],
            "left_wrist": results[9],
            "right_wrist": results[10],
            "left_hip": results[11],
            "right_hip": results[12],
            "left_knee": results[13],
            "right_knee": results[14],
            "left_ankle": results[15],
            "right_ankle": results[16]
        }

        # TODO: save data to user?

        draw = ImageDraw.Draw(img)
        for [y, x, confidence] in results:  # yes the results are y,x not x,y coordinates.
            print(f"Position ({x*width}, {y*height}) - Confidence ({confidence}/1)")
            if confidence > SCORE:
                # draw 2x2 red pixel square at each point if confidence > SCORE
                draw.rounded_rectangle((((x*width)-1, (y*height)-1), ((x*width)+1, (y*height)+1)), fill=(255, 0, 0), width=2)

        img.save(str(self.app.paths.data / RESULTS_FILE), "PNG")
        img.close()

        print('Time taken to analyse pose: {:.3f}ms'.format((stop_time - start_time) * 1000))

        return True


def _add_image_border(image, background_color=(0,0,0)):
    width, height = image.size
    if width == height:
        return image
    elif width > height:
        result = Image.new(image.mode, (width, width), background_color)
        result.paste(image, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(image.mode, (height, height), background_color)
        result.paste(image, ((height - width) // 2, 0))
        return result