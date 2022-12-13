import os
import subprocess
import sys
import traceback
from re import findall
from tkinter import *


def set_text(text_area: Text, text: str):
    text_area.delete("1.0", END)
    text_area.insert(END, text)


def run_code(code_area: Text, output_area: Text):
    code_string = code_area.get("1.0", END)
    py_file_path = "tmp.py"

    with open(py_file_path, "w") as f:
        f.write(code_string)

    try:
        result = subprocess.run(
            [sys.executable, py_file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            encoding="utf-8"
        )

        set_text(output_area, result.stdout)
    except Exception:
        tb = traceback.format_exc()
        set_text(output_area, str(tb))
    finally:
        os.remove(py_file_path)


def select_file(current_dir: str, list_box: Listbox,  code_area: Text):
    indices = list_box.curselection()

    if not indices:
        return

    selected_file = list_box.get(indices[0])
    select_file_path = os.path.join(current_dir, selected_file)

    with open(select_file_path) as f:
        file_text = f.read()
        set_text(code_area, file_text)


def select_directory(context, list_box: Listbox):
    from tkinter import filedialog

    current_dir = filedialog.askdirectory(
        title="Open directory", initialdir=context.get_current_dir())

    context.set_current_dir(current_dir)
    update_list_box(list_box, current_dir)


def update_list_box(list_box: Listbox, new_directory:str):
    list_box.delete(0, END)
    for file_name in os.listdir(new_directory):
        list_box.insert(0, file_name)