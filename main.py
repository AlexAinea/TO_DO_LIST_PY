import tkinter as tk

current_frame_auth = None
def authentication():
    global current_frame_auth

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

    def log_in_function():
        global current_frame_auth
        if current_frame_auth:
            current_frame_auth.destroy()
            current_frame_auth = None
        else:
            log_in_frame = tk.Frame(auth, bg="#87CEEB")
            current_frame_auth = log_in_frame
            current_frame_auth.place(x = 160, y = 250)

            username_log_in_label = tk.Label(current_frame_auth, text="USERNAME: ", bg="#87CEEB", fg="black")
            username_log_in_label.grid(row = 0, column=0)

            username_log_in_entry = tk.Entry(current_frame_auth, bg="#87CEEB", fg="black", bd=0, highlightthickness = 1, relief="flat", borderwidth=0)
            username_log_in_entry.grid(row = 0, column=1)

            password_log_in_label = tk.Label(current_frame_auth, text="PASSWORD: ", bg="#87CEEB", fg="black")
            password_log_in_label.grid(row = 1, column=0)

            password_log_in_entry = tk.Entry(current_frame_auth, bg="#87CEEB", fg="black", bd=0, highlightthickness = 1, show = '*')
            password_log_in_entry.grid(row = 1, column=1)

            log_in_button = tk.Button(current_frame_auth, text="LOG IN", bg="white",fg="black", activebackground="white", activeforeground="black",borderwidth=0, highlightthickness=0,highlightbackground="white", relief="flat", padx=10, pady=4, cursor="hand2")
            log_in_button.grid(row = 2, column= 0)

    def sign_up_function():
        global current_frame_auth
        if current_frame_auth:
            current_frame_auth.destroy()
            current_frame_auth = None
        else:
            sign_up_frame = tk.Frame(auth, bg="#87CEEB")
            current_frame_auth = sign_up_frame
            current_frame_auth.place(x = 160, y = 250)

            username_log_in_label = tk.Label(current_frame_auth, text="USERNAME: ", bg="#87CEEB", fg="black")
            username_log_in_label.grid(row = 0, column=0)

            username_log_in_entry = tk.Entry(current_frame_auth, bg="#87CEEB", fg="black", bd=0, highlightthickness = 1, relief="flat", borderwidth=0)
            username_log_in_entry.grid(row = 0, column=1)

            password_log_in_label = tk.Label(current_frame_auth, text="PASSWORD: ", bg="#87CEEB", fg="black")
            password_log_in_label.grid(row = 1, column=0)

            password_log_in_entry = tk.Entry(current_frame_auth, bg="#87CEEB", fg="black", bd=0, highlightthickness = 1, show = '*')
            password_log_in_entry.grid(row = 1, column=1)

            sign_up_button = tk.Button(current_frame_auth, text="SIGN UP", bg="white",fg="black", activebackground="white", activeforeground="black",borderwidth=0, highlightthickness=0,highlightbackground="white", relief="flat", padx=10, pady=4, cursor="hand2")
            sign_up_button.grid(row = 2, column= 0)

    log_in_button_auth_form = tk.Button(auth,text="LOG IN",command=log_in_function,bg="white",fg="black",activebackground="white",activeforeground="black",highlightbackground="#87CEEB",highlightthickness="0",padx=10, pady=4, cursor="hand2")
    log_in_button_auth_form.place(x = 180,y= 150)

    sign_up_button_auth_form = tk.Button(auth,text="SIGN UP",command=sign_up_function,bg="white",fg="black",activebackground="white",activeforeground="black",highlightbackground="#87CEEB",highlightthickness="0",padx=10, pady=4, cursor="hand2")
    sign_up_button_auth_form.place(x = 320,y= 150)



    auth.mainloop()

authentication()