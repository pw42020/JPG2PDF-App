from kivy.app import App
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget

from plyer import filechooser
import os
from shutil import copy

class MyWidget(Widget):
    
    def findfile(self):
        path = str(filechooser.open_file(title="Pick an image or document",path=r"C:\Users\Ninja\OneDrive\Desktop"))
        path=path.replace("[","")
        path=path.replace("]","")
        path=path.replace("'","")
        copy(path,r"C:\Users\Ninja\OneDrive\Documents\GitHub\App\Documents")
        


    def selected(self,file):
        try:
            self.ids.image.source=filename[0]
        except:
            pass



class FileChooserWindow(App):
    def build(self):

        return MyWidget()




if __name__=="__main__":
    FileChooserWindow().run()
