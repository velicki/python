from tkinter import *
from tkinter.font import BOLD
import game_controll



def Map_Button(jezik,p1color,p2color,p1_up,p1_down,p2_up,p2_down):          # Novi prozor kada se klikne dugme srpski ili engleski jezik

    def start_new_game(event):
        if (event.keysym != p1_down and event.keysym != p2_up and event.keysym != p2_down):
            p1_up = event.keysym
        else: p1_up = pokret
        menu_controll.destroy()
        game_controll.Menu_controll(jezik,p1color,p2color,p1_up,p1_down,p2_up,p2_down)


    menu_controll = Tk ()

    pokret = p1_up

    if jezik == "serbian":
        main_text = "Mico klikni dugme za gore!"
        copyright_text = "Igricu napravio Velicki"

    elif jezik == "english":
        main_text = "Mica press button for up"
        copyright_text = "copyright by Velicki"

    menu_controll.geometry("600x600")                  # Velicina prozora
    menu_controll.title("change_game_controll")                # Ime prozora
    menu_controll.resizable(False, False)

    icon = PhotoImage(file="Icon.png")          # Slika je prebacena u format koji moze da cita python
    menu_controll.iconphoto(True, icon)                # Ikonica prozora

    menu_controll.config(bg="black")           # Boja pozadine prozora

    menu_controll.bind("<Key>",start_new_game)   #ova komanda prihvata karakter sa tastature

    naslov = Label(menu_controll, 
                    text=main_text, 
                    font=("Arial", 20, BOLD), 
                    fg="red", 
                    bg="black",
                    activeforeground="red",
                    activebackground="black",  
                    relief=RAISED, 
                    bd=10 
                    #pady=10, 
                    #padx=10, 
                    )             #Napravljen i dekorisan naslov

    copyright = Label(menu_controll, 
                    text=copyright_text, 
                    font=("Arial", 10), 
                    fg="red", 
                    bg="black")                # Informacija na dnu stranice ko je napravio igricu

    naslov.pack(pady=150)                      # Dugme je ubaceno u prozor

    copyright.pack(side="bottom")              # Informacija na dnu je ubacena u prozor