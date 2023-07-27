import customtkinter

customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Focus application")
root.geometry("700x500")



def sideframe2_clock():
    side_frame2 = customtkinter.CTkFrame(master = frame, fg_color = "#E3E3E3") 
    side_frame2.pack(padx = 10, pady = 10, fill ="both", expand = True)

    for widgets in side_frame2.winfo_children():# to clear the frame
        widgets.destroy()


    analog_canvas = tk.Canvas(side_frame2,width = 400, height = 400, bg = 'grey') # '#E3E3E3' color
    analog_canvas.pack()

    digital_canvas = tk.Canvas(side_frame2, width = 400, height =100, bg = "#E3E3E3")
    digital_canvas.pack()

def sideframe2_timer():
    side_frame2 = customtkinter.CTkFrame(master = frame, fg_color = "#E3E3E3") 
    side_frame2.pack(padx = 10, pady = 10, fill ="both", expand = True)


    analog_canvas = tk.Canvas(side_frame2,width = 400, height = 400, bg = 'red') # '#E3E3E3' color
    analog_canvas.pack()

    digital_canvas = tk.Canvas(side_frame2, width = 400, height =100, bg = "red")
    digital_canvas.pack()





def main_app():
"""
    if username == "" and password == "": #  set userid and passworrd later
        for widgets in frame.winfo_children():# to clear the frame
            widgets.destroy()
"""

    side_frame = customtkinter.CTkFrame(master = frame, fg_color= "#D0F4FF") # this is a bad way to crate a side frame things will go wrong when we resize the window
    side_frame.pack(side = customtkinter.LEFT)
    side_frame.pack_propagate(False)
    side_frame.configure(width = 250, height = 1000)

    label = customtkinter.CTkLabel(master= side_frame, text = "" )
    label.pack(pady = 20)

    focus_button = customtkinter.CTkButton(master = side_frame, 
                                   text = "Focus session", 
                                    font = ("Arial", 20),
                                   fg_color = '#D0F4FF', 
                                   text_color= 'black', 
                                       width = 250,
                                       height = 60,
                                       hover_color = "#9BB5BD",
                                       #command= sideframe2_timer
                                       )
        focus_button.pack()
                                       
        
        clock_button = customtkinter.CTkButton(master= side_frame, 
                                       text = "Clock", 
                                       font = ("Arial", 20),
                                       fg_color = '#D0F4FF', 
                                       text_color= 'black', 
                                       width = 250,
                                       height = 60,
                                       hover_color = "#9BB5BD",
                                       #command= sideframe2_clock
                                       )
        clock_button.pack()

        # this is where switch frame are being crated
        sideframe_clock = frame(frame)
        sideframe_timer = frame(frame)

        sideframe_clock.grid(row = 0, cloumn = 0)
        sideframe_timer.grid(row = 0, cloumn = 0)

        lbl = label(sideframe_clock, text = "Yo loo")
        lbl.pack(pady = 20)

        lbl = label(sideframe_timer, text = "Yo loo111111")
        lbl.pack(pady = 20)
        

        sideframe_clock.tkraise()





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
