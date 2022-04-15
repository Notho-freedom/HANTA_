from tkintermapview import TkinterMapView
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from googletrans import Translator
import speech_recognition as sr
from PIL import Image, ImageTk
from tkinter import StringVar
from tkintermapview import *
import tkinter.messagebox
from hmac import trans_36
import PySimpleGUI as sg
from tkinter import Menu
from tkinter import ttk
import customtkinter
import wolframalpha
from geopy import *
import googletrans
import wikipedia
import requests
import datetime
import pyttsx3
import tkinter
import geopy
import time
import json
import sys
import os


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
PATH = os.path.dirname(os.path.realpath(__file__))
client = wolframalpha.Client("lilpumpsaysnopeeking")
sg.theme('DarkPurple')

def speak(texte):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(texte)
    engine.runAndWait()


class App(customtkinter.CTk):

    APP_NAME = "H A N T A"
    WIDTH = 1000
    HEIGHT = 700

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(App.APP_NAME)
        self.geometry(str(App.WIDTH) + "x" + str(App.HEIGHT))
        self.minsize(App.WIDTH, App.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind("<Command-q>", self.on_closing)
        self.bind("<Command-w>", self.on_closing)
        self.createcommand('tk::mac::Quit', self.on_closing)

        self.geolocator = Nominatim(user_agent='HANTA')
        self.list_cord=[]
        self.list_cord_other=[]


        image = Image.open(PATH + "/test_images/bg_gradient.jpg").resize((2048, 1900))
        self.bg_image = ImageTk.PhotoImage(image)

        self.image_label = tkinter.Label(master=self, image=self.bg_image)
        self.image_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.call('wm', 'iconphoto', self,ImageTk.PhotoImage(file=PATH + "/test_images/logo.jpg"))


        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=500,height=100)
        self.frame_left.grid(row=0, column=0, padx=5, pady=10, sticky="nsew", rowspan=1)

        self.frame_right = customtkinter.CTkFrame(master=self,
                                                  corner_radius=10)
        self.frame_right.grid(row=0, column=1, rowspan=1, pady=10, padx=5, sticky="nsew")

        # ============ frame_left ============

        self.frame_left.grid_rowconfigure(0, minsize=5)

        image_2 = Image.open(PATH + "/test_images/h2.jpg").resize((300, 200))
        self.bg_image_2 = ImageTk.PhotoImage(image_2)

        self.image_label_2 = tkinter.Label(master=self.frame_left,image=self.bg_image_2,width=300,height=200,bd=0,justify=tkinter.CENTER)
        self.image_label_2.grid(pady=8, padx=10, row=0, column=0,columnspan=4)


        self.bar = customtkinter.CTkButton(master=self.frame_left,
                                                text="MENU",
                                                width=300, height=30,
                                                corner_radius=8)
        self.bar.grid(pady=8, padx=10, row=1, column=0,columnspan=4)


        self.switch_2 = customtkinter.CTkSwitch(master=self.frame_left,
                                                text="Dark Mode",
                                                command=self.change_mode)
        self.switch_2.grid(pady=5, padx=10, row=7, column=2)

        self.switch_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="info",
                                               width=60, height=15,
                                                border_width=0,
                                                corner_radius=8,
                                                command=self.city2)
        self.switch_3.grid(pady=5, padx=10, row=7, column=1)

        self.switch_4 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Vocale",
                                               width=60, height=15,
                                                border_width=0,
                                                corner_radius=8,
                                                command=self.vocal)
        self.switch_4.grid(pady=5, padx=10, row=7, column=0)

        self.lang=StringVar()
        self.lang.set('en')
        liste_lang=[]
        combo_search = ttk.Combobox(master=self.frame_left,textvariable=self.lang,font=("times new roman",10),width=6)
        combo_search.grid(row=8,column=0,pady=5,padx=10,sticky="W")

        lang={'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'or': 'odia', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'}
        for kes in lang.keys():
            liste_lang.append(kes)
        combo_search['values']= tuple(liste_lang)
        # ============ frame_right ============

        self.frame_right.grid_rowconfigure(0, weight=1)
        self.frame_right.grid_rowconfigure(1, weight=0)
        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_columnconfigure(1, weight=0)
        self.frame_right.grid_columnconfigure(2, weight=1)

        self.map_widget = TkinterMapView(self.frame_right, width=500, height=250, corner_radius=9)
        self.map_widget.grid(row=0, rowspan=1, column=0, columnspan=5, sticky="nswe", padx=15, pady=15)
        self.map_widget.set_address("yaounde")

        self.entry = customtkinter.CTkEntry(master=self.frame_left,
                                            placeholder_text="Localisation...",
                                            width=120,
                                            height=30,
                                            corner_radius=8)
        self.entry.grid(row=3, column=0, sticky="we", padx=20, pady=10,columnspan=4)
        self.entry.entry.bind("<Return>", self.search_event)

        self.button_5 = customtkinter.CTkButton(master=self.frame_left,
                                               width=60, height=15,
                                                text="Localiser",
                                                command=self.search_event,
                                                border_width=0,
                                                corner_radius=8)
        self.button_5.grid(row=4, column=0, sticky="w", padx=10, pady=10)

