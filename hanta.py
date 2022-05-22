import tkinter
import customtkinter
from tkintermapview import TkinterMapView
from hmac import trans_36
from geopy.distance import geodesic
from googletrans import Translator
from PIL import Image, ImageTk
from tkinter import StringVar
from tkintermapview import *
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
import tkinter.messagebox
from tkinter import ttk
from geopy import *
import googletrans
from gtts import gTTS
from playsound import playsound
import tkinter.messagebox
import mysql.connector
import pyttsx3
import tkinter
import geopy
import sys
import os
import requests
import json
import datetime
import time
import numpy
from random import random, randrange, getrandbits, randint 

geolocator = Nominatim(user_agent="edmin")
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
PATH = os.path.dirname(os.path.realpath(__file__))





def talk(texte):
    engine = pyttsx3.init()
    engine.say(texte)
    engine.runAndWait()

def speak(texte,language="fr"):
    from gtts import gTTS
    from playsound import playsound
    s = gTTS(texte,lang=language)
    s.save('me.mp3')
    playsound('me.mp3',block=False)



















class App(customtkinter.CTk):

    APP_NAME = "H A N T A"
    WIDTH = 1200
    HEIGHT = 700

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
#=======================init and config windows=====
        self.title(App.APP_NAME)
        self.geometry(str(App.WIDTH) + "x" + str(App.HEIGHT))
        self.minsize(App.WIDTH, App.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind("<Command-q>", self.on_closing)
        self.bind("<Command-w>", self.on_closing)
        self.createcommand('tk::mac::Quit', self.on_closing)

# ===================== ATTRIB ===================

        self.marker_path = None
        self.search_marker = None
        self.search_in_progress = False
    # ============ Listes ============
        self.marker_list = []
        self.marker_list = []
        self.address_local=[]
        self.liste_lang=[]
        self.cood_dis=[]
        self.parcourt=[]

    # ==========StringVar ============
        self.lang=StringVar()
        
#===============get user data============
        self.user=[]

        f=open("config.ht","r")
        for line in f:
            line = line.replace('\n','')
            self.user.append(line)
        f.close()
        print(self.user)
    #=========set space in pseudo========
        a=""
        for i in self.user[0]:
            a+=i+" "
        self.user[0]=a
        print(self.user[0])
# ===============Images==================

    # ============ background image ============
        img = Image.open(PATH + "/test_images/bg_gradient.jpg").resize((self.WIDTH+500, self.HEIGHT+500))
        arr = numpy.array(img)
        image = Image.fromarray(arr)
        self.bg_image = ImageTk.PhotoImage(image)
        self.image_label = customtkinter.CTkLabel(master=self, image=self.bg_image)
        self.image_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    # ============ create CTkFrames ============

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ============ frame_left == options frame==========
        self.frame_left = customtkinter.CTkFrame(master=self,width=150)
        self.frame_left.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.frame_left.grid_rowconfigure(0, minsize=10)

        # ============ frame_right == profile user frame==========
        self.frame_right = customtkinter.CTkFrame(master=self,width=150)
        self.frame_right.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        self.frame_right.grid_rowconfigure(0, minsize=10)

        # ============ frame_center ============
        self.frame_center = customtkinter.CTkFrame(master=self,corner_radius=10)
        self.frame_center.grid(row=0, column=1, rowspan=1, pady=10, padx=10, sticky="nsew")
        self.frame_center.grid_rowconfigure(0, weight=1)
        self.frame_center.grid_rowconfigure(1, weight=0)
        self.frame_center.grid_columnconfigure(0, weight=1)
        self.frame_center.grid_columnconfigure(1, weight=0)
        self.frame_center.grid_columnconfigure(2, weight=1)
   
    # ============ title image ============
        img = Image.open(PATH + "/test_images/h_ground.jpg").resize((300, 200))
        arr = numpy.array(img)
        image = Image.fromarray(arr)
        self.bg_image3 = ImageTk.PhotoImage(image)
        self.image_label3 = customtkinter.CTkLabel(master=self.frame_left, image=self.bg_image3,width=300,height=200,justify=tkinter.CENTER)
        self.image_label3.grid(pady=8, padx=10, row=0, column=0,columnspan=4)

    # ============ menu options and list data ============
        self.bar = customtkinter.CTkButton(master=self.frame_left,text="MENU",width=300, height=30,corner_radius=8)
        self.bar.grid(pady=8, padx=10, row=1, column=0,columnspan=3)

        self.space_data = tkinter.Listbox(self.frame_left, height=10)
        self.space_data.grid(row=8, column=0, columnspan=4, sticky="ew", padx=10, pady=10)


    # ============ user image ============
        img = Image.open(PATH + "/test_images/"+str(self.user[6])).resize((250, 200))
        arr = numpy.array(img)
        image = Image.fromarray(arr)
        self.bg_image4 = ImageTk.PhotoImage(image)
        self.image_label4 = customtkinter.CTkLabel(master=self.frame_right, image=self.bg_image4,width=150,height=200,justify=tkinter.CENTER)
        self.image_label4.grid(pady=8, padx=10, row=0, column=0,columnspan=4)

#========================user pseudo and other data============================
        self.label_2 = tkinter.Label(master=self.frame_right, width=9, height=1,font=("impact",15,"bold"),fg="darkred", text=str(self.user[0]) ,justify=tkinter.CENTER)
        self.label_2.grid(pady=8, padx=10, row=1, column=0,columnspan=4)
        #----------------------------------------------------------------------
        self.label_1 = customtkinter.CTkLabel(master=self.frame_right, width=250, height=250,fg_color=("white", "gray35"), text=" E D M I N : : T R A N S \n C o n n e c t i o n ",justify=tkinter.CENTER)
        self.label_1.grid(pady=8, padx=10, row=2, column=0,columnspan=4)





        try:
            #==========================if internet connect=============================================
            requests.get('http://www.google.com')

            # ============ map ============
            self.map_widget = TkinterMapView(self.frame_center, width=500, height=250, corner_radius=9)
            self.map_widget.grid(row=0, rowspan=1, column=0, columnspan=5, sticky="nswe", padx=15, pady=15)
            self.map_widget.set_address("yaoundé")

            # ============ search ============
            self.entry = customtkinter.CTkEntry(master=self.frame_left,placeholder_text="Localisation...",width=120,height=30,corner_radius=8)
            self.entry.grid(row=3, column=0, sticky="we", padx=10, pady=10,columnspan=4)
            self.entry.entry.bind("<Return>", self.search_event)

            # ============ buttons ============
            self.button_5 = customtkinter.CTkButton(master=self.frame_left,width=60, height=15,text="Localiser",command=self.search_event,border_width=0,corner_radius=8)
            self.button_5.grid(row=4, column=0, sticky="w", padx=10, pady=10)
            self.button_6 = customtkinter.CTkButton(master=self.frame_left,text="Marquer",command=self.set_marker_event,width=60, height=15,border_width=0,corner_radius=8)
            self.button_6.grid(pady=10, padx=10, row=4, column=1)
            self.button_7 = customtkinter.CTkButton(master=self.frame_left,text="Retirer",command=self.clear_marker_event,width=60, height=15,border_width=0,corner_radius=8)
            self.button_7.grid(pady=10, padx=10, row=4, column=2)
            self.save_marker_button = customtkinter.CTkButton(master=self.frame_left,text="Enregistrer",width=60, height=15,border_width=0,corner_radius=8,command=self.save_marker)
            self.save_marker_button.grid(row=6, column=0, pady=10, padx=10)
            self.clear_marker_button = customtkinter.CTkButton(master=self.frame_left,text="Vider",width=60, height=15,border_width=0,corner_radius=8,command=self.clear_marker_list)
            self.clear_marker_button.grid(row=6, column=1, pady=10, padx=10)
            self.connect_marker_button = customtkinter.CTkButton(master=self.frame_left,text="Connecter",width=60, height=15,border_width=0,corner_radius=8,command=self.connect_marker)
            self.connect_marker_button.grid(row=6, column=2, pady=10, padx=10)

            # ============ slides for zoom and switch dark mode or light mode============
            self.slider_1 = customtkinter.CTkSlider(master=self.frame_left,width=250,height=15,from_=0, to=19,border_width=5,command=self.slider_event)
            self.slider_1.grid(row=2, column=0, padx=10, pady=10,columnspan=4)
            self.slider_1.set(self.map_widget.zoom)

            #--------------------------------switch-----------------------
            self.switch_2 = customtkinter.CTkSwitch(master=self.frame_left,text="Dark Mode",command=self.change_mode)
            self.switch_2.grid(pady=5, padx=10, row=10, column=2)

            # ========================== listbox for save address and coord ================
            self.marker_list_box = tkinter.Listbox(self.frame_center, height=2)
            self.marker_list_box.grid(row=1, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

            #-------------------------------------------coord-------------------------------
            self.marker_list_dis = tkinter.Listbox(self.frame_center, height=2)
            self.marker_list_dis.grid(row=1, column=3, columnspan=3, sticky="ew", padx=10, pady=10)

            # =========================== combobox for language ============================
            combo_search = ttk.Combobox(master=self.frame_left,textvariable=self.lang,font=("times new roman",10),width=6)
            combo_search.grid(row=10,column=0,pady=5,padx=10,sticky="W")

            lang={'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'or': 'odia', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'}
            for kes in lang.keys():
                self.liste_lang.append(kes)
            combo_search['values']= tuple(self.liste_lang)
            self.lang.set('fr')

        except requests.ConnectionError:

            self.entry_local = customtkinter.CTkEntry(master=self.frame_left,placeholder_text="Local Search...",width=170,height=30,corner_radius=8)
            self.entry_local.grid(row=7, column=0, sticky="we", padx=10, pady=10,columnspan=3)
            self.entry_local.entry.bind("<Return>", self.search_event0)

            # ============ buttons ============
            self.marker_list_box = tkinter.Listbox(self.frame_center,height=250,width=500)
            self.marker_list_box.grid(row=0, column=0, columnspan=3, sticky="ew", padx=20, pady=20)








    def meteo(self,ville="yaoundé"):
        try:
            current_position = self.map_widget.get_position()
            self.space_data.delete(0, tkinter.END)
            url_weather = "http://api.openweathermap.org/data/2.5/weather?q="+ville+"&APPID=beb97c1ce62559bba4e81e28de8be095"
            r_weather = requests.get(url_weather)
            data = r_weather.json()
            t = data['main']['temp']       
            t_min = data['main']['temp_min']
            t_max = data['main']['temp_max']
            humidite = data['main']['humidity']
            temps = data['weather'][0]['description']
            self.space_data.insert(tkinter.END, f"Adresse: {self.search_marker.text}")
            self.space_data.insert(tkinter.END, f"Longitude: {current_position[0]}")
            self.space_data.insert(tkinter.END, f"Latitude: {current_position[1]}")
            self.space_data.insert(tkinter.END, f"Alitude: 0")
            self.space_data.insert(tkinter.END, f"Coord: {current_position}")
            self.space_data.insert(tkinter.END, f"Temperature moyenne: {(str(t-273.15))[:4]}C")
            self.space_data.insert(tkinter.END, f"Variations: De {(str(t_min-273.15))[:4]} à {(str(t_max-273.15))[:4]}C")
            self.space_data.insert(tkinter.END, f"Taux d'humidite: {humidite}%")
            self.space_data.insert(tkinter.END, f"Conditions climatiques : {temps}")
            self.space_data.see(tkinter.END)
        except Exception as e:
            current_position = self.map_widget.get_position()
            self.space_data.delete(0, tkinter.END)
            self.space_data.insert(tkinter.END, f"Adresse: {self.search_marker.text}")
            self.space_data.insert(tkinter.END, f"Longitude: {current_position[0]}")
            self.space_data.insert(tkinter.END, f"Latitude: {current_position[1]}")
            self.space_data.insert(tkinter.END, f"Alitude: 0")
            self.space_data.insert(tkinter.END, f"Coord: {current_position}")
            self.space_data.see(tkinter.END)

    def search_event(self, event=None):
        if not self.search_in_progress:
            self.search_in_progress = True
            if self.search_marker not in self.marker_list:
                self.map_widget.delete(self.search_marker)

            self.address = self.entry.get()
            self.search_marker = self.map_widget.set_address(self.address, marker=True)
            current_position = self.map_widget.get_position()
            if self.search_marker is False:
                speak('Monsieur, je ne trouve pas cette adresse!!')
                self.search_marker = None
            else:
                self.meteo(self.address)
                
            self.search_in_progress = False

    def save_marker(self):
        if self.search_marker is not None:
            self.marker_list_box.insert(tkinter.END, f" {len(self.marker_list)}. {self.search_marker.text} ")
            current_position = self.map_widget.get_position()
            try:
                location = geolocator.geocode(self.address)
            except Exception as e:
                speak(f"Monsieur; je ne parvient pas à recupérer les coordonnées de l'adresse correspondant à {self.address}")

            self.cood=[]
            self.cood.append(location.latitude)
            self.cood.append(location.longitude)
            self.cood = tuple(self.cood)
            self.cood_dis.append(self.cood)
            self.marker_list_dis.insert(tkinter.END,self.cood)
            self.marker_list_box.see(tkinter.END)
            self.marker_list.append(self.search_marker)
            self.parcourt.append(self.address)


    def clear_marker_list(self):

    #====delet marker in map=======================
        for marker in self.marker_list:
            self.map_widget.delete(marker)

        if self.marker_path is not None:
            self.map_widget.delete(self.marker_path)
    #====reset position list=======================
        position_list = []

    #==========clear list data ====================
        self.marker_list.clear()
        self.cood_dis.clear()
        self.parcourt.clear()

    #==========clear listbox data ====================
        self.marker_list_box.delete(0, tkinter.END)
        self.marker_list_dis.delete(0, tkinter.END)
        self.space_data.delete(0, tkinter.END)


    def connect_marker(self):
        self.space_data.delete(0, tkinter.END)
        position_list = []

        for marker in self.marker_list:
            position_list.append(marker.position)

        if self.marker_path is not None:
            self.map_widget.delete(self.marker_path)


        if len(position_list) > 0:
            connectiondb = mysql.connector.connect(host="localhost",user="root",passwd="",database="edmin")
            cursordb = connectiondb.cursor()
            sql = f"select distinct * from travel where Trajet LIKE '%{self.parcourt[0]}%' and Trajet LIKE '%{self.parcourt[1]}%'"
            cursordb.execute(sql,)
            results = cursordb.fetchall()
            succes=["j'ai un trajet qui correspond à votre recherche","Trajet trouver","voici les informations concernant votre Trafic!"]
            if results:
                k=randint(0,2)
                print(k)
                speak(succes[k])
                time.sleep(1)
                for i in results:
                    i=list(i)
                    print(i)
                    self.marker_path = self.map_widget.set_path(position_list)
                    self.space_data.insert(tkinter.END,f"Distance: {geodesic(self.cood_dis[0], self.cood_dis[1]).km} Km")
                    self.space_data.insert(tkinter.END,f"Tarif System: 55XAD/Km")
                    self.space_data.insert(tkinter.END,f"Coût Estimer: {geodesic(self.cood_dis[0], self.cood_dis[1]).km * 55} FcF")
                    self.space_data.insert(tkinter.END,f"Coût Réel: {str(i[2])[:3]}FcF")
                    self.space_data.insert(tkinter.END,f"Trafic Embouteillagé: {i[3]} entre {i[0]}")
                    self.space_data.insert(tkinter.END,f"Etat De La Route: {i[5]}")
                    self.space_data.insert(tkinter.END,f"Durée Du Parcourt(en minutes): {str(i[4])}")
                    self.space_data.insert(tkinter.END,f"Trajet: {i[1]}")
                    if i[3]=='Oui':
                        succes=[f"le traffic est généralement Embouteillagé entre {i[0]}; Il est conseiller de passer plus tôt!",f"Etat De La Route: {i[5]}",f"Durée Du Parcourt(en minutes): {str(i[4])}",f"Trajet: {i[1]}"]
                        k=randint(0,3)
                        print(k)
                        speak(succes[k])
                    else:
                        succes=[f"le traffic est généralement plus ouvert entre {i[0]}; je pense que c'est le meilleur moment pour l'emprunté",f"Etat De La Route: {i[5]}",f"Durée Du Parcourt(en minutes): {str(i[4])}",f"Trajet: {i[1]}"]
                        k=randint(0,3)
                        print(k)
                        speak(succes[k])

                    try:
                        requests.get('http://www.google.com')
                        break
                    except requests.ConnectionError:
                        pass

            else:
                self.marker_path = self.map_widget.set_path(position_list)
                self.space_data.insert(tkinter.END,f"Distance: {geodesic(self.cood_dis[0], self.cood_dis[1]).km} Km")
                self.space_data.insert(tkinter.END,f"Tarif System: 55XAD/Km")
                self.space_data.insert(tkinter.END,f"Coût Estimer: {geodesic(self.cood_dis[0], self.cood_dis[1]).km * 55} FcF")
                self.space_data.insert(tkinter.END,f"Trafic: Non-Defini")
                self.space_data.insert(tkinter.END,f"Etat De La Route: Non-Defini")
                self.space_data.insert(tkinter.END,f"Trajet: Non-Defini")
                self.space_data.insert(tkinter.END,f"Durée Du Parcourt(en minutes): Non-Defini")
                speak("Monsieur; aucun trajet pré-défini ne correspond à votre recherche!")

#============================================Fonction offline============================================================

#====================================================================Recherches locales==================================
    def search_event0(self, event=None):
        a=self.entry_local.get()
        self.address_local.append(a)
        print(self.address_local)
        if len(self.address_local)>=2:
            connectiondb = mysql.connector.connect(host="localhost",user="root",passwd="",database="edmin")
            cursordb = connectiondb.cursor()
            sql = f"select distinct * from travel where Trajet LIKE '%{self.address_local[0]}%' and Trajet LIKE '%{self.address_local[1]}%'"
            cursordb.execute(sql,)
            results = cursordb.fetchall()
            self.space_data.delete(0, tkinter.END)
            if results:
                for i in results:
                    i=list(i)
                    print(i)
                    self.space_data.insert(tkinter.END,f"Distance: Non-Defini")
                    self.space_data.insert(tkinter.END,f"Tarif System: 55XAD/Km")
                    self.space_data.insert(tkinter.END,f"Coût Estimer:  Non-Defini")
                    self.space_data.insert(tkinter.END,f"Coût Réel: {str(i[2])[:3]}FcF")
                    self.space_data.insert(tkinter.END,f"Trafic Embouteillagé: {i[3]} entre {i[0]}")
                    self.space_data.insert(tkinter.END,f"Etat De La Route: {i[5]}")
                    self.space_data.insert(tkinter.END,f"Durée Du Parcourt(en minutes): {str(i[4])}")
                    self.space_data.insert(tkinter.END,f"Trajet: {i[1]}")
                    self.space_data.insert(tkinter.END,f"")
                    self.space_data.insert(tkinter.END,f"===============================================================")
                    self.space_data.insert(tkinter.END,f"")

                    self.marker_list_box.insert(tkinter.END,f"Distance: Non-Defini")
                    self.marker_list_box.insert(tkinter.END,f"Tarif System: 55XAD/Km")
                    self.marker_list_box.insert(tkinter.END,f"Coût Estimer:  Non-Defini")
                    self.marker_list_box.insert(tkinter.END,f"Coût Réel: {str(i[2])[:3]}FcF")
                    self.marker_list_box.insert(tkinter.END,f"Trafic Embouteillagé: {i[3]} entre {i[0]}")
                    self.marker_list_box.insert(tkinter.END,f"Etat De La Route: {i[5]}")
                    self.marker_list_box.insert(tkinter.END,f"Durée Du Parcourt(en minutes): {str(i[4])}")
                    self.marker_list_box.insert(tkinter.END,f"Trajet: {i[1]}")
                    self.marker_list_box.insert(tkinter.END,f"")
                    self.marker_list_box.insert(tkinter.END,f"===============================================================")
                    self.marker_list_box.insert(tkinter.END,f"")
            else:
                self.address_local.clear()
                print("aucun trajet trouver")
        self.parcourt.clear()

#================================================================Fin===De===La======Recherches locales==================================







    def change_mode(self):
        if self.switch_2.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")

    def slider_event(self, value):
        self.map_widget.set_zoom(value)


    def set_marker_event(self):
        current_position = self.map_widget.get_position()
        self.marker_list.append(self.map_widget.set_marker(current_position[0], current_position[1]))


    def clear_marker_event(self):
        for marker in self.marker_list:
            marker.delete()

    def start(self):
        self.mainloop()

    def on_closing(self, event=0):
        self.destroy()







if __name__ == "__main__":
    app = App()
    app.start()