from nicegui import ui
from calc import average
def calc():
    answerpanel.clear()
    with answerpanel:
        ui.label("Answer").style("font-size:25px;")
        ui.label(average(nums=nums)).style("font-size:25px;")
def addnew():
    def close():
        nums.append(int(newnumber.value))
        with numspanel:
            ui.label(newnumber.value).style("font-size:25px;")
        dialog.close()
    with ui.dialog() as dialog, ui.card():
        newnumber = ui.input("New Number")
        ui.button(icon="check", on_click=close, color="green")
    dialog.open()
def reset():
    global nums
    nums = []
    numspanel.clear()
    answerpanel.clear()
    with numspanel:
        ui.label("Numbers").style("font-size:25px;")
    with answerpanel:
        ui.label("Answer").style("font-size:25px;")
nums = []
ui.label("Avevrage GUI").style("font-size:50px;")
ui.separator()
numspanel = ui.card()
with numspanel:
    ui.label("Numbers").style("font-size:25px;")
ui.separator()
ui.button(on_click=addnew, icon="add")
ui.separator()
ui.button("Calculate", on_click=calc, color="green")
ui.separator()
ui.button("Reset", on_click=reset, color="red")
ui.separator()
answerpanel = ui.card()
with answerpanel:
    ui.label("Answer").style("font-size:25px;")

ui.run(dark=True)