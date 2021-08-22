from kivymd.app import MDApp
from kivy.uix.filechooser import FileChooserIconView
from kivy.core.window import Window

from kivy.uix.widget import Widget

from kivy.lang.builder import Builder

from plyer import filechooser
from shutil import copy

from kivy.uix.screenmanager import Screen,ScreenManager

Window.size=(300,500) ######MAKE SURE TO REMOVE LATER ######


class MenuScreen(Screen):
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


class DocumentsScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass



class CreatePDF(MDApp):
    def build(self):
        kv=Builder.load_file("createpdf.kv")
        return kv
    def navigation_draw(self):
        print("Navigation")
    
    




if __name__=="__main__":
    CreatePDF().run()

"""
GridLayout:
        cols:1
        size: root.width,root.height*0.2
        Button:
            text:"Add Document"
            on_press:root.findfile()
        Button:
            text:"Documents"
            on_press:
                root.manager.transition.direction="left"
                app.root.current="documents"""