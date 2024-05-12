import tkinter as tk
from tkinter import filedialog
import subprocess
import sys
import os

class PythonScriptRunnerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Automated Attendance System")
        self.root.geometry("1280x720")
        self.root.configure(bg='#3498db')
        # Buttons
        button_width = 20
        button_height = 3

        self.run_main_button = tk.Button(root, text="Mark Attendance", command=self.run_main, bg='#7eac61', fg='white', width=button_width, height=button_height)
        self.run_main_button.pack(pady=20)

        self.run_encode_button = tk.Button(root, text="Upload Images", command=self.run_encode, bg='#e74c3c', fg='white', width=button_width, height=button_height)
        self.run_encode_button.pack(pady=20)

        self.run_data_button = tk.Button(root, text="Upload Student Data", command=self.run_data, bg='#91dc2c', fg='white', width=button_width, height=button_height)
        self.run_data_button.pack(pady=20)


    def run_main(self):
        self.run_script("main.py")

    def run_encode(self):
        self.run_script("encodeFile.py")

    def run_data(self):
        self.run_script("addDataToDataBase.py")

    def run_script(self, script_name):
        try:
            venv_path = os.path.join(os.getcwd(), "venv")
            activate_this = os.path.join(venv_path, "Scripts" if sys.platform == "win32" else "bin", "activate_this.py")

            # Activate the virtual environment
            with open(activate_this) as file_:
                exec(file_.read(), dict(__file__=activate_this))

            subprocess.run([sys.executable, script_name], check=True)

        except subprocess.CalledProcessError:
            print(f"Error running {script_name}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PythonScriptRunnerUI(root)
    root.mainloop()
