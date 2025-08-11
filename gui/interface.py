#interface.py
import tkinter as tk
from core.stopwatch import Stopwatch

class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title("logIT")
        self.root.geometry("800x600")

        # Create Stopwatch instance
        self.stopwatch = Stopwatch()

        # Main outer frame (grey)
        main_frame = tk.Frame(root, bg="grey", width=780, height=590)
        main_frame.grid(padx=15, pady=15, column=0, row=0)
        main_frame.grid_propagate(False)

        # Inner frame for time label (black)
        time_label_frame = tk.LabelFrame(main_frame, width=770, height=300, bg="black")
        time_label_frame.grid(column=0, row=0, padx=5, pady=5)
        time_label_frame.grid_propagate(False)

        # Time label (I used 120 font so it fits; change to 250 if you prefer)
        self.time_label = tk.Label(time_label_frame,
                                   font=("Courier New", 120, "bold"),
                                   text="00:00:00",
                                   fg="white",
                                   bg="black")
        self.time_label.pack(fill="both", expand=True)

        # Button frame
        button_frame = tk.Frame(main_frame, width=770, height=100, bg="white")
        button_frame.grid(column=0, row=1, padx=5, pady=10)
        button_frame.grid_propagate(False)

        # Buttons (bound to stopwatch methods)
        start_button = tk.Button(button_frame, text="Start", font=("Arial", 20, "bold"), width=10,
                                 command=self._start)
        pause_button = tk.Button(button_frame, text="Pause", font=("Arial", 20, "bold"), width=10,
                                 command=self._pause)
        resume_button = tk.Button(button_frame, text="Resume", font=("Arial", 20, "bold"), width=10,
                                  command=self._resume)
        finish_button = tk.Button(button_frame, text="Finish", font=("Arial", 20, "bold"), width=10,
                                  command=self._finish)

        start_button.grid(row=0, column=0, padx=10, pady=20)
        pause_button.grid(row=0, column=1, padx=10, pady=20)
        resume_button.grid(row=0, column=2, padx=10, pady=20)
        finish_button.grid(row=0, column=3, padx=10, pady=20)

        # Keep the display updated (always update the label; stopwatch handles running/paused)
        self.update_display()

    def _start(self):
        self.stopwatch.start()

    def _pause(self):
        self.stopwatch.pause()

    def _resume(self):
        self.stopwatch.resume()

    def _finish(self):
        self.stopwatch.reset()

    def update_display(self):
        # Always refresh the label from stopwatch state
        self.time_label.config(text=self.stopwatch.get_elapsed_time())
        self.root.after(200, self.update_display)   # refresh 5x/sec for a smoother feel


