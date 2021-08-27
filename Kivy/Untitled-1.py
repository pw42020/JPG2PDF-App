from types import BuiltinFunctionType
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.menu import MDDropdownMenu
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.uix.screenmanager import Screen,ScreenManager



import os
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Image,SimpleDocTemplate
from plyer import filechooser
from shutil import copy,move
from reportlab.lib.pagesizes import letter


Window.size=(300,500) ######MAKE SURE TO REMOVE LATER ######


class MenuScreen(Screen):
    pass


class BookmarkScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class ContentNavigationDrawer(BoxLayout):
    pass


class PDFNameCheck(BoxLayout):
    pass

class CreatePDF(MDApp):
    menu=ObjectProperty()
    dialog=None

    def build(self):
        self.kv=Builder.load_file("createpdf.kv")
        self.theme_cls.primary_palette="DeepPurple"
        return self.kv
        
    def on_start(self):
        self.menu=MDDropdownMenu(caller=self.kv.ids.plus,width_mult=4)
        

        self.menu.items.append({
            "viewclass":"OneLineListItem",
            "text":"Upload Document",
            "callback":self.option_callback,
            "on_release":self.findfile
        })
        self.menu.items.append({
            "viewclass":"OneLineListItem",
            "text":"Upload Image",
            "callback":self.option_callback,
            "on_release":self.findfile
        })
        self.menu.items.append({
            "viewclass":"OneLineListItem",
            "text":"Create PDF",
            "callback":self.option_callback,
            "on_release":self.generatepdf
        })

        

    
    def option_callback(self,text_of_option):
        print(text_of_option)


    
    def findfile(self):
        path = str(filechooser.open_file(title="Pick an image or document",path=r"C:\Users\Ninja\OneDrive\Desktop"))
        path=path.replace("[","")
        path=path.replace("]","")
        path=path.replace("'","")
        copy(path,r"C:\Users\Ninja\OneDrive\Documents\GitHub\App\Documents")
        
    def dialogthing(self):
        if not self.dialog:
            self.dialog=MDDialog(
                type="custom",
                content_cls=PDFNameCheck(),
                buttons=[
                    MDFlatButton(
                            text="CANCEL", text_color=self.theme_cls.primary_color,on_release=self.closedialog
                        ),
                    MDFlatButton(
                        text="OK", text_color=self.theme_cls.primary_color,on_release=self.closedialog
                    ),

                ]
            )
        self.dialog.open()


    def closedialog(self,obj):
        self.dialog.dismiss()
    def generatepdf(self):
        self.pdfname="Untitled"
        path = filechooser.open_file(title="Select Image(s)",path=r"C:\Users\Ninja\OneDrive\Desktop",multiple=True)

        
        
        save_name = os.path.join(os.path.expanduser("~"), r"OneDrive\Documents\GitHub\App\Documents")

        self.dialogthing()
        

        canvas=Canvas(save_name+r"\\"+self.pdfname+".pdf",pagesize=letter)
        
        for i in range(len(path)):
            newstr=str(path[i])
            canvas.drawInlineImage(newstr,0,0)
            canvas.showPage()

        
        canvas.save()
        self.menu.dismiss()

    




if __name__=="__main__":
    CreatePDF().run()
