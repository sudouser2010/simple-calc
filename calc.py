from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class InputButton(Button):

    def __init__(self, *args, **kwargs):
        super(InputButton, self).__init__(*args, **kwargs)
        self.font_size  = 50
        self.textinput  = kwargs["textinput"]

    def on_press(self):
        self.textinput.text += self.text


class OperatorButton(InputButton):

    def __init__(self, *args, **kwargs):
        super(OperatorButton, self).__init__(*args, **kwargs)
        self.background_color = [0,0,1,1]



class CalcApp(App):

    def build(self):
        font_size       = 50
        equal_color     = [0,1,1,1]


        entire_area = BoxLayout(orientation="vertical", padding=40)
        textinput   = TextInput(
            text='',
            multiline=False,
            size_hint=(1, .3),
            font_size=68,
        )
        top_area    = BoxLayout(size_hint=(1, .3))
        bottom_area = BoxLayout(
            orientation="horizontal",
            size_hint=(1, 1),
            spacing=40,
            padding=[0,40,0,0]
        )


        number_pad      = GridLayout(
            cols=3,
            size_hint=(1, 1),
            spacing=10,
        )

        for i in xrange(0, 10):
            number = str(i)
            number_pad.add_widget(InputButton(text=number, textinput=textinput))
        number_pad.add_widget(InputButton(text=".", textinput=textinput))

        number_pad.add_widget(
            Button(
                text="=",
                font_size=font_size,
                background_color=equal_color)
        )

        operation_pad   = GridLayout(
            cols=1,
            size_hint=(.2, 1),
            spacing=10,

        )

        for operation in ["+", "-", "x", "/"]:
            operation_pad.add_widget(OperatorButton(text=operation, textinput=textinput))




        entire_area.add_widget(textinput)
        entire_area.add_widget(bottom_area)

        bottom_area.add_widget(number_pad)
        bottom_area.add_widget(operation_pad)




        return entire_area

if __name__ == "__main__":
    CalcApp().run()
