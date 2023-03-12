from tkinter import *
from tkinter.font import BOLD
import New_Game
import game_controll
import Change_color


def menu_of_game(jezik,p1color,p2color,p1_up,p1_down,p2_up,p2_down):                         # Novi prozor kada se klikne dugme srpski ili engleski jezik

#-----------------------------------------------

    class buttonb(object):
        def __init__(self, d_text, d_command):
            self.d_text = d_text
            self.d_command = d_command
            
        def create_button (self):
            s_f = Button(menu_game, 
                        text=self.d_text,
                        font=("Arial", 20, BOLD), 
                        fg="red", 
                        bg="black",
                        activeforeground="red",
                        activebackground="black",  
                        relief=RAISED, 
                        bd=10,
                        command=self.d_command )
            return (s_f)

#-----------------------------------------------

    def start_new_game():
        menu_game.destroy()
        New_Game.game(jezik,p1color,p2color,p1_up,p1_down,p2_up,p2_down)

    def change_controll():
        menu_game.destroy()
        game_controll.Menu_controll(jezik,p1color,p2color,p1_up,p1_down,p2_up,p2_down)

    def change_color():
        menu_game.destroy()
        Change_color.Map_Color(jezik,p1color,p2color,p1_up,p1_down,p2_up,p2_down)

    def chosen_language(jezik):
        if jezik == "serbian":
            main_text = "Mica protiv Bice!!!"
            copyright_text = "Igricu napravio Velicki"
            kontrole = "podesi kontrole"
            boje = "podesi boje igrača"
            Pokreni_igricu = "Pokreni igricu"

        elif jezik == "english":
            main_text = "Mica VS Bica!!!"
            copyright_text = "copyright by Velicki"
            kontrole = "game controll"
            boje = "player color"
            Pokreni_igricu = "START GAME"

        return (main_text,copyright_text,kontrole,boje,Pokreni_igricu)
    
    def windows_configuration():
        menu_game.geometry("600x600")                  # Velicina prozora
        menu_game.title(chosen_language(jezik)[0])                # Ime prozora
        menu_game.resizable(False, False)
        icon = PhotoImage(file="Icon.png")          # Slika je prebacena u format koji moze da cita python
        menu_game.iconphoto(True, icon)                # Ikonica prozora
        menu_game.config(bg="black")

    def naslov():
        naslov = Label(menu_game, 
                    text=chosen_language(jezik)[0], 
                    font=("Arial", 40, BOLD), 
                    fg="red", 
                    bg="black",
                    activeforeground="red",
                    activebackground="black",  
                    relief=RAISED, 
                    bd=10 
                    #pady=10, 
                    #padx=10, 
                    )             #Napravljen i dekorisan naslov
        return naslov

    def copyright():
        copyright = Label(menu_game, 
                        text=chosen_language(jezik)[1], 
                        font=("Arial", 10), 
                        fg="red", 
                        bg="black")                # Informacija na dnu stranice ko je napravio igricu
        return copyright

#-----------------------------------------------

    menu_game = Tk ()


    windows_configuration()

#-----------------------------------------------

    con = buttonb(chosen_language(jezik)[2], change_controll)  #Kreirano dugme za promene kontole

    col = buttonb(chosen_language(jezik)[3], change_color)     #Kreirano dugme za promenu boje igraca

    s_g = buttonb(chosen_language(jezik)[4], start_new_game)   #Kreirano dugme za pokretanje igrice

#-----------------------------------------------

    naslov().pack(pady=50)                       # Dugme je ubaceno u prozor
    con.create_button().pack(pady=10)
    col.create_button().pack(pady=10)
    s_g.create_button().pack(pady=10)
    copyright().pack(side="bottom")              # Informacija na dnu je ubacena u prozor