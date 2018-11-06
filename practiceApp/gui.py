'''
Developed by Zachary Filosi
'''
import kivy
kivy.require('1.0.7')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class Menu(GridLayout):
    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
        self.cols = 3
        self.add_widget(Button(text = "Classes"))
        self.add_widget(Button(text = "SCiPs"))
    

class TestApp(App):
    def build(self):
        return Button(text="Secure Contain Protect")



if __name__=='__main__':
    TestApp.run()


TestApp().run()
