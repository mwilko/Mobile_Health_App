#-------------------------------------------------------------------------------------------------------#
import asyncio
import time
import toga
import numpy as np
import warnings
from toga.style import Pack
from toga.style.pack import COLUMN
from PIL import Image, ImageDraw
from pathlib import Path

from healthapp.style import create_border
from healthapp.app import HealthApp
from healthapp.config import POSE_DETECTION_TYPE, POSE_PHOTO_RESULTS_FILE, POSE_VIDEO_RESULTS_FILE
from healthapp.config import POSE_DETECTION_CONFIDENCE as SCORE
#-------------------------------------------------------------------------------------------------------#
# Raw android imports for interacting directly with the camera (IDE probably wont know about these dont worry)
from android.content import Intent # type: ignore
from android.content.pm import PackageManager # type: ignore
from android.provider import MediaStore # type: ignore
from androidx.core.content import FileProvider # type: ignore
from java.io import File # type: ignore
from java import jarray, jbyte # type: ignore
#-------------------------------------------------------------------------------------------------------#


class AnalysePose():
    def __init__(self, app: HealthApp):
        self.app = app 
        self.app.update_content(self.get_content())
        self.image_path = None
        self.video_path = None

    def get_loading_content(self) -> toga.Box:
        content = toga.Box(style=Pack(direction=COLUMN, background_color="#e0965e"))
        header_box = toga.Box(style=Pack(direction=COLUMN, padding=(20, 20, 0)))
        footer_box = toga.Box(style=Pack(padding=5))
        text = toga.Label("Analyzing pose, please wait.", style=Pack(font_size=20, padding=(5, 10)))
        header_box.add(text)
        bar = toga.ProgressBar(style=Pack(padding=10, width=self.app.main_window.size[0]-30), running=True, max=None)
        footer_box.add(bar)
        for box in [header_box, footer_box]:
            content.add(box)
        return content

    def get_content(self) -> toga.Box:
        content = toga.Box(style=Pack(direction=COLUMN, background_color="#e0965e"))

        header_box = toga.Box(style=Pack(direction=COLUMN, padding=(20, 20, 0)))
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=(2, 2), background_color="#fbf5cc"))
        main_black_box = toga.Box(style=Pack(direction=COLUMN, padding=(0, 18, 18), background_color="black"))
        footer_box = toga.Box(style=Pack(padding=5))

        if (self.app.paths.data / POSE_PHOTO_RESULTS_FILE).exists():
            self.image = toga.ImageView(str(self.app.paths.data / POSE_PHOTO_RESULTS_FILE), style=Pack(width=256, height=256, direction=COLUMN, padding=20))
        else:
            img = Image.new("RGB", (256, 256), (255, 0, 0))
            ImageDraw.Draw(img).text((10, 10), "No image found\nPress button to take a picture", fill=(255, 255, 255))
            self.image = toga.ImageView(img, style=Pack(width=256, height=256, direction=COLUMN, padding=20))
            img.close()

        # button for pose analysis
        analyse_gait_button = toga.Button('Analyse Pose - Picture', on_press=self.analyse_pose_handler, style=Pack(background_color="#fbf5cc", padding=(-3)))
        analyse_gait_box = create_border(analyse_gait_button, inner_color="#fbf5cc")

        analyse_gait_2_button = toga.Button('Analyse Pose - Picture (gallery)', on_press=self.analyse_pose_handler_2, style=Pack(background_color="#fbf5cc", padding=(-3)))
        analyse_gait_2_box = create_border(analyse_gait_2_button, inner_color="#fbf5cc")

        analyse_gait_3_button = toga.Button('Analyse Pose - Video', on_press=self.analyse_pose_handler_3, style=Pack(background_color="#fbf5cc", padding=(-3)))
        analyse_gait_3_box = create_border(analyse_gait_3_button, inner_color="#fbf5cc")

        analyse_gait_4_button = toga.Button('Analyse Pose - Video (gallery)', on_press=self.analyse_pose_handler_4, style=Pack(background_color="#fbf5cc", padding=(-3)))
        analyse_gait_4_box = create_border(analyse_gait_4_button, inner_color="#fbf5cc")

        back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(background_color="#fbf5cc", padding=(-3)))
        back_box = create_border(back_button, inner_color="#fbf5cc")

        header_box.add(toga.Label("Pose Analysis", style=Pack(font_size=20, padding=(5, 10))))
        main_box.add(self.image)
        main_box.add(analyse_gait_box)
        main_box.add(analyse_gait_2_box)
        main_box.add(analyse_gait_3_box)
        main_box.add(analyse_gait_4_box)
        main_box.add(toga.Label("")) # Creates a space in background colour. ("Spacer")      
        main_black_box.add(main_box)
        footer_box.add(back_box)

        for box in [header_box, main_black_box, footer_box]:
            content.add(box)

        return content

    async def analyse_pose_handler(self, widget):
        if await self.app.camera.request_permission():
            photo = await self.app.camera.take_photo()
            if photo is None:
                return
            file = str(self.app.paths.data) + "/picture.png"
            photo.save(file)
            
            print("starting pose analysis on file - " + str(file))
            self.image_path = file
            self.app.update_content(self.get_loading_content())
            self.app.add_background_task(self.run_image_analysis)
        else:
            self.app.main_window.info_dialog("Oh no!", "You have not granted permission to use the camera!")
    
    async def analyse_pose_handler_2(self, widget):
        def run(pic_path):
            if(pic_path is None):
                return
            else:
                print("starting pose analysis on image file - " + str(pic_path))
                self.image_path = pic_path
                self.app.update_content(self.get_loading_content())
                self.app.add_background_task(self.run_image_analysis)
        self.choose_picture(lambda pic_path: run(pic_path))
        
    async def analyse_pose_handler_3(self, widget):
        if await self.app.camera.request_permission():
            def run(video_path):
                if(video_path is None):
                    return
                else:
                    print("starting pose analysis on video file - " + str(video_path))
                    self.video_path = video_path
                    self.app.update_content(self.get_loading_content())
                    self.app.add_background_task(self.run_video_analysis)
            self.take_video(lambda video_path: run(video_path))
        else:
            self.app.main_window.info_dialog("Oh no!", "You have not granted permission to use the camera!")
    
    async def analyse_pose_handler_4(self, widget):
        def run(video_path):
            if(video_path is None):
                return
            else:
                print("starting pose analysis on video file - " + str(video_path))
                self.video_path = video_path
                self.app.update_content(self.get_loading_content())
                self.app.add_background_task(self.run_video_analysis)
        self.choose_video(lambda video_path: run(video_path))

    def back_handler(self, widget):
        self.app.show_menu()
    
    async def run_video_analysis(self, app, **kwargs):
        time_start = time.time()
        file = self.video_path
        import cv2
        images = []
        vidcap = cv2.VideoCapture(str(file))
        success,image = vidcap.read()
        count = 0
        while success:
            cv2.imwrite(str(self.app.paths.data / ("frame%d.jpg" % count)), image)     # save frame as JPEG file      
            self.run_analysis(str(self.app.paths.data / ("frame%d.jpg" % count)), "frame%d-results.jpg" % count)
            images.append(Image.open(str(self.app.paths.data / ("frame%d-results.jpg" % count))))
            success,image = vidcap.read()
            await asyncio.sleep(0.1)
            count += 1
        #compress to gif?
        self.run_analysis(str(self.app.paths.data / ("frame%d.jpg" % (count - 2))))
        self.image.image = str(self.app.paths.data / POSE_PHOTO_RESULTS_FILE)
        time_end = time.time()
        print('Time taken to analyse whole video pose: {:.3f}s'.format(time_end - time_start))

        images[0].save(str(self.app.paths.data / POSE_VIDEO_RESULTS_FILE),
               save_all=True, append_images=images[1:], optimize=False, duration=33, loop=0)

        for image in images:
            image.close()
        
        #delete all the frame images
        for i in range(count):
            Path(str(self.app.paths.data / ("frame%d.jpg" % i))).unlink()
            Path(str(self.app.paths.data / ("frame%d-results.jpg" % i))).unlink()

        self.app.main_window.info_dialog("Success!", "Pose analysis complete!\nResults saved as '" + POSE_VIDEO_RESULTS_FILE + "' in the data folder.")
        self.app.update_content(self.get_content())
        return True
    
    async def run_image_analysis(self, app, **kwargs):
        file = self.image_path
        self.run_analysis(file)
        self.image.image = str(self.app.paths.data / POSE_PHOTO_RESULTS_FILE)

        self.app.main_window.info_dialog("Success!", "Pose analysis complete!\nResults saved as '" + POSE_PHOTO_RESULTS_FILE + "' in the data folder.")
        self.app.update_content(self.get_content())
        return True

    def run_analysis(self, file, output_file=POSE_PHOTO_RESULTS_FILE):
        import tflite_runtime.interpreter as tflite

        model_file = str((self.app.paths.app / f"resources/machine_learning/singlepose-{POSE_DETECTION_TYPE}-tflite-float16-v4.tflite"))

        #print(f"Running pose analysis model '{model_file}' on file '{file}'")
        
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

        interpreter.invoke()

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

        draw = ImageDraw.Draw(img)
        for [y, x, confidence] in results:  # yes the results are y,x not x,y coordinates.
            #print(f"Position ({x*width}, {y*height}) - Confidence ({confidence}/1)")
            if confidence > SCORE:
                # draw 2x2 red pixel square at each point if confidence > SCORE
                draw.rounded_rectangle((((x*width)-1, (y*height)-1), ((x*width)+1, (y*height)+1)), fill=(255, 0, 0), width=2)

        img.save(str(self.app.paths.data / output_file), "PNG")
        img.close()

        return True
    
    def choose_picture(self, callable):
        context = self.app._impl.native.getApplicationContext()

        shared_folder = File(context.getCacheDir(), "shared")
        if not shared_folder.exists():
            shared_folder.mkdirs()

        # Create a temporary file in the shared folder,
        # and convert it to a URI using the app's fileprovider.
        jpg_file = File.createTempFile("camera_", ".jpg", shared_folder)
        jpg_uri = FileProvider.getUriForFile(
            context,
            f"{self.app.app_id}.fileprovider",
            jpg_file,
        )

        def file_chosen(code, data):
            # Completed == -1
            if code == -1:
                stream = context.getContentResolver().openInputStream(data.getData())
                def read_stream(stream):
                    block = jarray(jbyte)(1024 * 1024)
                    blocks = []
                    while True:
                        bytes_read = stream.read(block)
                        if bytes_read == -1:
                            return b"".join(blocks)
                        else:
                            blocks.append(bytes(block)[:bytes_read])
                data = read_stream(stream)
                stream.close()
                
                jpg_stream = context.getContentResolver().openOutputStream(jpg_uri)
                jpg_stream.write(data)
                jpg_stream.flush()
                jpg_stream.close()
                stream.close()

                callable(Path(jpg_file.getAbsolutePath()))
            else:
                callable(None)

        intent = Intent(MediaStore.ACTION_PICK_IMAGES)
        intent.setTypeAndNormalize("image/*") #Takes a MIME type to filter the users choices
        self.app._impl.start_activity(intent, on_complete=file_chosen)
    
    def choose_video(self, callable):
        context = self.app._impl.native.getApplicationContext()

        shared_folder = File(context.getCacheDir(), "shared")
        if not shared_folder.exists():
            shared_folder.mkdirs()

        # Create a temporary file in the shared folder,
        # and convert it to a URI using the app's fileprovider.
        mp4_file = File.createTempFile("camera_video_", ".mp4", shared_folder)
        mp4_uri = FileProvider.getUriForFile(
            context,
            f"{self.app.app_id}.fileprovider",
            mp4_file,
        )

        def file_chosen(code, data):
            # Completed == -1
            if code == -1:
                stream = context.getContentResolver().openInputStream(data.getData())
                def read_stream(stream):
                    block = jarray(jbyte)(1024 * 1024)
                    blocks = []
                    while True:
                        bytes_read = stream.read(block)
                        if bytes_read == -1:
                            return b"".join(blocks)
                        else:
                            blocks.append(bytes(block)[:bytes_read])
                data = read_stream(stream)
                stream.close()
                
                mp4_stream = context.getContentResolver().openOutputStream(mp4_uri)
                mp4_stream.write(data)
                mp4_stream.flush()
                mp4_stream.close()
                stream.close()

                callable(Path(mp4_file.getAbsolutePath()))
            else:
                callable(None)

        intent = Intent(MediaStore.ACTION_PICK_IMAGES)
        intent.setTypeAndNormalize("video/*") #Takes a MIME type to filter the users choices
        self.app._impl.start_activity(intent, on_complete=file_chosen)
    
    def take_video(self, callable):
        context = self.app._impl.native.getApplicationContext()
        has_camera = context.getPackageManager().hasSystemFeature(
            PackageManager.FEATURE_CAMERA
        )

        if not has_camera:
            warnings.warn("No camera is available")
            callable(None)
            return

        shared_folder = File(context.getCacheDir(), "shared")
        if not shared_folder.exists():
            shared_folder.mkdirs()

        # Create a temporary file in the shared folder,
        # and convert it to a URI using the app's fileprovider.
        mp4_file = File.createTempFile("camera_video_", ".mp4", shared_folder)
        mp4_uri = FileProvider.getUriForFile(
            context,
            f"{self.app.app_id}.fileprovider",
            mp4_file,
        )

        def video_taken(code, data):
            # Completed == 0
            if code == 0:
                callable(Path(mp4_file.getAbsolutePath()))
            else:
                callable(None)

        intent = Intent(MediaStore.ACTION_VIDEO_CAPTURE)
        #intent.putExtra(MediaStore.EXTRA_DURATION_LIMIT, 10) # 10 seconds (doesnt work?)
        intent.putExtra(MediaStore.EXTRA_VIDEO_QUALITY, 0) # 0 = low quality, 1 = high quality
        intent.putExtra(MediaStore.EXTRA_OUTPUT, mp4_uri)
        self.app._impl.start_activity(intent, on_complete=video_taken)


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