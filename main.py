import tkinter as tk
import customtkinter as ctk

root = tk.Tk()
root.geometry("700x500")
root.title("Focus Application")

def focus_page():
    focus_frame = tk.Frame(main_frame)
    focus_frame.pack(pady = 20)

    label = ctk.CTkLabel(focus_frame, text = "this is focus frame")
    label.pack()

def clock_page():
    clock_frame = tk.Frame(main_frame)
    clock_frame.pack(pady = 20)

    label = ctk.CTkLabel(clock_frame, text = "this is clock frame")
    label.pack()

def about_page():
    about_frame = tk.Frame(main_frame)
    about_frame.pack(pady = 20)

    label = ctk.CTkLabel(about_frame, text = "this is about frame")
    label.pack()

def github_page():
    github_frame = tk.Frame(main_frame)
    github_frame.pack(pady = 20)

    label = ctk.CTkLabel(github_frame, text = "this is github frame")
    label.pack()

def clear_frame():
   for widgets in main_frame.winfo_children():
      widgets.destroy()

def hide_selectors():
    focus_button.configure(border_width = 0, fg_color = "#DAF9FF")
    clock_button.configure(border_width = 0, fg_color = "#DAF9FF")
    about_button.configure(border_width = 0, fg_color = "#DAF9FF")
    github_button.configure(border_width = 0, fg_color = "#DAF9FF")

    focus_indicate.config(bg = "#DAF9FF")
    clock_indicate.config(bg = "#DAF9FF")
    about_indicate.config(bg = "#DAF9FF")
    github_indicate.config(bg = "#DAF9FF")



def selector(button, label, page):
    hide_selectors()
    label.config(bg = "black")
    button.configure(border_width = 2, fg_color = "#D9D9D9")
    clear_frame()
    page()

# this is the side frame 
side_panel = tk.Frame(root, background = "#DAF9FF")
side_panel.pack(side = tk.LEFT)
side_panel.pack_propagate(False)
side_panel.configure(width = 200, height = 500)


focus_button = ctk.CTkButton(side_panel, text = "Focus timer", fg_color =  "transparent", text_color = "black", hover_color = "#E3E3E3", corner_radius = 2, font= ("Bold", 20), height= 40, border_color = "Black", border_width = 0, command =lambda: selector(focus_button,focus_indicate, focus_page))
focus_button.place(x = 30, y = 50)

focus_indicate = tk.Label(side_panel, text = "", bg = "#DAF9FF")
focus_indicate.place(x = 22, y = 50, height = 40)

clock_button = ctk.CTkButton(side_panel, text = "Clock", fg_color =  "transparent", text_color = "black", hover_color = "#E3E3E3", corner_radius = 2, font= ("Bold", 20), height = 40, border_color = "Black", border_width = 0, command =lambda: selector(clock_button,clock_indicate, clock_page))
clock_button.place(x = 30, y = 100)

clock_indicate = tk.Label(side_panel, text = "", bg = "#DAF9FF")
clock_indicate.place(x = 22, y = 100, height = 40)

about_button = ctk.CTkButton(side_panel, text = "About Us", fg_color =  "transparent", text_color = "black", hover_color = "#E3E3E3", corner_radius = 2, font= ("Bold", 20), height = 40, border_color = "Black", border_width = 0, command =lambda: selector(about_button,about_indicate, about_page))
about_button.place(x = 30, y = 150)

about_indicate = tk.Label(side_panel, text = "", bg = "#DAF9FF")
about_indicate.place(x = 22, y = 150, height = 40)

github_button = ctk.CTkButton(side_panel, text = "Git hub", fg_color =  "transparent", text_color = "black", hover_color = "#E3E3E3", corner_radius = 2, font= ("Bold", 20), height = 40, border_color = "Black", border_width = 0, command =lambda: selector(github_button,github_indicate, github_page))
github_button.place(x = 30, y = 425)

github_indicate = tk.Label(side_panel, text = "", bg = "#DAF9FF")
github_indicate.place(x = 22, y = 425, height = 40)

# this is the main frame
main_frame = tk.Frame(root, background = "#EDEDED", highlightbackground = "#D8E3FF", highlightthickness = 2)
main_frame.pack(side = tk.LEFT)
main_frame.propagate(False)
main_frame.configure(width = 500, height = 500)



root.mainloop()
