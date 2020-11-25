from tkinter import*
import webbrowser
from PIL import Image , ImageTk

fen = Tk()
fen.title("FICHE DE MATHEMATIQUES (analyse)")
fen.geometry("720x480")
fen.config (background ='grey')
fen.minsize(480 , 360)
fen.iconbitmap("icon.ico")

#bar de menu
menu_bar = Menu(fen)

#========================================================================================================================================

#insertion des images dans formule

#image trigonometrie
def open_img_trigo():
	trigo = "1.gif"
	img_trigo = Image.open(trigo)
	img_trigo = img_trigo.resize((480 , 360) , Image.ANTIALIAS)
	img_trigo = ImageTk.PhotoImage(img_trigo)
	panel = Label (fen , image = img_trigo)
	panel.image = img_trigo
	panel.pack()
#image DL
def open_img_ineg():
	ineg = "2.png"
	img_ineg = Image.open(ineg)
	img_ineg = img_ineg.resize((480 , 360) , Image.ANTIALIAS)
	img_ineg = ImageTk.PhotoImage(img_ineg)
	panel = Label (fen , image = img_ineg)
	panel.image = img_ineg
	panel.pack()
#image Expo
def open_img_exp():
	exp = "3.jpg"	
	img_exp = Image.open(exp)
	img_exp = img_exp.resize((480 , 360) , Image.ANTIALIAS)
	img_exp = ImageTk.PhotoImage(img_exp)
	panel = Label (fen , image = img_exp)
	panel.image = img_exp
	panel.pack()
#image logarithme
def open_img_log():
	log = "4.gif"
	img_log = Image.open(log)
	img_log = img_log.resize((480 , 360) , Image.ANTIALIAS)
	img_log = ImageTk.PhotoImage(img_log)
	panel = Label (fen , image = img_log)
	panel.image = img_log
	panel.pack()			


#menu formule
Formule = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = "Formule", menu = Formule)
#creation des sous menus de formule
Formule.add_command(label = "Trigonométrie" , command = open_img_trigo)
Formule.add_command(label = "DL", command =open_img_ineg)
Formule.add_command(label = "Expo", command =open_img_exp)
Formule.add_command(label = "Logarithme", command =open_img_log)

#========================================================================================================================================


#insertion des images dans Serie

#image dans proprieté
def open_img_prop():
	prop = "5.gif"
	img_prop = Image.open(prop)
	img_prop = img_prop.resize((480 , 360) , Image.ANTIALIAS)
	img_prop = ImageTk.PhotoImage(img_prop)
	panel = Label (fen , image = img_prop)
	panel.image = img_prop
	panel.pack()

#image dans critere
def open_img_cri():
	cri = "6.png"
	img_cri = Image.open(cri)
	img_cri = img_cri.resize((480 , 360) , Image.ANTIALIAS)
	img_cri = ImageTk.PhotoImage(img_cri)
	panel = Label (fen , image = img_cri)
	panel.image = img_cri
	panel.pack()	


#menu serie
Série = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = "Série", menu = Série)
#creation des sous menus de serie
Série.add_command(label = "Proprieté", command =open_img_prop)
Série.add_command(label = "Critère de convergence", command =open_img_cri)

#========================================================================================================================================

#insertion des images dans suites de fonctions

#image dans propriete
def open_img_propsui():
	propsui = "7.png"
	img_propsui = Image.open(propsui)
	img_propsui = img_propsui.resize((480 , 360) , Image.ANTIALIAS)
	img_propsui = ImageTk.PhotoImage(img_propsui)
	panel = Label (fen , image = img_propsui)
	panel.image = img_propsui
	panel.pack()

#image dans mode
def open_img_modesui():
	modesui = "8.png"
	img_modesui = Image.open(modesui)
	img_modesui = img_modesui.resize((480 , 360) , Image.ANTIALIAS)
	img_modesui = ImageTk.PhotoImage(img_modesui)
	panel = Label (fen , image = img_modesui)
	panel.image = img_modesui
	panel.pack()	

#menu suites des fonctions
suFonctions = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = "Suites des Fonctions", menu = suFonctions)
#creation des sous menus suites de fonctions
suFonctions.add_command(label = "Définition", command =open_img_propsui)
suFonctions.add_command(label = "Mode de convergence", command =open_img_modesui)

#========================================================================================================================================

#insertion des images dans series de fonctions

#image dans propriete
def open_img_propse():
	propse = "9.png"
	img_propse = Image.open(propse)
	img_propse = img_propse.resize((480 , 360) , Image.ANTIALIAS)
	img_propse = ImageTk.PhotoImage(img_propse)
	panel = Label (fen , image = img_propse)
	panel.image = img_propse
	panel.pack()

#image dans mode
def open_img_modese():
	modese = "10.png"
	img_modese = Image.open(modese)
	img_modese = img_modese.resize((480 , 360) , Image.ANTIALIAS)
	img_modese = ImageTk.PhotoImage(img_modese)
	panel = Label (fen , image = img_modese)
	panel.image = img_modese
	panel.pack()			

#menu series des foctions
séFonctions = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = "Séries des Fonctions", menu = séFonctions)
#creation des sous menus séries de fonctions
séFonctions.add_command(label = "Définition", command =open_img_propse)
séFonctions.add_command(label = "Mode de convergence", command =open_img_modese)


fen.config(menu = menu_bar)
fen.mainloop()
