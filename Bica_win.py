from tkinter import *
from tkinter.font import BOLD
import Menu_of_game

#-----------------------------------------------

def menu_of_game(jezik,p1color,p2color,p1_up,p1_down,p2_up,p2_down,player1_result,player2_result):                         # Novi prozor kada se klikne dugme srpski ili engleski jezik

#-----------------------------------------------

    class lb(object):
        def __init__(self, c_text, f_s, rel, bor):
            self.c_text=c_text
            self.f_s=f_s
            self.rel=rel
            self.bor=bor
            
        def create_label(self):
            c_lb = Label(menu_game, 
                    text=self.c_text, 
                    font=("Arial", self.f_s, BOLD), 
                    fg="red", 
                    bg="black",  
                    relief=self.rel, 
                    bd=self.bor )
            return(c_lb)

#-----------------------------------------------

    def start_new_game():
        menu_game.destroy()
        Menu_of_game.menu_of_game(jezik,p1color,p2color,p1_up,p1_down,p2_up,p2_down)

    def chosen_language(jezik):
        if jezik == "serbian":
            main_text = "Bica je pobedila!!!"
            copyright_text = "Igricu napravio Velicki"
            kontrole = "Mica ima: "+str(player1_result)+" poena"
            boje = "Bica ima: "+str(player2_result)+" poena"
            Pokreni_igricu = "Igraj ponovo!"

        elif jezik == "english":
            main_text = "Bica is the winner!!!"
            copyright_text = "copyright by Velicki"
            kontrole = "Mica have: "+str(player1_result)+" points"
            boje = "Bica have: "+str(player2_result)+" points"
            Pokreni_igricu = "Play again"

        return (main_text,copyright_text,kontrole,boje,Pokreni_igricu)
    
    def windows_configuration():
        menu_game.geometry("600x600")   
        menu_game.title(chosen_language(jezik)[0])
        menu_game.resizable(False, False)
        icon = PhotoImage(file="Icon.png")
        menu_game.iconphoto(True, icon)
        menu_game.config(bg="black")

    def start_game():
        start_game = Button(menu_game, 
                    text=chosen_language(jezik)[4], 
                    font=("Arial", 20, BOLD), 
                    fg="red", 
                    bg="black",
                    activeforeground="red",
                    activebackground="black",  
                    relief=RAISED, 
                    bd=10, 
                    command=start_new_game )
        return start_game

#-----------------------------------------------

    menu_game = Tk ()

    windows_configuration()

    nas = lb(chosen_language(jezik)[0], 40, RAISED, 5)
    
    con = lb(chosen_language(jezik)[2], 20, RAISED, 5)
    
    col = lb(chosen_language(jezik)[3], 20, RAISED, 5)
    
    cr = lb(chosen_language(jezik)[1], 10, FLAT, 5)

#-----------------------------------------------

    nas.create_label().pack(pady=50)
    con.create_label().pack(pady=10)
    col.create_label().pack(pady=10)
    start_game().pack(pady=20)
    cr.create_label().pack(side="bottom")