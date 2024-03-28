from tkinter import *
from tkinter.font import BOLD
import Menu_of_game

#-----------------------------------------------

class buttonb(object):
    def __init__(self, d_text, d_Serbian_Flag, d_command):
        self.d_Serbian_Flag = d_Serbian_Flag
        self.d_text = d_text
        self.d_command = d_command
        
    def create_button (self):
        s_f = Button(window, 
                text= self.d_text, 
                font=("Arial", 40, BOLD), 
                fg="red", 
                bg="black",
                activeforeground="red",
                activebackground="black",  
                relief=RAISED, 
                bd=10, 
                #pady=10, 
                #padx=10, 
                image= self.d_Serbian_Flag, 
                compound="left",
                command= self.d_command)
        return (s_f)

#-----------------------------------------------

def windows_configuration():
    window.geometry("600x600")
    window.title("Mica VS Bica")
    window.resizable(False, False)
    window.iconphoto(True, PhotoImage(file="Icon.png"))
    window.config(bg="black")

def setup_defoult_controlls():
    p2_up = "Up"
    p2_down = "Down"
    p1_up = "w"
    p1_down = "s"
    p1color = "red"
    p2color = "blue"
    return (p1_up,p1_down,p2_up,p2_down,p1color,p2color)

def clicked_serbian():
    jezik = "serbian"
    x = setup_defoult_controlls()
    window.destroy()
    Menu_of_game.menu_of_game(jezik,x[4],x[5],x[0],x[1],x[2],x[3])
    

def clicked_english():
    jezik = "english"
    x = setup_defoult_controlls()
    window.destroy()
    Menu_of_game.menu_of_game(jezik,x[4],x[5],x[0],x[1],x[2],x[3])

def copyright():
    copyright = Label(window, 
                text="copyright by Velicki", 
                font=("Arial", 10), 
                fg="red", 
                bg="black")
    return copyright

#-----------------------------------------------

window = Tk ()

windows_configuration()

#-----------------------------------------------

s_f_b = buttonb("SRPSKI", PhotoImage(file="SerbianFlag.png"), clicked_serbian)

e_f_b = buttonb("ENGLISH", PhotoImage(file="EnglishFlag.png"), clicked_english)

#-----------------------------------------------

s_f_b.create_button().pack(pady=50)
e_f_b.create_button().pack(pady=50)
copyright().pack(side="bottom")

#-----------------------------------------------

window.mainloop()