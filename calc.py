from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class InputButton(Button):

    def __init__(self, *args, **kwargs):
        super(InputButton, self).__init__(*args, **kwargs)
        self.font_size  = CalcApp.font_size

    def on_press(self):
        CalcApp.textinput.text += self.text


class OperatorButton(InputButton):

    def __init__(self, *args, **kwargs):
        super(OperatorButton, self).__init__(*args, **kwargs)
        self.background_color = CalcApp.operator_color


class CalcApp(App):
    font_size       = 50
    equal_color     = [0,1,1,1]
    operator_color  = [0,0,1,1]

    #made text input a class variable b/c I wanted to make it easy to access
    textinput       = TextInput(
        text='',
        multiline=False,
        size_hint=(1, 1),
        font_size=68,
    )


    def build_operation_pad(self):
        operation_pad   = GridLayout(
            cols=1,
            size_hint=(.2, 1),
            spacing=10,
        )

        for operation in ["+", "-", "x", "/"]:
            operation_pad.add_widget(OperatorButton(text=operation))

        return operation_pad

    def build_number_pad(self):
        number_pad      = GridLayout(
            cols=3,
            size_hint=(1, 1),
            spacing=10,
        )

        for i in xrange(0, 10):
            number = str(i)
            number_pad.add_widget(InputButton(text=number))
        number_pad.add_widget(InputButton(text="."))

        number_pad.add_widget(
            Button(
                text="=",
                font_size=CalcApp.font_size,
                background_color=CalcApp.equal_color)
        )
        return number_pad

    def define_top_area(self):
        return BoxLayout(size_hint=(1, .3))

    def define_entire_area(self):
        return BoxLayout(orientation="vertical", padding=40)

    def define_bottom_area(self):
        return BoxLayout(
            orientation="horizontal",
            size_hint=(1, 1),
            spacing=40,
            padding=[0,40,0,0]
        )

    def build(self):
        """
            This function build the entire area of app using the top and bottom
            parts of calculator app
        """
        #define main areas of app
        entire_area = self.define_entire_area()
        top_area    = self.define_top_area()
        bottom_area = self.define_bottom_area()

        #build app from main areas
        entire_area.add_widget(top_area)
        entire_area.add_widget(bottom_area)

        #build  top area
        top_area.add_widget(CalcApp.textinput)

        #build bottom area
        number_pad      = self.build_number_pad()
        operation_pad   = self.build_operation_pad()
        bottom_area.add_widget(number_pad)
        bottom_area.add_widget(operation_pad)


        #return entire area
        return entire_area

if __name__ == "__main__":
    CalcApp().run()
