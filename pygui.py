import PySimpleGUI as sg

comprimir = sg.Text("Seleccione los archivos a comprimir")
destino = sg.Text("Seleccione carpeta de destino")
input_box1 = sg.Input()
input_box2 = sg.Input()
elegir_archivo = sg.FileBrowse("Seleccionar")
elegir_carpeta = sg.FolderBrowse("Seleccionar")
ejecutar = sg.Button("COMPRIMIR")


window = sg.Window("File zipper",
                   layout=[[comprimir, input_box1, elegir_archivo],
                           [destino, input_box2, elegir_carpeta],
                           [ejecutar]])
window.read()
window.close()