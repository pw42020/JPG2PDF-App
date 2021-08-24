from types import BuiltinFunctionType
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.menu import MDDropdownMenu
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty

from plyer import filechooser
from shutil import copy

from kivy.uix.screenmanager import Screen,ScreenManager

Window.size=(300,500) ######MAKE SURE TO REMOVE LATER ######


class MenuScreen(Screen):
    pass


class DocumentsScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class ContentNavigationDrawer(BoxLayout):
    pass




class CreatePDF(MDApp):
    menu=ObjectProperty()
    def build(self):
        self.kv=Builder.load_file("createpdf.kv")
        self.theme_cls.primary_palette="DeepPurple"
        return self.kv
        
    def on_start(self):
        self.menu=MDDropdownMenu(caller=self.kv.ids.plus,width_mult=4)
        
        self.menu.items.append({
            "viewclass":"OneLineListItem",
            "text":"Upload Document",
            "callback":self.option_callback
        })
        self.menu.items.append({
            "viewclass":"OneLineListItem",
            "text":"Upload Image",
            "callback":self.option_callback
        })
        self.menu.items.append({
            "viewclass":"OneLineListItem",
            "text":"Create PDF",
            "callback":self.option_callback
        })

    
    def option_callback(self,text_of_option):
        print(text_of_option)


    
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
    




if __name__=="__main__":
    CreatePDF().run()
