import customtkinter
import tkinter as tk
import time
import math

customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme("dark-blue")


class FocusFrame(customtkinter.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)

        label1 = customtkinter.CTkLabel(master=self, text="Abe sale", text_color='black', font=("Arial", 20))
        label1.pack(pady=20)

        clock_button = customtkinter.CTkButton(
            master=self,
            text="Clock",
            font=("Arial", 20),
            fg_color='#D0F4FF',
            text_color='black',
            width=250,
            height=60,
            hover_color="#9BB5BD",
            # command=sideframe2_clock
        )
        clock_button.pack()
class Appliaction(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Focus application")
        self.geometry("1080x900")
        frame = customtkinter.CTkFrame(master=self)
        frame.pack(padx=20, pady=20, fill="both", expand=True)
        self.main_app(frame)

    def main_app(self, frame):
        self.side_frame = customtkinter.CTkFrame(master=frame, fg_color="#D0F4FF") 
        self.side_frame.pack(side=customtkinter.LEFT)
        self.side_frame.pack_propagate(False)
        self.side_frame.configure(width=250, height=1000)

        label = customtkinter.CTkLabel(master=self.side_frame, text="")
        label.pack(pady=20)

        focus_button = customtkinter.CTkButton(
            master=self.side_frame, 
            text="Focus session", 
            font=("Arial", 20),
            fg_color='#D0F4FF', 
            text_color='black', 
            width=250,
            height=60,
            hover_color="#9BB5BD",
            command=self.show_focus_frame
        )
        focus_button.pack()

        clock_button = customtkinter.CTkButton(
            master=self.side_frame, 
            text="Clock", 
            font=("Arial", 20),
            fg_color='#D0F4FF', 
            text_color='black', 
            width=250,
            height=60,
            hover_color="#9BB5BD",
            #command=sideframe2_clock
        )
        clock_button.pack()

    def show_focus_frame(self):
        for widget in self.side_frame.winfo_children():
            widget.destroy()
        focus_frame=FocusFrame(master=self.side_frame)
        focus_frame.pack()

if __name__ == "__main__":
    app = Appliaction()
    app.mainloop()
