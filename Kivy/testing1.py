from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager



kv='''
ScreenManager:
    MenuScreen:
        BoxLayout:
            MDTextField:
                pos_hint:{"center_x":0.5,"center_y":0.5}
                hint_text:"Enter something"
                width:0.5
            MDRectangleFlatButton:
                text:"Press me"
            MDRectangleFlatButton:
                text:"Don't Press me"
'''

class MenuScreen(Screen):
    pass

class App(MDApp):
    def build(self):
        screen=Screen()
        kvcode=Builder.load_string(kv)
        screen.add_widget(kvcode)
        return screen

if __name__=="__main__":
    App().run()