#================================new_button================

        self.button_6 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Marquer",
                                                command=self.set_marker_event,
                                               width=60, height=15,
                                                border_width=0,
                                                corner_radius=8)
        self.button_6.grid(pady=10, padx=10, row=4, column=1)

        self.button_7 = customtkinter.CTkButton(master=self.frame_left,text="Retirer",command=self.clear_marker_event,width=60, height=15,border_width=0,corner_radius=8)
        self.button_7.grid(pady=10, padx=10, row=4, column=2)
#==============================end==new_button================


        self.slider_1 = customtkinter.CTkSlider(master=self.frame_left,
                                                width=250,
                                                height=15,
                                                from_=0, to=19,
                                                border_width=5,
                                                command=self.slider_event)
        self.slider_1.grid(row=2, column=0, padx=10, pady=10,columnspan=4)
        self.slider_1.set(self.map_widget.zoom)

        self.marker_list_box = tkinter.Listbox(self.frame_right, height=8)
        self.marker_list_box.grid(row=1, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

        self.marker_list_dis = tkinter.Listbox(self.frame_right, height=8)
        self.marker_list_dis.grid(row=1, column=3, columnspan=3, sticky="ew", padx=10, pady=10)

        self.save_marker_button = customtkinter.CTkButton(master=self.frame_left,text="Enregistrer",width=60, height=15,border_width=0,corner_radius=8,command=self.save_marker)
        self.save_marker_button.grid(row=6, column=0, pady=10, padx=10)

        self.clear_marker_button = customtkinter.CTkButton(master=self.frame_left,text="Vider",width=60, height=15,border_width=0,corner_radius=8,command=self.clear_marker_list)
        self.clear_marker_button.grid(row=6, column=1, pady=10, padx=10)

        self.connect_marker_button = customtkinter.CTkButton(master=self.frame_left,text="Connecter",width=60, height=15,border_width=0,corner_radius=8,command=self.connect_marker)
        self.connect_marker_button.grid(row=6, column=2, pady=10, padx=10)


        self.marker_path = None
        self.marker_list = []

        self.search_marker = None
        self.search_in_progress = False
        # ============ create two CTkFrames ============
    def pmd(self,topic):
        try:
            wiki_res = wikipedia.summary(topic, sentences=2)
            wolfram_res = next(client.query(topic).results).text
            speak(wolfram_res)
            sg.PopupNonBlocking("Wolfram Result: "+wolfram_res,"Wikipedia Result: "+wiki_res)
        except wikipedia.exceptions.DisambiguationError:
            wolfram_res = next(client.query(topic).results).text
            speak(wolfram_res)
            sg.PopupNonBlocking(wolfram_res)
        except wikipedia.exceptions.PageError:
            wolfram_res = next(client.query(topic).results).text
            speak(wolfram_res)
            sg.PopupNonBlocking(wolfram_res)
        except:
            wiki_res = wikipedia.summary(topic, sentences=2)
            speak(wiki_res)
            sg.PopupNonBlocking(wiki_res)
        else:
            speak("impossible de se connecter au serveur!")

    def takeCommand(self,event=None):

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='Fr-fr')
            print(f"requette:{query}\n")

        except Exception as e:
            print(e)
            speak("désolé, mais je ne vous écoute pas; vérifiez votre micro")
            return None
        return query

    def vocal(self, event=None):
        query=self.takeCommand()
        if "localise" in query:
            add = query.replace("localise","")
            speak(f'adresse a localisée: {add}')
            self.search(add)
            self.location = self.geolocator.geocode(add)
            speak(self.location.address)
        elif "parle moi de" in query or  "parle-moi de" in query:
            topic=query.replace("parle moi de","")
            topic=query.replace("parle-moi de","")
            self.pmd(topic)


    def city(self, ville):
        url_weather = "http://api.openweathermap.org/data/2.5/weather?q="+str(ville)+"&APPID=beb97c1ce62559bba4e81e28de8be095"
        r_weather = requests.get(url_weather)
        data = r_weather.json()
        t = data['main']['temp']       
        speak("Température moyenne {} dégrés Celsius".format(int(t-273.15)))
        t_min = data['main']['temp_min']
        t_max = data['main']['temp_max']
        speak("Les températures varient entre {}".format(int(t_min-273.15)) + " a {} dégrés Celsius".format(int(t_max-273.15)))
        humidite = data['main']['humidity']
        speak("Taux d'humidité de {}".format(int(humidite)) + "%")
        temps = data['weather'][0]['description']
        speak("Conditions climatiques : {}".format(temps))
        print("Conditions climatiques : {}".format(temps))

    def next(ville):
        url_forecast = "http://api.openweathermap.org/data/2.5/forecast?q="+ville+"&APPID=beb97c1ce62559bba4e81e28de8be095"
        r_forecast = requests.get(url_forecast)
        data = r_forecast.json()
               
        for i in range (0,25):
            t = data['list'][i]['main']['temp']
            temps = data['list'][i]['weather'][0]['description']
            time = data['list'][i]['dt_txt']
            speak("Previsions pour le {}".format(time))
            speak("La temperature moyenne est de {} degres Celsius".format(t-273.15))
            speak("Conditions climatiques : {}".format(temps))

    def search_event(self, event=None):
        if not self.search_in_progress:
            self.search_in_progress = True
            if self.search_marker not in self.marker_list:
                self.map_widget.delete(self.search_marker)

            address = self.entry.get()
            self.search_marker = self.map_widget.set_address(address, marker=True)
            
            if self.search_marker is False:
                speak("Adresse introuvable!")
                self.search_marker = None
            else:
                self.search_marker = self.map_widget.set_address(address, marker=True)
                current_position = self.map_widget.get_position()
            self.search_in_progress = False

    def city2(self):
        address = self.entry.get()
        self.search_marker = self.map_widget.set_address(address, marker=True)
        if self.search_marker is not False:
            self.location = self.geolocator.geocode(address)
            speak(self.location.address)
            self.city(address)

    def save_marker(self):
        address = self.entry.get()
        if self.search_marker is not None:
            self.marker_list_box.insert(tkinter.END, f" {len(self.marker_list)}. {self.search_marker.text} ")
            self.marker_list_box.see(tkinter.END)
            self.marker_list.append(self.search_marker)


            self.cord = self.geolocator.geocode(address)
            self.list_cord=[self.cord.latitude,self.cord.longitude]
            self.list_cord_other.append(self.list_cord)
            self.marker_list_dis.insert(tkinter.END,self.list_cord)
            self.marker_list_dis.see(tkinter.END)

    def clear_marker_list(self):
        for marker in self.marker_list:
            self.map_widget.delete(marker)

        self.marker_list_box.delete(0, tkinter.END)
        self.marker_list_dis.delete(0, tkinter.END)
        self.marker_list.clear()
        self.connect_marker()

    def connect_marker(self):
        print(self.marker_list)
        position_list = []

        for marker in self.marker_list:
            position_list.append(marker.position)

        if self.marker_path is not None:
            self.map_widget.delete(self.marker_path)

        if len(position_list) > 0:
            self.marker_path = self.map_widget.set_path(position_list)
            speak('distance nète')
            speak(geodesic(self.list_cord_other[0],self.list_cord_other[1]).km)

    def search(self, add):
        self.search_marker = self.map_widget.set_address(add, marker=True)
        if self.search_marker is False:
            speak("Adresse introuvable!")
            self.search_marker = None
        else:
            self.search_marker = self.map_widget.set_address(add, marker=True)
            current_position = self.map_widget.get_position()
        self.search_in_progress = False
        self.map_widget.set_zoom(self.map_widget.zoom)

    def slider_event(self, value):
        self.map_widget.set_zoom(value)

    def set_marker_event(self):
        current_position = self.map_widget.get_position()
        self.marker_list.append(self.map_widget.set_marker(current_position[0], current_position[1]))

    def clear_marker_event(self):
        for marker in self.marker_list:
            marker.delete()

    def change_mode(self):
        if self.switch_2.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    if float(customtkinter.__version__) < 3.2:
        print("Please update customtkinter: pip3 install customtkinter --upgrade")
        exit()

    app = App()
    app.start()
