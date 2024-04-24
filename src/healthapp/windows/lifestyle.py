#-------------------------------------------------------------------------------------------------------#
import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from healthapp.style import create_border
from healthapp.app import HealthApp
#-------------------------------------------------------------------------------------------------------#
class Lifestyle():
   def __init__(self, app: HealthApp):
      self.app = app
      self.app.update_content(self.get_content())

   def get_content(self) -> toga.Box:
      content = toga.Box(style=Pack(direction=COLUMN, background_color="#e0965e"))
      # Create an instance of variable to store the user's selection
      self.exercise_selection = None
        

      # Main box for the initial content
      header_box = toga.Box(style=Pack(padding=20))
      main_box = toga.Box(style=Pack(direction = COLUMN, padding=(2, 2), background_color="#fbf5cc"))
      main_black_box = toga.Box(style=Pack(direction=COLUMN, padding=(0, 18, 18), background_color="black"))
      footer_box = toga.Box(style=Pack(padding=5))

      # label + button for behavioural analysis
      exercise_label = toga.Label("How much exercise do you get per week?", style=Pack(color='black', font_size=14, padding=(0, 5)))
        
      e60_button = toga.Button('Less than 60 mins', on_press=self.lifestyle_handler, style=Pack(color='black',background_color="#fbf5cc", padding=(-3)))
      e60_box = create_border(e60_button, inner_color="#fbf5cc")

      e60_119_button = toga.Button('60 - 119 mins', on_press=self.lifestyle_handler, style=Pack(color='black', background_color="#fbf5cc", padding=(-3)))
      e60_119_box = create_border(e60_119_button, inner_color="#fbf5cc")

      e120_180_button = toga.Button('120 - 180 mins', on_press=self.lifestyle_handler, style=Pack(color='black', background_color="#fbf5cc", padding=(-3)))
      e120_180_box = create_border(e120_180_button, inner_color="#fbf5cc")

      e180_plus_button = toga.Button('More than 180 mins', on_press=self.lifestyle_handler, style=Pack(color='black', background_color="#fbf5cc", padding=(-3)))
      e180_plus_box = create_border(e180_plus_button, inner_color="#fbf5cc")

      back_button = toga.Button('Back', on_press=self.back_handler, style=Pack(color='black', background_color="#fbf5cc", padding=(-3)))
      back_box = create_border(back_button, inner_color="#fbf5cc")
        
      # label + button for high blood pressure
      highbp_label = toga.Label("Do you have a high blood pressure?", style=Pack(color='black', font_size=15, padding=(0, 5)))
        
      yesbp_button = toga.Button('Yes', on_press=self.highbp_handler, style=Pack(color='black', background_color="#fbf5cc", padding=(-3)))
      yesbp_box = create_border(yesbp_button, inner_color="#fbf5cc")
        
      nobp_button = toga.Button('No', on_press=self.highbp_handler, style=Pack(color='black', background_color="#fbf5cc", padding=(-3)))
      nobp_box = create_border(nobp_button, inner_color="#fbf5cc")
        
      # label + button for high cholesterol
      highcol_label = toga.Label("Do you have a high cholesterol?", style=Pack(color='black', font_size=15, padding=(0, 5)))
        
      yescol_button = toga.Button('Yes', on_press=self.highcol_handler, style=Pack(color='black', background_color="#fbf5cc", padding=(-3)))
      yescol_box = create_border(yescol_button, inner_color="#fbf5cc")
        
      nocol_button = toga.Button('No', on_press=self.highcol_handler, style=Pack(color='black', background_color="#fbf5cc", padding=(-3)))
      nocol_box = create_border(nocol_button, inner_color="#fbf5cc")
        
      # label + button for smoking
      smoker_label = toga.Label("Do you smoke?", style=Pack(color='black', font_size=15, padding=(0, 5)))
        
      yessmoke_button = toga.Button('Yes', on_press=self.smoker_handler, style=Pack(color='black', background_color="#fbf5cc", padding=(-3)))
      yessmoke_box = create_border(yessmoke_button, inner_color="#fbf5cc")
        
      nosmoke_button = toga.Button('No', on_press=self.smoker_handler, style=Pack(color='black', background_color="#fbf5cc", padding=(-3)))
      nosmoke_box = create_border(nosmoke_button, inner_color="#fbf5cc")
        
      # label + button for stroke
      stroke_label = toga.Label("Have you had a stroke?", style=Pack(color='black', font_size=15, padding=(0, 5)))
        
      yesstroke_button = toga.Button('Yes', on_press=self.stroke_handler, style=Pack(color='black', background_color="#fbf5cc", padding=(-3)))
      yesstroke_box = create_border(yesstroke_button, inner_color="#fbf5cc")
        
      nostroke_button = toga.Button('No', on_press=self.smoker_handler, style=Pack(color='black', background_color="#fbf5cc", padding=(-3)))
      nostroke_box = create_border(nostroke_button, inner_color="#fbf5cc")  
        
      # label + button for diabetes
      diabetes_label = toga.Label("Have you had a stroke?", style=Pack(color='black', font_size=15, padding=(0, 5)))
        
      yesdiabetes_button = toga.Button('Yes', on_press=self.stroke_handler, style=Pack(color='black', background_color="#fbf5cc", padding=(-3)))
      yesdiabetes_box = create_border(yesdiabetes_button, inner_color="#fbf5cc")
        
      nodiabetes_button = toga.Button('No', on_press=self.diabetes_handler, style=Pack(color='black', background_color="#fbf5cc", padding=(-3)))
      nodiabetes_box = create_border(nodiabetes_button, inner_color="#fbf5cc")            
        
      # label + button for alcohol
      alcohol_label = toga.Label("Do you drink alcohol?", style=Pack(color='black', font_size=15, padding=(0, 5)))
        
      yesalco_button = toga.Button('Yes', on_press=self.alcohol_handler, style=Pack(color='black', background_color="#fbf5cc", padding=(-3)))
      yesalco_box = create_border(yesalco_button, inner_color="#fbf5cc")
        
      noalco_button = toga.Button('No', on_press=self.alcohol_handler, style=Pack(color='black', background_color="#fbf5cc", padding=(-3)))
      noalco_box = create_border(noalco_button, inner_color="#fbf5cc")
                
      # label + button for difficulty walking
      walking_label = toga.Label("Do you have difficulty walking?", style=Pack(color='black', font_size=15, padding=(0, 5)))
        
      yeswalk_button = toga.Button('Yes', on_press=self.walking_handler, style=Pack(color='black', background_color="#fbf5cc", padding=(-3)))
      yeswalk_box = create_border(yeswalk_button, inner_color="#fbf5cc")
        
      nowalk_button = toga.Button('No', on_press=self.walking_handler, style=Pack(color='black', background_color="#fbf5cc", padding=(-3)))
      nowalk_box = create_border(nowalk_button, inner_color="#fbf5cc")        

      lifestyle2_button = toga.Button('Lifestyle2', on_press=self.lifestyle2_handler, style=Pack(color='black', background_color="#fbf5cc", padding=(-3)))
      lifestyle2_box = create_border(lifestyle2_button, inner_color="#fbf5cc")
        
      # adding labels to page
      header_box.add(exercise_label)
      header_box.add(highbp_label)
      header_box.add(highcol_label)
      header_box.add(smoker_label)
      header_box.add(stroke_label)
      header_box.add(diabetes_label)
      header_box.add(alcohol_label)
      header_box.add(walking_label)
        
        
      main_box.add(toga.Label(""))
      for button in [e60_119_box, e60_box, e120_180_box,
                     e180_plus_box, back_box]:
         if button != back_box:
            main_box.add(button)
            main_box.add(toga.Label(""))
         else:
            footer_box.add(button)

      main_black_box.add(main_box)

      for box in [header_box, main_black_box, footer_box]:
         content.add(box)

      return content 
        
      # HighBP labels 
      main_box.add(toga.Label(""))
      main_box.add(highbp_label)
      main_box.add(yesbp_box)
      main_box.add(nobp_box)
      main_box.add(toga.Label(""))
        
      # HighBP labels 
      main_box.add(toga.Label(""))
      main_box.add(highcol_label)
      main_box.add(yescol_box)
      main_box.add(nocol_box)
      main_box.add(toga.Label(""))
        
      # Smoker labels 
      main_box.add(toga.Label(""))
      main_box.add(smoker_label)
      main_box.add(yessmoke_box)
      main_box.add(nosmoke_box)
      main_box.add(toga.Label(""))

      # Stroke labels 
      main_box.add(toga.Label(""))
      main_box.add(stroke_label)
      main_box.add(yesstroke_box)
      main_box.add(nostroke_box)
      main_box.add(toga.Label(""))

      # Diabetes labels 
      main_box.add(toga.Label(""))
      main_box.add(stroke_label)
      main_box.add(yesdiabetes_box)
      main_box.add(nodiabetes_box)
      main_box.add(toga.Label(""))
        
      # Alcohol labels 
      main_box.add(toga.Label(""))
      main_box.add(alcohol_label)
      main_box.add(yesalco_box)
      main_box.add(noalco_box)
      main_box.add(toga.Label(""))
        
      # Walking labels
      main_box.add(toga.Label(""))
      main_box.add(walking_label)
      main_box.add(yeswalk_box)
      main_box.add(nowalk_box)
      main_box.add(toga.Label(""))
        

      return content

   def lifestyle_handler(self, widget):
      #add logic
      print("Exercise Handler ran!")
      # Access the label attribute of the button widget to get the user's selection
      self.exercise_selection = widget.text
      print(f"Exercise duration: {self.exercise_selection}")
       
   def highbp_handler(self, widget):
   # Update the high blood pressure variable based on the user's selection
      if widget.text == 'Yes':
         self.app.user.highbp = 1
      elif widget.text == 'No':
         self.app.user.highbp = 0
      print(f"High blood pressure: {self.app.user.highbp}")
     
   def highcol_handler(self, widget):
   # Update the high blood pressure variable based on the user's selection
      if widget.text == 'Yes':
         self.app.user.highcol = 1
      elif widget.text == 'No':
         self.app.user.highcol = 0
      print(f"High cholesterol: {self.app.user.highcol}")
        
   def smoker_handler(self, widget):
   # Update the high blood pressure variable based on the user's selection
      if widget.text == 'Yes':
         self.app.user.smoker = 1
      elif widget.text == 'No':
         self.app.user.smoker = 0
      print(f"Smoker: {self.app.user.smoker}")
        
   def stroke_handler(self, widget):
   # Update the high blood pressure variable based on the user's selection
      if widget.text == 'Yes':
         self.app.user.stroke = 1
      elif widget.text == 'No':
         self.app.user.stroke = 0
      print(f"Smoker: {self.app.user.stroke}")

   def diabetes_handler(self, widget):
   # Update the high blood pressure variable based on the user's selection
      if widget.text == 'Yes':
         self.app.user.stroke = 1
      elif widget.text == 'No':
         self.app.user.stroke = 0
      print(f"Smoker: {self.app.user.diabetes}")
        
   def alcohol_handler(self, widget):
   # Update the high blood pressure variable based on the user's selection
      if widget.text == 'Yes':
         self.app.user.alcohol = 1
      elif widget.text == 'No':
         self.app.user.alcohol = 0
      print(f"Smoker: {self.app.user.alcohol}")
        
   def walking_handler(self, widget):
   # Update the high blood pressure variable based on the user's selection
      if widget.text == 'Yes':
         self.app.user.diffwalking = 1
      elif widget.text == 'No':
         self.app.user.diffwalking = 0
      print(f"Smoker: {self.app.user.diffwalking}")

   def back_handler(self, widget):
      print("Back button pressed!")
      self.app.show_menu()
