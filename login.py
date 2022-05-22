import tkinter
import tkinter as tk
from tkinter import *
import tkinter.messagebox
import mysql.connector
import customtkinter
from PIL import Image, ImageTk
import os
import pyttsx3
import hanta
import numpy
import PIL


customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

PATH = os.path.dirname(os.path.realpath(__file__))

connectiondb = mysql.connector.connect(host="localhost",user="root",passwd="",database="edmin")
cursordb = connectiondb.cursor()



class personne():
    """ Class personne comportant les informations personnelles des utilisateurs"""
    def __init__(self,pseudo,email,password,typeCompte,sexe,coordonnees,pp):
        self.pseudo = pseudo
        self.email = email
        self.password = password
        self.typeCompte = typeCompte
        self.sexe = sexe
        self.coordonnees = coordonnees


    def __repr__(self) -> str:
        return f"je m'appel {self.pseudo}, j'utilise un compte {self.typeCompte}. Je suis également un utilisateur de Hanta."

    def info(self):
        return  f"je m'appel {self.pseudo}, j'utilise un compte {self.typeCompte}. Je suis également un utilisateur de hanta."

def speak(texte):
    from gtts import gTTS
    from playsound import playsound
    s = gTTS(texte,lang="fr",slow=False)
    s.save('me.mp3')
    playsound('me.mp3',block=False)

class client(personne):
    def __init__(self, pseudo, email, password, typeCompte, sexe, coordonnees,pp,destination):
        super().__init__(pseudo, email, password, typeCompte, sexe,coordonnees,pp)
        self.destination = destination
        self.pp=pp
    
    def __repr__(self) -> str:
        print(f"mon pseudo est {self.pseudo},je suis de sexe {self.sexe} et ma destination pour aujourd'hui est {self.destination}")
        return super().__repr__()

class vehiculer(personne):
    """classe vehiculer caractérise les moto-taximans ou toute personne possédant un véhicule et souhaitant le mettre à la disposition des autes utilisateurs"""

    def __init__(self, pseudo, email, password, typeCompte, sexe, coordonnees,pp, vehicule,tarif):
        super().__init__(pseudo, email, password, typeCompte, sexe, coordonnees,pp)
        self.vehicule = vehicule
        self.tarif = tarif
    
    def __repr__(self) -> str:
        print(f" moi c'est {self.pseudo} j'ai un compte de type {self.typeCompte}. mon vehicule est {self.vehicule}. je me situe actuellement aux coordonnées suivantes {self.coordonnees}")
        return super().__repr__()+str(f"mon tarif: {self.tarif}")


class Login(customtkinter.CTk):

    Login_NAME = "Edmin::Trans"
    WIDTH = 600
    HEIGHT = 700

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(Login.Login_NAME)
        self.geometry(f"{Login.WIDTH}x{Login.HEIGHT}")
        self.minsize(Login.WIDTH, Login.HEIGHT)
        self.maxsize(Login.WIDTH, Login.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind("<Command-q>", self.on_closing)
        self.bind("<Command-w>", self.on_closing)
        self.createcommand('tk::mac::Quit', self.on_closing)




        # Convert PIL Image to NumPy array
        img = Image.open(PATH + "/test_images/bg_gradient.jpg").resize((self.WIDTH, self.HEIGHT))
        arr = numpy.array(img)

        # Convert array to Image
        image = Image.fromarray(arr)
        self.bg_image = ImageTk.PhotoImage(image)





        self.image_label = tkinter.Label(master=self, image=self.bg_image)
        self.image_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)




        # Convert PIL Image to NumPy array
        img = Image.open(PATH + "/test_images/bg_gradient.jpg").resize((self.WIDTH, self.HEIGHT))
        arr = numpy.array(img)

        # Convert array to Image
        image = Image.fromarray(arr)
        self.bg_image = ImageTk.PhotoImage(image)





        self.image_label = tkinter.Label(master=self, image=self.bg_image)
        self.image_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)



        self.frame = customtkinter.CTkFrame(master=self,width=400,height=Login.HEIGHT-60,corner_radius=0)
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.label_1 = customtkinter.CTkLabel(master=self.frame, width=200, height=60,
                                                fg_color=("white", "gray35"), text=" E D M I N : : T R A N S \n C o n n e c t i o n ")
        self.label_1.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        self.pseudo = customtkinter.CTkEntry(master=self.frame, corner_radius=20, width=300, placeholder_text="username")
        self.pseudo.place(relx=0.5, rely=0.52, anchor=tkinter.CENTER)

        self.password = customtkinter.CTkEntry(master=self.frame, corner_radius=20, width=300, show="*", placeholder_text="password")
        self.password.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

        self.button_2 = customtkinter.CTkButton(master=self.frame, text="Login",
                                                corner_radius=6, command=self.login_verification, width=200)
        self.button_2.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

        self.entry = tk.Label(master=self.frame, width=15,bg="gray30",fg="lime")
        self.entry.place(relx=0.5, rely=0.82, anchor=tkinter.CENTER)



    def login_verification(self):
        user_verification = self.pseudo.get()
        pass_verification = self.password.get()
        sql = "select * from user where pseudo = %s and password = %s"
        cursordb.execute(sql,[(user_verification),(pass_verification)])
        results = cursordb.fetchall()
        if results:
            for i in results:
                self.entry["text"]="S u c c è s !"
                i=list(i)
                print(i)
                if i[2]==1:
                    self.sexe="Masculin"
                    self.nomin="Monsieur"
                else:
                    self.sexe="Feminin"
                    self.nomin="Madame"
                self.user = client(i[1],i[3],i[4],"Client",self.sexe,"",i[7],"")

                # Convert PIL Image to NumPy array
                img2 = Image.open(PATH + "/test_images/" + self.user.pp).resize((self.WIDTH, self.HEIGHT))
                arr2 = numpy.array(img2)

                # Convert array to Image
                image2 = Image.fromarray(arr2)
                self.bg_image2 = ImageTk.PhotoImage(image2)

                self.image_label2 = customtkinter.CTkLabel(master=self.frame, image=self.bg_image2,width=100, height=100,)
                self.image_label2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

                if os.path.exists("config.ht"):
                    speak(f"Bienvenue {self.user.pseudo}, vos informations ont déjà été enregistrée!")
                else:
                    f = open("config.ht","a+")
                    f.write(i[1]+"\n")
                    f.write(i[3]+"\n")
                    f.write(i[4]+"\n")
                    f.write("Client"+"\n")
                    f.write(self.sexe+"\n")
                    f.write(""+"\n")
                    f.write(i[7]+"\n")
                    f.write(""+"\n")
                    f.close()

                    speak(f"Bienvenue {self.user.pseudo} !\nLa procédure de connection est un succès.\nVoici tes informations:\n-pseudo: {self.user.pseudo}\n-sexe: {self.user.sexe}\n-Type de compte: {self.user.typeCompte}\nJe vous souhaite un bon retour {self.nomin};Vos informations ont été prises en charge, veillez redémarré le programme; Assurez vous de rester connecter à internet pour profiter de la meilleur expérience possible. Dans le cas contraire vous pourez toujour vous contanté du mode offline!")
        else:
            
            tkinter.messagebox.showerror("Login Error", "veriffiez vos informations")


    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()




if __name__ == "__main__":
    login = Login()
    login.start()
