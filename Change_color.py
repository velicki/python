from tkinter import *
from tkinter.font import BOLD
from tkinter import colorchooser
import Menu_of_game
import Change_color

#-----------------------------------------------

def Map_Color(jezik,p1color,p2color,p1_up,p1_down,p2_up,p2_down):                         # Novi prozor kada se klikne dugme srpski ili engleski jezik

#-----------------------------------------------

    class buttonb(object):
        def __init__(self, d_text, bg_c, d_command):
            self.d_text = d_text
            self.bg_c = bg_c
            self.d_command = d_command
            
        def create_button(self):
            s_f = Button(menu_controll, 
                    text=self.d_text, 
                    font=("Arial", 12, BOLD), 
                    fg="red", 
                    bg=self.bg_c,
                    activeforeground="red",
                    activebackground="black",  
                    relief=RAISED, 
                    bd=10, 
                    command=self.d_command )
            return(s_f)

#-----------------------------------------------

    def player_one_color():
        color1 = colorchooser.askcolor()
        p1color = color1[1]
        menu_controll.destroy()
        Change_color.Map_Color(jezik,p1color,p2color,p1_up,p1_down,p2_up,p2_down)
        

    def player_two_color():
        color2 = colorchooser.askcolor()
        p2color = color2[1]
        menu_controll.destroy()
        Change_color.Map_Color(jezik,p1color,p2color,p1_up,p1_down,p2_up,p2_down)
        
    def save():
        menu_controll.destroy()
        Menu_of_game.menu_of_game(jezik,p1color,p2color,p1_up,p1_down,p2_up,p2_down)    

    def chosen_language(jezik):
        if jezik == "serbian":
            main_text = "Promeni boje igračima!"
            p1uptext = "izaberi boju za Micu"
            p2uptext = "izaberi boju za Bicu"
            SaveColor = "Sačuvaj promenu"
            copyright_text = "Igricu napravio Velicki"

        elif jezik == "english":
            main_text = "Change Players color"
            p1uptext = "Choose a color for Mica"
            p2uptext = "Choose a color for Bica"
            SaveColor = "Save Change"
            copyright_text = "copyright by Velicki"
        return (main_text,p1uptext,p2uptext,SaveColor,copyright_text)

    def windows_configuration():
        menu_controll.geometry("600x600")                  # Velicina prozora
        menu_controll.title(chosen_language(jezik)[0])                # Ime prozora
        menu_controll.resizable(False, False)
        icon = PhotoImage(file="Icon.png")          # Slika je prebacena u format koji moze da cita python
        menu_controll.iconphoto(True, icon)                # Ikonica prozora
        menu_controll.config(bg="black")           # Boja pozadine prozora

    def naslov():
        naslov = Label(menu_controll, 
                    text=chosen_language(jezik)[0], 
                    font=("Arial", 20, BOLD), 
                    fg="red", 
                    bg="black",
                    activeforeground="red",
                    activebackground="black",  
                    relief=RAISED, 
                    bd=10)             #Napravljen i dekorisan naslov
        return naslov

    def copyright():
        copyright = Label(menu_controll, 
                    text=chosen_language(jezik)[4], 
                    font=("Arial", 10), 
                    fg="red", 
                    bg="black")                # Informacija na dnu stranice ko je napravio igricu
        return copyright

#-----------------------------------------------

    menu_controll = Tk ()

    windows_configuration()

    p_1_c = buttonb(chosen_language(jezik)[1], p1color, player_one_color)   #napravljeno dugme za igraca Micu - promena boje igraca

    p_2_c = buttonb(chosen_language(jezik)[2], p2color, player_two_color)   #napravljeno dugme za igraca Bicu - promena boje igraca

    s_c = buttonb(chosen_language(jezik)[3], "black", save)                 #napravljeno dugme za cuvanje promena - SAVE

#-----------------------------------------------

    naslov().pack(pady=40)                       # Dugme je ubaceno u prozor
    p_1_c.create_button().pack(pady=20)
    p_2_c.create_button().pack(pady=20)
    s_c.create_button().pack(pady=20)
    copyright().pack(side="bottom")              # Informacija na dnu je ubacena u prozor