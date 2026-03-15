from tkinter import *
import os

def shutdown():
    return os.system("shutdown /s /t 1")

def restart():
    return os.system("shutdown /r /t 1")

def logout():
    return os.system("shutdown /l")  # Windows logout command

# create the tkinter window
master = Tk()  # Fixed: was TK()

# set the title of the window
master.title("system control panel")

# configure window size and background
master.geometry("300x200")
master.config(bg="lightblue")

# function to style buttons
def style_button(button, color):
    button.config(bg=color, fg="white", bd=0, padx=0, pady=0, font=("Arial", 12), width=10, height=2)

# create buttons
btn_shutdown = Button(master, text="Shutdown", command=shutdown)
btn_restart = Button(master, text="Restart", command=restart)
btn_logout = Button(master, text="Logout", command=logout)

# apply styles to buttons
style_button(btn_shutdown, "#FF5733")
style_button(btn_restart, "#33FF57")
style_button(btn_logout, "#5733FF")

# grid layout
btn_shutdown.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")
btn_restart.grid(row=1, column=0, pady=10, padx=10, sticky="nsew")
btn_logout.grid(row=2, column=0, pady=10, padx=10, sticky="nsew")

# center the buttons in the window
master.grid_columnconfigure(0, weight=1)

# start the main event loop
master.mainloop()