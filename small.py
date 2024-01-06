from nicegui import ui
from calc import average
def calc(): ui.label(average(nums=nums))
def addnew():
    def close():
        nums.append(int(newnumber.value))
        dialog.close()
    with ui.dialog() as dialog, ui.card():
        newnumber = ui.input("New Number")
        ui.button('Add', on_click=close)
    dialog.open()
nums = []

ui.button("+", on_click=addnew)
ui.button("Calculate", on_click=calc)

ui.run(dark=True)