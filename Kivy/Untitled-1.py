from types import BuiltinFunctionType
from kivymd.app import MDApp
from kivy.uix.filechooser import FileChooserIconView
from kivy.core.window import Window
from kivymd.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.list import OneLineIconListItem,MDList
from kivy.properties import StringProperty
from kivymd.theming import ThemableBehavior

from kivy.lang.builder import Builder

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

class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()

class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        '''Called when tap on a menu item.'''

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color

class CreatePDF(MDApp):
    def build(self):
        kv=Builder.load_file("createpdf.kv")
        menu_items = [
            {
                "text": f"Item {i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"Item {i}": self.menu_callback(x),
            } for i in range(5)
        ]
        self.menu = MDDropdownMenu(

            items=menu_items,
            width_mult=4,
        )
        self.theme_cls.primary_palette="DeepPurple"
        return kv

    def on_start(self):
        icons_item={
            "folder":"Open folders",
            "upload":"Upload Document"

        }
        for icon_name in icons_item.keys(): #content_drawer.ids.md_list.add_widget
            self.root.ids.md_list.add_widget(
            ItemDrawer(icon=icon_name, text=icons_item[icon_name])
        )

    def callback(self,button):
        self.menu.caller=button
        self.menu.open()
    def menu_callback(self):
        self.menu.dismiss()

    

        

    def navigation_draw(self):
        print("Navigation")
    
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