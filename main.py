import tkinter as tk
import datetime
import pandas as pd
from datetime import datetime, timedelta
from tkinter import *

running = False
actual_start_time = 0
start_time = 0
elapsed_time = timedelta(0)
timer_id = None

def update_timer():
    global timer_id, elapsed
    current_time = datetime.now()
    elapsed = current_time - start_time
    time_str = str(elapsed).split('.')[0]  # Format: HH:MM:SS
    time_label.config(text=time_str)
    timer_id = root.after(1000, update_timer)


def start_timer():
    global running,start_time
    if not running:
        start_time = datetime.now() - elapsed_time
        actual_start_time = start_time
        update_timer()
        running = True

def pause_timer():
    global running, timer_id
    if running:
        root.after_cancel(timer_id)
        running = False

def resume_timer():
    global running, start_time
    if not running:
        start_time = datetime.now() - elapsed
        update_timer()
        running = True


def save():
    global start_time,actual_start_time,elapsed_time
    elapsed_time = start_time - datetime.now()



root = tk.Tk()
root.title("Task Timer")
root.geometry("600x300")

df = pd.read_csv("category.csv")

categories = df["category_name"].tolist()
opt = StringVar(value="Study")
OptionMenu(root, opt, *categories).pack()


# Stopwatch Frame (full height)
stopwatch_frame = tk.Frame(root, bg="lightgray")
stopwatch_frame.pack(fill="both", expand=True)

# Time Label — make it really visible with color and spacing
time_label = tk.Label(
    stopwatch_frame,
    text="00:00:00",
    font=("Helvetica", 30, "bold"),
    fg="white",
    bg="red",
    relief="solid",
    bd=2,
    width=10,
    height=2
)
time_label.pack(pady=30)


# Button Frame
button_frame = tk.Frame(stopwatch_frame, bg="lightgray")
button_frame.pack()

tk.Button(button_frame, text="Start", width=12, command=start_timer).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Pause", width=12, command=pause_timer).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Resume", width=12, command=resume_timer).grid(row=0, column=2, padx=5)
#tk.Button(button_frame, text="Stop & Save", width=12, command=stop_and_save).grid(row=0, column=3, padx=5)
root.mainloop()

# import sys
# print("Running Python from:", sys.executable)
