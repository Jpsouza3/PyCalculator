from calendar import c
from turtle import color
import PySimpleGUI as sg
###
def create_window():
    sg.theme('DarkBlue13')
    sg.set_options(button_element_size=(6,3))
    btnSize = (6,3)

    layout = [
        [sg.Text('Result:' , pad=(5,5))],
        [sg.Button('Enter',expand_x=True) , sg.Button('Clear', expand_x=True)],
        [sg.Button(1 , size=btnSize) , sg.Button(2 , size=btnSize) , sg.Button(3 , size=btnSize) , sg.Button('*' , size=btnSize)],
        [sg.Button(4 , size=btnSize) , sg.Button(5 , size=btnSize) , sg.Button(6 , size=btnSize), sg.Button('+' , size=btnSize)],
        [sg.Button(7 , size=btnSize) , sg.Button(8 , size=btnSize) , sg.Button(9 , size=btnSize) , sg.Button('-' , size=btnSize)],
        [sg.Button(0 , expand_x=True) , sg.Button('.' , size=btnSize) , sg.Button('/' , size=btnSize)]

    ]
    return sg.Window('Calculator' , layout)
####

window = create_window()

current_num = []

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event in ['0','1','2','3','4','5','6','7','8','9','.']:
        current_num.append(event)
        num_string = ''.join(current_num)
        print(num_string)

    if event in ['+','-','*','/']:
        print(event)

    if event == 'Enter':
        print(event)

    if event == 'Clear':
        print(event)

window.close()