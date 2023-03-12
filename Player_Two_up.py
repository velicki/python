from tkinter import *
from tkinter.font import BOLD
import game_controll

#-----------------------------------------------

def Map_Button(jezik,p1color,p2color,p1_up,p1_down,p2_up,p2_down):      # Novi prozor kada se klikne dugme srpski ili engleski jezik

#-----------------------------------------------

    def start_new_game(event):
        if (event.keysym != p1_down and event.keysym != p2_down and event.keysym != p1_up):
            p2_up = event.keysym
        else: p2_up = pokret
        menu_controll.destroy()
        game_controll.Menu_controll(jezik,p1color,p2color,p1_up,p1_down,p2_up,p2_down)

    def chosen_language(jezik):
        if jezik == "serbian":
            main_text = "Bico klikni dugme za dole!"
            copyright_text = "Igricu napravio Velicki"

        elif jezik == "english":
            main_text = "Bica press button for down"
            copyright_text = "copyright by Velicki"

        return (main_text,copyright_text)

    def windows_configuration():
        menu_controll.geometry("600x600")                  # Velicina prozora
        menu_controll.title(chosen_language(jezik)[0])     # Ime prozora
        menu_controll.resizable(False, False)
        icon = PhotoImage(file="Icon.png")                 # Slika je prebacena u format koji moze da cita python
        menu_controll.iconphoto(True, icon)                # Ikonica prozora
        menu_controll.config(bg="black")                   # Boja pozadine prozora

    def naslov():
        naslov = Label(menu_controll, 
                    text=chosen_language(jezik)[0], 
                    font=("Arial", 20, BOLD), 
                    fg="red", 
                    bg="black",
                    activeforeground="red",
                    activebackground="black",  
                    relief=RAISED, 
                    bd=10)                    #Napravljen i dekorisan naslov
        return naslov

    def copyright():
        copyright = Label(menu_controll, 
                    text=chosen_language(jezik)[1], 
                    font=("Arial", 10), 
                    fg="red", 
                    bg="black")                # Informacija na dnu stranice ko je napravio igricu
        return copyright

#-----------------------------------------------

    menu_controll = Tk ()

    pokret = p2_up

    windows_configuration()

    menu_controll.bind("<Key>",start_new_game)   #ova komanda prihvata karakter sa tastature

#-----------------------------------------------

    naslov().pack(pady=150)                       # Dugme je ubaceno u prozor
    copyright().pack(side="bottom")               # Informacija na dnu je ubacena u prozor