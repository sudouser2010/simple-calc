from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

import re
import calculator

class InputButton(Button):

    def __init__(self, *args, **kwargs):
        super(InputButton, self).__init__(*args, **kwargs)
        self.font_size  = CalcApp.button_font_size

    def on_press(self):
        CalcApp.textinput.text += self.text


class OperatorButton(InputButton):

    def __init__(self, *args, **kwargs):
        super(OperatorButton, self).__init__(*args, **kwargs)
        self.background_color = CalcApp.operator_color


class EqualButton(Button):

    def __init__(self, *args, **kwargs):
        super(Button, self).__init__(*args, **kwargs)
        self.font_size          = CalcApp.button_font_size
        self.text               = "="
        self.background_color   = CalcApp.equal_color

    def on_press(self):
        try:
            matchObj        = re.match(CalcApp.input_regex, CalcApp.textinput.text)
            left_operand    = int(matchObj.group(1))
            operator        = matchObj.group(2)
            right_operand   = int(matchObj.group(3))

            #this codifies the operator as an integer for the calc module
            operator_int    = ['+','-','*','/'].index(operator)

            #this is where text input will be processed by the calculator module
            result = calculator.process_input(left_operand, right_operand, operator_int)
            CalcApp.textinput.text = str(result)

        except:
            print "error with user input"


class ClearButton(Button):

    def __init__(self, *args, **kwargs):
        super(Button, self).__init__(*args, **kwargs)
        self.font_size          = CalcApp.button_font_size
        self.text               = "clear"
        self.background_color   = CalcApp.clear_color
        self.size_hint          = (.3, 1)

    def on_press(self):
        CalcApp.textinput.text = ""

class CalcApp(App):

    #sets up characteristics of calculator app
    button_font_size= 50
    input_font_size = 68
    clear_color     = [1,0,0,1]
    equal_color     = [0,1,1,1]
    operator_color  = [0,0,1,1]
    padding         = 40
    spacing         = 10

    decimal_regex   = r'([-+]?\d*\.*\d+)'       #definition of decimal in regex
    operations      = '([-+*/])'                #character class for allowed operations
    input_regex     = r'{0}{1}{0}'.format(decimal_regex, operations)

    #made text input a class variable b/c I wanted to make it easy to access
    textinput       = TextInput(
        text='',
        multiline=False,
        size_hint=(1, 1),
        font_size=input_font_size,
    )


    def build_operation_pad(self):
        operation_pad   = GridLayout(
            cols=1,
            size_hint=(.2, 1),
            spacing=CalcApp.spacing,
        )

        for operation in ["+", "-", "*", "/"]:
            operation_pad.add_widget(OperatorButton(text=operation))

        return operation_pad

    def build_number_pad(self):
        number_pad      = GridLayout(
            cols=3,
            size_hint=(1, 1),
            spacing=CalcApp.spacing,
        )

        for i in xrange(0, 10):
            number = str(i)
            number_pad.add_widget(InputButton(text=number))
        number_pad.add_widget(InputButton(text="."))

        number_pad.add_widget(EqualButton())
        return number_pad

    def define_top_area(self):
        return BoxLayout(size_hint=(1, .3))

    def define_entire_area(self):
        return BoxLayout(orientation="vertical", padding=CalcApp.padding)

    def define_bottom_area(self):
        return BoxLayout(
            orientation="horizontal",
            size_hint=(1, 1),
            spacing=CalcApp.padding,
            padding=[0,CalcApp.padding,0,0]
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
        top_area.add_widget(ClearButton())

        #build bottom area
        number_pad      = self.build_number_pad()
        operation_pad   = self.build_operation_pad()
        bottom_area.add_widget(number_pad)
        bottom_area.add_widget(operation_pad)

        #return entire area
        return entire_area

if __name__ == "__main__":
    CalcApp().run()
