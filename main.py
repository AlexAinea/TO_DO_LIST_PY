import tkinter as tk

auth = tk.Tk()
auth.geometry("500x500")
auth.title("TASK MANAGER")
auth.config(bg = "#87CEEB")

window_width = 600
window_height = 400

screen_width = auth.winfo_screenwidth()
screen_height = auth.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

auth.geometry(f"{window_width}x{window_height}+{x}+{y}")

log_in_frame = tk.Frame(auth, bg="#87CEEB")
log_in_frame.pack()

username_log_in_label = tk.Label(log_in_frame, text="USERNAME: ", bg="#87CEEB", fg="black")
username_log_in_label.grid(row = 0, column=0)

username_log_in_entry = tk.Entry(log_in_frame, bg="#87CEEB", fg="black", bd=0, highlightthickness = 1)
username_log_in_entry.grid(row = 0, column=1)

password_log_in_label = tk.Label(log_in_frame, text="PASSWORD: ", bg="#87CEEB", fg="black")
password_log_in_label.grid(row = 1, column=0)

password_log_in_entry = tk.Entry(log_in_frame, bg="#87CEEB", fg="black", bd=0, highlightthickness = 1, show = '*')
password_log_in_entry.grid(row = 1, column=1)

log_in_button = tk.Button(log_in_frame, text="LOG IN", bg="white",fg="black", activebackground="white", activeforeground="black",borderwidth=0, highlightthickness=0,highlightbackground="white", relief="flat", padx=10, pady=4, cursor="hand2")
log_in_button.grid(row = 2, column= 0)

auth.mainloop()