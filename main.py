import customtkinter

customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Focus application")
root.geometry("700x500")

login = False
global username_input
global password_input




def main_app():
    username = username_input.get() # gets the text in the box named username_input
    password = password_input.get()
    if username == "" and password == "": #  set userid and passworrd later
        for widgets in frame.winfo_children():# to clear the frame
            widgets.destroy()

        side_frame = customtkinter.CTkFrame(master = frame, fg_color= "#D0F4FF") # this is a bad way to crate a side frame things will go wrong when we resize the window
        side_frame.pack(side = customtkinter.LEFT)
        side_frame.pack_propagate(False)
        side_frame.configure(width = 250, height = 1000)

        label = customtkinter.CTkLabel(master= side_frame, text = "" )
        label.pack(pady = 20)

        main_button = customtkinter.CTkButton(master= side_frame, 
                                       text = "Focus session", 
                                       font = ("Arial", 20),
                                       fg_color = '#D0F4FF', 
                                       text_color= 'black', 
                                       width = 250,
                                       height = 60,
                                       hover_color = "#9BB5BD",
                                       )
        main_button.pack()




        side_frame2 = customtkinter.CTkFrame(master = frame) # this is a bad way to crate a side frame things will go wrong when we resize the window
        side_frame2.pack(padx = 10, pady = 10, fill ="both", expand = True)



    else:
        print("Invalid Password")


frame = customtkinter.CTkFrame(master = root)
frame.pack(padx = 20, pady = 20, fill = "both", expand = True)

label = customtkinter.CTkLabel(master= frame, text = "Login System")
label.pack(pady = 12, padx = 10)

username_input = customtkinter.CTkEntry(master = frame, placeholder_text="Username")
username_input.pack(pady = 12, padx = 10)

password_input = customtkinter.CTkEntry(master = frame, placeholder_text="Password", show = "*")
password_input.pack(pady = 12, padx = 10)

login_button = customtkinter.CTkButton(master = frame, text = "Login", command = main_app)
login_button.pack(pady = 10, padx = 6)

remember_checkbox = customtkinter.CTkCheckBox(master = frame, text = "Rember me")
remember_checkbox.pack(pady = 5, padx = 5)

main_frame = customtkinter.CTkFrame(master = root)
frame.pack(padx = 20, pady = 20, fill = "both", expand = True)

label = customtkinter.CTkLabel(master= main_frame, text = "Login System")
label.pack(pady = 12, padx = 10)



root.mainloop()