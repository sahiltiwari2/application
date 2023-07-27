import customtkinter
import tkinter as tk
import time
import math

customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Focus application")
root.geometry("700x500")

global username_input
global password_input






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




frame = customtkinter.CTkFrame(master = root)
frame.pack(padx = 20, pady = 20, fill = "both", expand = True)


main_app()
root.mainloop()