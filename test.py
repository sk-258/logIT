import tkinter as tk

root = tk.Tk()
root.title("Label Test")
root.geometry("300x200")

label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 20), fg="white", bg="blue")
label.pack(pady=40)

root.mainloop()
