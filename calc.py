from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class CalcApp(App):

    def build(self):
        font_size       = 50
        equal_color     = [0,1,1,1]
        operator_color  = [0,0,1,1]

        entire_area = BoxLayout(orientation="vertical", padding=40)
        textinput   = TextInput(
            text='Enter Math Here',
            multiline=False,
            size_hint=(1, .3),
            font_size=68,
        )
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
            number_pad.add_widget(Button(text= number, font_size=font_size))
        number_pad.add_widget(Button(text=".", font_size=font_size))
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

        operation_pad.add_widget(Button(text="+", font_size=font_size, background_color=operator_color))
        operation_pad.add_widget(Button(text="-", font_size=font_size, background_color=operator_color))
        operation_pad.add_widget(Button(text="x", font_size=font_size, background_color=operator_color))
        operation_pad.add_widget(Button(text="/", font_size=font_size, background_color=operator_color))



        entire_area.add_widget(textinput)
        bottom_area.add_widget(number_pad)
        bottom_area.add_widget(operation_pad)
        entire_area.add_widget(bottom_area)



        return entire_area

if __name__ == "__main__":
    CalcApp().run()