from tkintermapview import TkinterMapView
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from googletrans import Translator
import speech_recognition as sr
from PIL import Image, ImageTk
from tkinter import StringVar
from tkintermapview import *
import tkinter.messagebox
from hmac import trans_36
import PySimpleGUI as sg
from tkinter import Menu
from tkinter import ttk
import customtkinter
import wolframalpha
from geopy import *
import googletrans
import wikipedia
import requests
import datetime
import pyttsx3
import tkinter
import geopy
import time
import json
import sys
import os


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
PATH = os.path.dirname(os.path.realpath(__file__))
client = wolframalpha.Client("lilpumpsaysnopeeking")
sg.theme('DarkPurple')

def speak(texte):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(texte)
    engine.runAndWait()


class App(customtkinter.CTk):

    APP_NAME = "H A N T A"
    WIDTH = 1000
    HEIGHT = 700

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(App.APP_NAME)
        self.geometry(str(App.WIDTH) + "x" + str(App.HEIGHT))
        self.minsize(App.WIDTH, App.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind("<Command-q>", self.on_closing)
        self.bind("<Command-w>", self.on_closing)
        self.createcommand('tk::mac::Quit', self.on_closing)

        self.geolocator = Nominatim(user_agent='HANTA')
        self.list_cord=[]
        self.list_cord_other=[]


        image = Image.open(PATH + "/test_images/bg_gradient.jpg").resize((2048, 1900))
        self.bg_image = ImageTk.PhotoImage(image)

        self.image_label = tkinter.Label(master=self, image=self.bg_image)
        self.image_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.call('wm', 'iconphoto', self,ImageTk.PhotoImage(file=PATH + "/test_images/logo.jpg"))


        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=500,height=100)
        self.frame_left.grid(row=0, column=0, padx=5, pady=10, sticky="nsew", rowspan=1)

        self.frame_right = customtkinter.CTkFrame(master=self,
                                                  corner_radius=10)
        self.frame_right.grid(row=0, column=1, rowspan=1, pady=10, padx=5, sticky="nsew")

        # ============ frame_left ============

        self.frame_left.grid_rowconfigure(0, minsize=5)

        image_2 = Image.open(PATH + "/test_images/h2.jpg").resize((300, 200))
        self.bg_image_2 = ImageTk.PhotoImage(image_2)

        self.image_label_2 = tkinter.Label(master=self.frame_left,image=self.bg_image_2,width=300,height=200,bd=0,justify=tkinter.CENTER)
        self.image_label_2.grid(pady=8, padx=10, row=0, column=0,columnspan=4)


        self.bar = customtkinter.CTkButton(master=self.frame_left,
                                                text="MENU",
                                                width=300, height=30,
                                                corner_radius=8)
        self.bar.grid(pady=8, padx=10, row=1, column=0,columnspan=4)


        self.switch_2 = customtkinter.CTkSwitch(master=self.frame_left,
                                                text="Dark Mode",
                                                command=self.change_mode)
        self.switch_2.grid(pady=5, padx=10, row=7, column=2)

        self.switch_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="info",
                                               width=60, height=15,
                                                border_width=0,
                                                corner_radius=8,
                                                command=self.city2)
        self.switch_3.grid(pady=5, padx=10, row=7, column=1)

        self.switch_4 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Vocale",
                                               width=60, height=15,
                                                border_width=0,
                                                corner_radius=8,
                                                command=self.vocal)
        self.switch_4.grid(pady=5, padx=10, row=7, column=0)

        self.lang=StringVar()
        self.lang.set('en')
        liste_lang=[]
        combo_search = ttk.Combobox(master=self.frame_left,textvariable=self.lang,font=("times new roman",10),width=6)
        combo_search.grid(row=8,column=0,pady=5,padx=10,sticky="W")

        lang={'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'or': 'odia', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'}
        for kes in lang.keys():
            liste_lang.append(kes)
        combo_search['values']= tuple(liste_lang)
        # ============ frame_right ============

        self.frame_right.grid_rowconfigure(0, weight=1)
        self.frame_right.grid_rowconfigure(1, weight=0)
        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_columnconfigure(1, weight=0)
        self.frame_right.grid_columnconfigure(2, weight=1)

        self.map_widget = TkinterMapView(self.frame_right, width=500, height=250, corner_radius=9)
        self.map_widget.grid(row=0, rowspan=1, column=0, columnspan=5, sticky="nswe", padx=15, pady=15)
        self.map_widget.set_address("yaounde")

        self.entry = customtkinter.CTkEntry(master=self.frame_left,
                                            placeholder_text="Localisation...",
                                            width=120,
                                            height=30,
                                            corner_radius=8)
        self.entry.grid(row=3, column=0, sticky="we", padx=20, pady=10,columnspan=4)
        self.entry.entry.bind("<Return>", self.search_event)

        self.button_5 = customtkinter.CTkButton(master=self.frame_left,
                                               width=60, height=15,
                                                text="Localiser",
                                                command=self.search_event,
                                                border_width=0,
                                                corner_radius=8)
        self.button_5.grid(row=4, column=0, sticky="w", padx=10, pady=10)

