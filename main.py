import customtkinter
import tkinter as tk
import time
import math

customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme("dark-blue")




class Appliaction(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Focus application")
        self.geometry("1080x900")
        frame = customtkinter.CTkFrame(master = self)
        frame.pack(padx = 20, pady = 20, fill = "both", expand = True)
        self.main_app(frame)






    def main_app(self, frame):


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




if __name__=="__main__":

    app = Appliaction()
    app.mainloop()