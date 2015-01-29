from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput




class CalcApp(App):

    def build(self):
        entire_area = BoxLayout(orientation="vertical")
        textinput   = TextInput(text='Enter Math Here',
                              multiline=False,
                              size_hint=(1, .2))

        bottom_area = BoxLayout(orientation="horizontal")

        l =  Label(text="Hello!",
                   font_size = 35)

        entire_area.add_widget(textinput)
        entire_area.add_widget(bottom_area)

        return entire_area

if __name__ == "__main__":
    CalcApp().run()
