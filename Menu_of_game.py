from tkinter import *
from tkinter.font import BOLD
import New_Game
import game_controll
import Change_color



def menu_of_game(jezik,p1color,p2color,p1_up,p1_down,p2_up,p2_down):                         # Novi prozor kada se klikne dugme srpski ili engleski jezik

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

    def start_new_game():
        menu_game.destroy()
        New_Game.game(jezik,p1color,p2color,p1_up,p1_down,p2_up,p2_down)

    def change_controll():
        menu_game.destroy()
        game_controll.Menu_controll(jezik,p1color,p2color,p1_up,p1_down,p2_up,p2_down)

    def change_color():
        menu_game.destroy()
        Change_color.Map_Color(jezik,p1color,p2color,p1_up,p1_down,p2_up,p2_down)

    menu_game = Tk ()


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

    menu_game.geometry("600x600")                  # Velicina prozora
    menu_game.title(main_text)                # Ime prozora
    menu_game.resizable(False, False)

    icon = PhotoImage(file="Icon.png")          # Slika je prebacena u format koji moze da cita python
    menu_game.iconphoto(True, icon)                # Ikonica prozora

    menu_game.config(bg="black")           # Boja pozadine prozora

    naslov = Label(menu_game, 
                    text=main_text, 
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

    con = buttonb(kontrole, change_controll)
    controll = con.create_button()         #Kreirano dugme za promene kontole

    col = buttonb(boje, change_color)
    colorr = col.create_button()          #Kreirano dugme za promenu boje igraca

    s_g = buttonb(Pokreni_igricu, start_new_game)
    start_game = s_g.create_button()  #Kreirano dugme za pokretanje igrice

    copyright = Label(menu_game, 
                    text=copyright_text, 
                    font=("Arial", 10), 
                    fg="red", 
                    bg="black")                # Informacija na dnu stranice ko je napravio igricu

    naslov.pack(pady=50)                       # Dugme je ubaceno u prozor
    controll.pack(pady=10)
    colorr.pack(pady=10)
    start_game.pack(pady=10)

    copyright.pack(side="bottom")              # Informacija na dnu je ubacena u prozor