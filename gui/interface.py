import tkinter as tk

root = tk.Tk()
root.title("logIT")
root.geometry("800x600")

# Main outer frame (grey)
main_frame = tk.Frame(root, bg="grey", width=780, height=590)
main_frame.grid(padx=15, pady=15, column=0, row=0)
main_frame.grid_propagate(False)

# Inner frame for time label (black)
time_label_frame = tk.LabelFrame(main_frame, width=770, height=300, bg="black")
time_label_frame.grid(column=0, row=0, padx=5, pady=5)
time_label_frame.grid_propagate(False)

# Time label inside the frame
time_label = tk.Label(time_label_frame,
                      font=("Courier New", 250, "bold"),
                      text="00:00",
                      fg="white",
                      bg="black")
time_label.pack(fill="both", expand=True)

# Button frame below the time label
button_frame = tk.Frame(main_frame, width=770, height=100, bg="white")
button_frame.grid(column=0, row=1, padx=5, pady=10)
button_frame.grid_propagate(False)

# Create buttons
start_button = tk.Button(button_frame, text="Start", font=("Arial", 20, "bold"), width=10)
pause_button = tk.Button(button_frame, text="Pause", font=("Arial", 20, "bold"), width=10)
resume_button = tk.Button(button_frame, text="Resume", font=("Arial", 20, "bold"), width=10)
finish_button = tk.Button(button_frame, text="Finish", font=("Arial", 20, "bold"), width=10)

# Place buttons in a single row using grid
start_button.grid(row=0, column=0, padx=10, pady=20)
pause_button.grid(row=0, column=1, padx=10, pady=20)
resume_button.grid(row=0, column=2, padx=10, pady=20)
finish_button.grid(row=0, column=3, padx=10, pady=20)


root.mainloop()
