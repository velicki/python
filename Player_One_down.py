from tkinter import *
from tkinter.font import BOLD
import game_controll

#-----------------------------------------------

def Map_Button(jezik,p1color,p2color,p1_up,p1_down,p2_up,p2_down):

#-----------------------------------------------

    def start_new_game(event):
        if (event.keysym != p2_up and event.keysym != p2_down and event.keysym != p1_up):
            p1_down = event.keysym
        else: p1_down = pokret
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
        menu_controll.geometry("600x600")
        menu_controll.title(chosen_language(jezik)[0])
        menu_controll.resizable(False, False)
        icon = PhotoImage(file="Icon.png")
        menu_controll.iconphoto(True, icon)
        menu_controll.config(bg="black")

    def naslov():
        naslov = Label(menu_controll, 
                    text=chosen_language(jezik)[0], 
                    font=("Arial", 20, BOLD), 
                    fg="red", 
                    bg="black",
                    activeforeground="red",
                    activebackground="black",  
                    relief=RAISED, 
                    bd=10)
        return naslov

    def copyright():
        copyright = Label(menu_controll, 
                    text=chosen_language(jezik)[1], 
                    font=("Arial", 10), 
                    fg="red", 
                    bg="black")
        return copyright

#-----------------------------------------------

    menu_controll = Tk ()

    pokret = p1_down

    windows_configuration()

    menu_controll.bind("<Key>",start_new_game)

#-----------------------------------------------

    naslov().pack(pady=150)
    copyright().pack(side="bottom")