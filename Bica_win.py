from tkinter import *
from tkinter.font import BOLD
import Menu_of_game




def menu_of_game(jezik,p1color,p2color,p1_up,p1_down,p2_up,p2_down,player1_result,player2_result):                         # Novi prozor kada se klikne dugme srpski ili engleski jezik

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

    def start_new_game():
        menu_game.destroy()
        Menu_of_game.menu_of_game(jezik,p1color,p2color,p1_up,p1_down,p2_up,p2_down)

    menu_game = Tk ()


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

    menu_game.geometry("600x600")              # Velicina prozora
    menu_game.title(main_text)                 # Ime prozora
    menu_game.resizable(False, False)

    icon = PhotoImage(file="Icon.png")         # Slika je prebacena u format koji moze da cita python
    menu_game.iconphoto(True, icon)            # Ikonica prozora

    menu_game.config(bg="black")               # Boja pozadine prozora

    nas = lb(main_text, 40, RAISED, 5)
    naslov = nas.create_label()                #Napravljen i dekorisan naslov
    
    con = lb(kontrole, 20, RAISED, 5)
    controll = con.create_label()              #Kreirano dugme za promene kontole
    
    col = lb(boje, 20, RAISED, 5)
    colorr = col.create_label()                #Kreirano dugme za promenu boje igraca
    
    start_game = Button(menu_game, 
                    text=Pokreni_igricu, 
                    font=("Arial", 20, BOLD), 
                    fg="red", 
                    bg="black",
                    activeforeground="red",
                    activebackground="black",  
                    relief=RAISED, 
                    bd=10, 
                    command=start_new_game )   #Kreirano dugme za pokretanje igrice

    cr = lb(copyright_text, 10, FLAT, 5)
    copyright = cr.create_label()              # Informacija na dnu stranice ko je napravio igricu

    naslov.pack(pady=50)                       # Dugme je ubaceno u prozor
    controll.pack(pady=10)
    colorr.pack(pady=10)
    start_game.pack(pady=20)

    copyright.pack(side="bottom")              # Informacija na dnu je ubacena u prozor