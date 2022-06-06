import PySimpleGUI as sg
from cep_br import CepBr

sg.theme('DarkGray10')
layout = [  [sg.Text('Digite o CEP (somente números): ')],
            [sg.InputText(key='cep')],
            [sg.Button('OK'), sg.Button('Cancelar')],
            [sg.Text('',key='resposta_cep')]
            ]

window = sg.Window('App CEP', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break
    elif event == 'OK':
        cep = values['cep']
        objeto_cep = CepBr(cep)
        objeto_cep_api = objeto_cep.api_via_cep()
        window['resposta_cep'].update(objeto_cep_api)

window.close()