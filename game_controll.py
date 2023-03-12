from tkinter import *
from tkinter.font import BOLD
import Menu_of_game
import Player_One_up
import Player_One_down
import Player_Two_up
import Player_Two_down



def Menu_controll(jezik,p1color,p2color,p1_up,p1_down,p2_up,p2_down):    # Novi prozor kada se klikne dugme srpski ili engleski jezik

    class buttonb(object):
        def __init__(self, d_text, d_command):
            self.d_text = d_text
            self.d_command = d_command
            
        def create_button (self):
            s_f = Button(menu_controll, 
                    text=self.d_text, 
                    font=("Arial", 12, BOLD), 
                    fg="red", 
                    bg="black",
                    activeforeground="red",
                    activebackground="black",  
                    relief=RAISED, 
                    bd=10, 
                    command=self.d_command )
            return (s_f)

    def start_new_game():
        menu_controll.destroy()
        Menu_of_game.menu_of_game(jezik,p1color,p2color,p1_up,p1_down,p2_up,p2_down)

    def player_1_up():
        menu_controll.destroy()
        Player_One_up.Map_Button(jezik,p1color,p2color,p1_up,p1_down,p2_up,p2_down)

    def player_1_down():
        menu_controll.destroy()
        Player_One_down.Map_Button(jezik,p1color,p2color,p1_up,p1_down,p2_up,p2_down)

    def player_2_up():
        menu_controll.destroy()
        Player_Two_up.Map_Button(jezik,p1color,p2color,p1_up,p1_down,p2_up,p2_down)

    def player_2_down():
        menu_controll.destroy()
        Player_Two_down.Map_Button(jezik,p1color,p2color,p1_up,p1_down,p2_up,p2_down)

    menu_controll = Tk ()

    

    if jezik == "serbian":
        main_text = "Podešavanje Kontrole"
        p1up = "Kontrola za igrača Micu nagore je: "
        p1down = "Kontrola za igrača Micu nadole je: "
        p2up = "Kontrola za igrača Bicu nagore je: "
        p2down = "Kontrola za igrača Bicu nadole je: "
        save_change = "Sačuvaj"
        copyright_text = "Igricu napravio Velicki"

    elif jezik == "english":
        main_text = "Controll Setup"
        p1up = "Player Mica - controll for Up is: "
        p1down = "Player Mica - controll for Down is: "
        p2up = "Player Bica - controll for Up is: "
        p2down = "Player Bica - controll for Down is: "
        save_change = "Save"
        copyright_text = "copyright by Velicki"

    menu_controll.geometry("600x600")                  # Velicina prozora
    menu_controll.title("change_game_controll")        # Ime prozora
    menu_controll.resizable(False, False)

    icon = PhotoImage(file="Icon.png")       # Slika je prebacena u format koji moze da cita python
    menu_controll.iconphoto(True, icon)      # Ikonica prozora

    menu_controll.config(bg="black")         # Boja pozadine prozora

    naslov = Label(menu_controll, 
                    text=main_text, 
                    font=("Arial", 40, BOLD), 
                    fg="red", 
                    bg="black",
                    activeforeground="red",
                    activebackground="black",  
                    relief=RAISED, 
                    bd=10)                   #Napravljen i dekorisan naslov

    p_1_u = buttonb(p1up+p1_up, player_1_up)
    player1up = p_1_u.create_button()        #napravljeno dugme za igraca Micu - gore

    p_1_d = buttonb(p1down+p1_down, player_1_down)
    player1down = p_1_d.create_button()      #napravljeno dugme za igraca Micu - dole

    p_2_u = buttonb(p2up+p2_up, player_2_up)
    player2up = p_2_u.create_button()        #napravljeno dugme za igraca Bicu - gore

    p_2_d = buttonb(p2down+p2_down, player_2_down)
    player2down = p_2_d.create_button()        #napravljeno dugme za igraca Bicu - dole


    s_c = buttonb(save_change, start_new_game)
    save_change_button = s_c.create_button()  #Kreirano dugme za cuvanje promena

    copyright = Label(menu_controll, 
                    text=copyright_text, 
                    font=("Arial", 10), 
                    fg="red", 
                    bg="black")                # Informacija na dnu stranice ko je napravio igricu

    naslov.pack(pady=50)                       # Dugme je ubaceno u prozor

    player1up.pack(pady=5)
    player1down.pack(pady=5)
    player2up.pack(pady=5)
    player2down.pack(pady=5)

    save_change_button.pack(pady=10)

    copyright.pack(side="bottom")              # Informacija na dnu je ubacena u prozor