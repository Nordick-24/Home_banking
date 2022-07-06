from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
#importing


KV = """
MyBL:
    orientation: "vertical"
    size_hint: (0.95, 0.95)
    pos_hint: {"center_x": 0.5, "center_y":0.5}
    
    Label:
        font_size: "30sp"
        multiline: True
        text_size:self.width*0.98, None
        size_hint_x: 1.0
        size_hint_y: None
        height: self.texture_size[1] + 15
        text: root.data_label
    
    Button:
        text: "Банк на каждого"
        bold: True
        background_color:'#00FFCE'
        size_hint: (1,0.5)
        on_press: root.callback()
    
    Button:
        text: "Банк для всей семьи"
        bold: True
        background_color:'#00FFCE'
        size_hint: (1,0.5)
        on_press: root.callback()

"""

class MyBL(BoxLayout):
    data_label = StringProperty("Привет! выбери необходимый вариант")
    def callback(self):
        

class MyApp(App):
    running = True
    def build(self):
        return Builder.load_string(KV)

    def on_stop(self):
        self.running = False





MyApp().run()
