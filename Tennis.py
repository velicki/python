from tkinter import *
from tkinter.font import BOLD
import Menu_of_game

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
                compound="left", command= self.d_command)
        return (s_f)


def clicked_serbian():
    jezik = "serbian"
    p1color = "red"
    p2color = "blue"
    window.destroy()
    Menu_of_game.menu_of_game(jezik,p1color,p2color,p1_up,p1_down,p2_up,p2_down)
    

def clicked_english():
    jezik = "english"
    p1color = "red"
    p2color = "blue"
    window.destroy()
    Menu_of_game.menu_of_game(jezik,p1color,p2color,p1_up,p1_down,p2_up,p2_down)
    


window = Tk ()                                # inicializiran prozor

p2_up = "Up"
p2_down = "Down"
p1_up = "w"
p1_down = "s"

window.geometry("600x600")                     # Velicina prozora
window.title("Mica VS Bica")                   # Ime prozora
window.resizable(False, False)


icon = PhotoImage(file="Icon.png")             # Slika je prebacena u format koji moze da cita python
window.iconphoto(True, icon)                   # Ikonica prozora

window.config(bg="black")                      # Boja pozadine prozora

Serbian_Flag = PhotoImage(file="SerbianFlag.png")
English_Flag = PhotoImage(file="EnglishFlag.png")


s_f_b = buttonb("SRPSKI", Serbian_Flag, clicked_serbian)
serbian_flag = s_f_b.create_button()            # Napravljeno i dekorisano je dugme srpski jezikj

e_f_b = buttonb("ENGLISH", English_Flag, clicked_english)
english_flag = e_f_b.create_button()            # Napravljeno i dekorisano je dugme engleski jezik

copyright = Label(window, 
                text="copyright by Velicki", 
                font=("Arial", 10), 
                fg="red", 
                bg="black")                      # Informacija na dnu stranice ko je napravio igricu


serbian_flag.pack(pady=50)                       # Dugme za Srpski je ubaceno u prozor
english_flag.pack(pady=50)                       # Dugme za Engleski je ubaceno u prozor
copyright.pack(side="bottom")                    # Informacija na dnu je ubacena u prozor

window.mainloop()                                # kraj inicializiranog prozora