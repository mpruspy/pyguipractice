import PySimpleGUI as sg

titulo = sg.Text("Este es mi programita")
label = sg.Text("Ingrese un valor")
input_box = sg.InputText(tooltip="Enter to-do")
add_button = sg.Button("Agregar")


window = sg.Window("Mi Aplicacion", layout=[[titulo],[label, input_box, add_button]])
window.read()
window.close()