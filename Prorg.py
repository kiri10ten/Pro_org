import os
import shutil
import tkinter as tk
from tkinter import filedialog

file_types = {
    "photos": [".jpeg", ".jpg", ".png", ".gif"],
    "documents": [".pdf", ".doc", ".docx", ".txt", ".rtf"],
    "spreadsheets": [".xls", ".xlsx", ".csv"],
    "presentations": [".ppt", ".pptx"],
    "videos": [".mp4", ".avi", ".mov", ".mkv"],
    "music": [".mp3", ".wav", ".ogg", ".flac"],
}

def create_folder_if_not_exists(Fname):
    if not os.path.exists(Fname):
        os.makedirs(Fname)

def move_file_to_folder(file, file_type):
    shutil.move(file, file_type)

def separate_files_by_type(dir):
    os.chdir(dir)
    files = os.listdir()
    for file in files:
        if os.path.isfile(file):
            exten_name = os.path.splitext(file)[1].strip().lower()
            for file_type, extensions in file_types.items():  
                if exten_name in extensions:
                    create_folder_if_not_exists(file_type)
                    move_file_to_folder(file, file_type)
                    break
def browse_directory():
    directory = filedialog.askdirectory(title="Select Directory")
    if directory:
        separate_files_by_type(directory)
        result_label.config(text="Files organized successfully!")


root = tk.Tk()
root.title("File Organizer")

instruction_label = tk.Label(root, text="Select a directory to organize files:")
instruction_label.pack(pady=10)

browse_button = tk.Button(root, text="Browse", command=browse_directory)
browse_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()

## Additional functionalities 