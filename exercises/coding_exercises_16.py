import PySimpleGUI as sg

label1 = sg.Text("Enter feet:")
input1 = sg.InputText()
label2 = sg.Text("Enter inches:")
input2 = sg.InputText()
convert_button = sg.Button("Convert")

window = sg.Window("Converter", [
    [label1, input1],
    [label2, input2],
    [convert_button],
])
window.read()
window.close()
