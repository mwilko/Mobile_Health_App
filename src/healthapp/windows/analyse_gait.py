#-------------------------------------------------------------------------------------------------------#
import time
import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from healthapp.style import create_border
from healthapp.app import HealthApp
#-------------------------------------------------------------------------------------------------------#

class AnalyseGait():
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
    
        # button for gait analysis
        analyse_gait_button = toga.Button('Analyse Gait', on_press=self.analyse_gait_handler, style=Pack(background_color="#fbf5cc"))
        analyse_gait_box = create_border(analyse_gait_button, inner_color="#fbf5cc")

        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(background_color="#fbf5cc"))
        back_box = create_border(back_button, inner_color="#fbf5cc")

        header_box.add(toga.Label("Analyse Gait", style=Pack(font_size=20, padding=(5, 10))))
        main_box.add(analyse_gait_box)
        main_box.add(toga.Label("")) # Creates a space in background colour. ("Spacer")      
        main_black_box.add(main_box)
        footer_box.add(back_box)

        for box in [header_box, main_black_box, footer_box]:
            content.add(box)

        return content

    async def analyse_gait_handler(self, widget):
        print("Analyse Gait button pressed!")

        # to just test ML
        #file = str(self.app.paths.data) + "/picture.png"
        #print("starting tf - " + str(file))
        #import threading
        #threading.Thread(None, self.RUN_TEST, "tf-thread", [str(file)]).start()
        #return

        # Note this doesnt return on iOS/macOS yet, fully working on android.
        if await self.app.camera.request_permission():
            photo = await self.app.camera.take_photo()
            if photo is None:
                # User cancelled.
                return
            file = str(self.app.paths.data) + "/picture.png"
            photo.save(file)
            print("starting tf - " + str(file))
            import threading
            threading.Thread(None, self.RUN_TEST, "tf-thread", [str(file)]).start()
            #self.RUN_TEST(file)
            self.app.main_window.info_dialog("Success!", "Photo has been saved to: " + file)
        else:
            self.app.main_window.info_dialog("Oh no!", "You have not granted permission to take photos")

    def back_handler(self, widget):
        print("Back button pressed!")
        self.app.show_menu()

    # Only run from inside sub-thread.
    def RUN_TEST(self, file):
        import tflite_runtime.interpreter as tflite
        import numpy as np
        from PIL import Image

        #print(file)
        #print(str((self.app.paths.app / "resources/machine_learning/singlepose-thunder-tflite-float16-v4.tflite")))
        
        interpreter = tflite.Interpreter(model_path=str((self.app.paths.app / "resources/machine_learning/singlepose-thunder-tflite-float16-v4.tflite")))
        interpreter.allocate_tensors()

        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()


        # check the type of the input tensor
        floating_model = input_details[0]['dtype'] == np.float32

        # NxHxWxC, H:1, W:2
        height = input_details[0]['shape'][1]
        width = input_details[0]['shape'][2]
        img = Image.open(file).resize((width, height))

        # add N dim
        input_data = np.expand_dims(img, axis=0)

        input_mean = 127.5
        input_std = 127.5

        if floating_model:
            input_data = (np.float32(input_data) - input_mean) / input_std

        interpreter.set_tensor(input_details[0]['index'], input_data)

        start_time = time.time()
        interpreter.invoke()
        stop_time = time.time()

        output_data = interpreter.get_tensor(output_details[0]['index'])

        results = np.squeeze(output_data)
        #print(results)
        for [y,x,score] in results:
            print(f"Position ({x*256}, {y*256}) - Confidence ({score}/1)")
        # 17 rows, [x, y, confidence score] (all 0.0-1.0)
        # [nose, left eye, right eye, left ear, right ear, left shoulder, right shoulder, left elbow,
        # right elbow, left wrist, right wrist, left hip, right hip, left knee, right knee, left ankle, right ankle]

        print('time: {:.3f}ms'.format((stop_time - start_time) * 1000))

        exit(0)
        pass
