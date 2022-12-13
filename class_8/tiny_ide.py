import os
from collections.abc import Collection
from tkinter import *

import listeners


class Context:
    _current_dir = os.getcwd()

    def get_current_dir(self) -> str:
        return self._current_dir

    def set_current_dir(self, new_path):
        self._current_dir = new_path

window = Tk()
context = Context()



window.title("TIDE")
window.minsize(width=200, height=200)

# Code
code_label = Label(window, text="Code:", font=("Arial Bold", 10))
code_area = Text(window, height=15, width=80, font=("Courier", 10))
code_scroll = Scrollbar(window, command=code_area.yview)
code_area['yscrollcommand'] = code_scroll.set

# Output
output_label = Label(window, text="Output:", font=("Arial Bold", 10))
output_area = Text(window, height=5, width=80, font=("Courier", 10))
output_scroll = Scrollbar(window, command=output_area.yview)
output_area['yscrollcommand'] = output_scroll.set

# Buttons

save_btn = Button(window, text="Save")
run_btn = Button(window, text="Run", command=lambda: listeners.run_code(
    code_area, output_area))
exit_btn = Button(window, text="Exit")
dir_btn = Button(window, text="Directory", command=lambda: listeners.select_directory(context, file_list_box))

# Files
files = StringVar(value=os.listdir(context.get_current_dir()))
file_list_box = Listbox(
    window,
    listvariable=files,
    height=5,
    selectmode="single"
)

file_scroll = Scrollbar(window, orient='vertical', command=file_list_box.yview)
file_list_box['yscrollcommand'] = file_scroll.set
file_list_box.bind('<<ListboxSelect>>', lambda e: listeners.select_file(context.get_current_dir(), file_list_box, code_area))


# Layout
dir_btn.grid(column=0, row=0, sticky='ew')
file_list_box.grid(column=0, row=1, rowspan=9, sticky='nesw')
file_scroll.grid(column=1, row=1, rowspan=9, sticky='nesw')

code_label.grid(column=2, row=0, sticky="w")
code_area.grid(column=2, row=1, columnspan=5, rowspan=4)
code_scroll.grid(column=7, row=1, columnspan=1, rowspan=4, sticky="nesw")

output_label.grid(column=2, row=5, columnspan=1, sticky="w")
output_area.grid(column=2, row=6, columnspan=5, rowspan=4)
output_scroll.grid(column=7, row=6, columnspan=2, rowspan=4, sticky="nesw")

run_btn.grid(column=4, row=0, sticky="e")
save_btn.grid(column=5, row=0, sticky="e")
exit_btn.grid(column=6, row=0, sticky="e")

window.mainloop()