#================================new_button================

        self.button_6 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Marquer",
                                                command=self.set_marker_event,
                                               width=60, height=15,
                                                border_width=0,
                                                corner_radius=8)
        self.button_6.grid(pady=10, padx=10, row=4, column=1)

        self.button_7 = customtkinter.CTkButton(master=self.frame_left,text="Retirer",command=self.clear_marker_event,width=60, height=15,border_width=0,corner_radius=8)
        self.button_7.grid(pady=10, padx=10, row=4, column=2)
#==============================end==new_button================


        self.slider_1 = customtkinter.CTkSlider(master=self.frame_left,
                                                width=250,
                                                height=15,
                                                from_=0, to=19,
                                                border_width=5,
                                                command=self.slider_event)
        self.slider_1.grid(row=2, column=0, padx=10, pady=10,columnspan=4)
        self.slider_1.set(self.map_widget.zoom)

        self.marker_list_box = tkinter.Listbox(self.frame_right, height=8)
        self.marker_list_box.grid(row=1, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

        self.marker_list_dis = tkinter.Listbox(self.frame_right, height=8)
        self.marker_list_dis.grid(row=1, column=3, columnspan=3, sticky="ew", padx=10, pady=10)

        self.save_marker_button = customtkinter.CTkButton(master=self.frame_left,text="Enregistrer",width=60, height=15,border_width=0,corner_radius=8,command=self.save_marker)
        self.save_marker_button.grid(row=6, column=0, pady=10, padx=10)

        self.clear_marker_button = customtkinter.CTkButton(master=self.frame_left,text="Vider",width=60, height=15,border_width=0,corner_radius=8,command=self.clear_marker_list)
        self.clear_marker_button.grid(row=6, column=1, pady=10, padx=10)

        self.connect_marker_button = customtkinter.CTkButton(master=self.frame_left,text="Connecter",width=60, height=15,border_width=0,corner_radius=8,command=self.connect_marker)
        self.connect_marker_button.grid(row=6, column=2, pady=10, padx=10)


        self.marker_path = None
        self.marker_list = []

        self.search_marker = None
        self.search_in_progress = False
        # ============ create two CTkFrames ============
    def pmd(self,topic):
        try:
            wiki_res = wikipedia.summary(topic, sentences=2)
            wolfram_res = next(client.query(topic).results).text
            speak(wolfram_res)
            sg.PopupNonBlocking("Wolfram Result: "+wolfram_res,"Wikipedia Result: "+wiki_res)
        except wikipedia.exceptions.DisambiguationError:
            wolfram_res = next(client.query(topic).results).text
            speak(wolfram_res)
            sg.PopupNonBlocking(wolfram_res)
        except wikipedia.exceptions.PageError:
            wolfram_res = next(client.query(topic).results).text
            speak(wolfram_res)
            sg.PopupNonBlocking(wolfram_res)
        except:
            wiki_res = wikipedia.summary(topic, sentences=2)
            speak(wiki_res)
            sg.PopupNonBlocking(wiki_res)
        else:
            speak("impossible de se connecter au serveur!")

    def takeCommand(self,event=None):

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='Fr-fr')
            print(f"requette:{query}\n")

        except Exception as e:
            print(e)
            speak("désolé, mais je ne vous écoute pas; vérifiez votre micro")
            return None
        return query

    def vocal(self, event=None):
        query=self.takeCommand()
        if "localise" in query:
            add = query.replace("localise","")
            speak(f'adresse a localisée: {add}')
            self.search(add)
            self.location = self.geolocator.geocode(add)
            speak(self.location.address)
        elif "parle moi de" in query or  "parle-moi de" in query:
            topic=query.replace("parle moi de","")
            topic=query.replace("parle-moi de","")
            self.pmd(topic)


    def city(self, ville):
        url_weather = "http://api.openweathermap.org/data/2.5/weather?q="+str(ville)+"&APPID=beb97c1ce62559bba4e81e28de8be095"
        r_weather = requests.get(url_weather)
        data = r_weather.json()
        t = data['main']['temp']       
        speak("Température moyenne {} dégrés Celsius".format(int(t-273.15)))
        t_min = data['main']['temp_min']
        t_max = data['main']['temp_max']
        speak("Les températures varient entre {}".format(int(t_min-273.15)) + " a {} dégrés Celsius".format(int(t_max-273.15)))
        humidite = data['main']['humidity']
        speak("Taux d'humidité de {}".format(int(humidite)) + "%")
        temps = data['weather'][0]['description']
        speak("Conditions climatiques : {}".format(temps))
        print("Conditions climatiques : {}".format(temps))

    def next(ville):
        url_forecast = "http://api.openweathermap.org/data/2.5/forecast?q="+ville+"&APPID=beb97c1ce62559bba4e81e28de8be095"
        r_forecast = requests.get(url_forecast)
        data = r_forecast.json()
               
        for i in range (0,25):
            t = data['list'][i]['main']['temp']
            temps = data['list'][i]['weather'][0]['description']
            time = data['list'][i]['dt_txt']
            speak("Previsions pour le {}".format(time))
            speak("La temperature moyenne est de {} degres Celsius".format(t-273.15))
            speak("Conditions climatiques : {}".format(temps))

    def search_event(self, event=None):
        if not self.search_in_progress:
            self.search_in_progress = True
            if self.search_marker not in self.marker_list:
                self.map_widget.delete(self.search_marker)

            address = self.entry.get()
            self.search_marker = self.map_widget.set_address(address, marker=True)
            
            if self.search_marker is False:
                speak("Adresse introuvable!")
                self.search_marker = None
            else:
                self.search_marker = self.map_widget.set_address(address, marker=True)
                current_position = self.map_widget.get_position()
            self.search_in_progress = False

    def city2(self):
        address = self.entry.get()
        self.search_marker = self.map_widget.set_address(address, marker=True)
        if self.search_marker is not False:
            self.location = self.geolocator.geocode(address)
            speak(self.location.address)
            self.city(address)

    def save_marker(self):
        address = self.entry.get()
        if self.search_marker is not None:
            self.marker_list_box.insert(tkinter.END, f" {len(self.marker_list)}. {self.search_marker.text} ")
            self.marker_list_box.see(tkinter.END)
            self.marker_list.append(self.search_marker)


            self.cord = self.geolocator.geocode(address)
            self.list_cord=[self.cord.latitude,self.cord.longitude]
            self.list_cord_other.append(self.list_cord)
            self.marker_list_dis.insert(tkinter.END,self.list_cord)
            self.marker_list_dis.see(tkinter.END)

    def clear_marker_list(self):
        for marker in self.marker_list:
            self.map_widget.delete(marker)

        self.marker_list_box.delete(0, tkinter.END)
        self.marker_list_dis.delete(0, tkinter.END)
        self.marker_list.clear()
        self.connect_marker()

    def connect_marker(self):
        print(self.marker_list)
        position_list = []

        for marker in self.marker_list:
            position_list.append(marker.position)

        if self.marker_path is not None:
            self.map_widget.delete(self.marker_path)

        if len(position_list) > 0:
            self.marker_path = self.map_widget.set_path(position_list)
            speak('distance nète')
            speak(geodesic(self.list_cord_other[0],self.list_cord_other[1]).km)

    def search(self, add):
        self.search_marker = self.map_widget.set_address(add, marker=True)
        if self.search_marker is False:
            speak("Adresse introuvable!")
            self.search_marker = None
        else:
            self.search_marker = self.map_widget.set_address(add, marker=True)
            current_position = self.map_widget.get_position()
        self.search_in_progress = False
        self.map_widget.set_zoom(self.map_widget.zoom)

    def slider_event(self, value):
        self.map_widget.set_zoom(value)

    def set_marker_event(self):
        current_position = self.map_widget.get_position()
        self.marker_list.append(self.map_widget.set_marker(current_position[0], current_position[1]))

    def clear_marker_event(self):
        for marker in self.marker_list:
            marker.delete()

    def change_mode(self):
        if self.switch_2.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    if float(customtkinter.__version__) < 3.2:
        print("Please update customtkinter: pip3 install customtkinter --upgrade")
        exit()

    app = App()
    app.start()
