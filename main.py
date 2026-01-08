import tkinter as tk

auth = tk.Tk()
auth.geometry("500x500")
auth.title("TASK MANAGER")
auth.config(bg = "white")

window_width = 600
window_height = 400

screen_width = auth.winfo_screenwidth()
screen_height = auth.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

auth.geometry(f"{window_width}x{window_height}+{x}+{y}")

auth.mainloop()