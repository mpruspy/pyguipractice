import PySimpleGUI as sg
import functions

titulo = sg.Text("Lista de tareas")
input_box1 = sg.InputText(tooltip="Ingresa una tareita", key="todo")
agregar = sg.Button("Add")


window = sg.Window("File zipper",
                   layout=[[titulo],[input_box1, agregar]],
                   font=("Helvetica", 20))
while True:
    event, values = window.read()
    print(values)
    match event:
        case "Add":
            functions.imprimir(event)
        case sg.WIN_CLOSED:
            break

window.close()