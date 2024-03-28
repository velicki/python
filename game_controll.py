from tkinter import *
from tkinter.font import BOLD
import Menu_of_game
import Player_One_up
import Player_One_down
import Player_Two_up
import Player_Two_down

#-----------------------------------------------

def Menu_controll(jezik,p1color,p2color,p1_up,p1_down,p2_up,p2_down):

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

#-----------------------------------------------

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
    
    def chosen_language(jezik):
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
        
        return (main_text,p1up,p1down,p2up,p2down,save_change,copyright_text)
    
    def windows_configuration():
        menu_controll.geometry("600x600")
        menu_controll.title(chosen_language(jezik)[0])
        menu_controll.resizable(False, False)
        icon = PhotoImage(file="Icon.png")
        menu_controll.iconphoto(True, icon)
        menu_controll.config(bg="black")
    
    def naslov():
        naslov = Label(menu_controll, 
                    text=chosen_language(jezik)[0], 
                    font=("Arial", 40, BOLD), 
                    fg="red", 
                    bg="black",
                    activeforeground="red",
                    activebackground="black",  
                    relief=RAISED, 
                    bd=10)
        return naslov
    
    def copyright():
        copyright = Label(menu_controll, 
                    text=chosen_language(jezik)[6], 
                    font=("Arial", 10), 
                    fg="red", 
                    bg="black")
        return copyright

#-----------------------------------------------

    menu_controll = Tk ()


    windows_configuration()


    p_1_u = buttonb(chosen_language(jezik)[1]+p1_up, player_1_up)

    p_1_d = buttonb(chosen_language(jezik)[2]+p1_down, player_1_down)

    p_2_u = buttonb(chosen_language(jezik)[3]+p2_up, player_2_up)

    p_2_d = buttonb(chosen_language(jezik)[4]+p2_down, player_2_down)

    s_c = buttonb(chosen_language(jezik)[5], start_new_game)

#-----------------------------------------------

    naslov().pack(pady=50)
    p_1_u.create_button().pack(pady=5)
    p_1_d.create_button().pack(pady=5)
    p_2_u.create_button().pack(pady=5)
    p_2_d.create_button().pack(pady=5)
    s_c.create_button().pack(pady=10)
    copyright().pack(side="bottom")