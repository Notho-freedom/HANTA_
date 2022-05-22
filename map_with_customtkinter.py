
from tkintermapview import TkinterMapView
from geopy.distance import geodesic
from googletrans import Translator
from PIL import Image, ImageTk
from tkinter import StringVar
from tkintermapview import *
import tkinter.messagebox
from hmac import trans_36
from geopy import *
from tkinter import ttk
import customtkinter
import googletrans
import tkinter
import pyttsx3
import tkinter
import geopy
import sys
import os


class App(customtkinter.CTk):

    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")
    PATH = os.path.dirname(os.path.realpath(__file__))


    APP_NAME = " H . A . N . T . A "
    WIDTH = 800
    HEIGHT = 500




    def speak(texte):
        engine = pyttsx3.init()
        engine.say(texte)
        engine.runAndWait()



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(App.APP_NAME)
        self.geometry(str(App.WIDTH) + "x" + str(App.HEIGHT))
        self.minsize(App.WIDTH, App.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind("<Command-q>", self.on_closing)
        self.bind("<Command-w>", self.on_closing)
        self.createcommand('tk::mac::Quit', self.on_closing)

        # ============ ATTRIB ============

        self.marker_path = None
        self.marker_list = []

        self.search_marker = None
        self.search_in_progress = False

        self.marker_list = []
        self.lang=StringVar()
        liste_lang=[]


        # ============ create two CTkFrames ============

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,width=150)
        self.frame_left.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.frame_left.grid_rowconfigure(0, minsize=10)

        # ============ frame_right ============

        self.frame_right = customtkinter.CTkFrame(master=self,corner_radius=10)
        self.frame_right.grid(row=0, column=1, rowspan=1, pady=20, padx=20, sticky="nsew")
        self.frame_right.grid_rowconfigure(0, weight=1)
        self.frame_right.grid_rowconfigure(1, weight=0)
        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_columnconfigure(1, weight=0)
        self.frame_right.grid_columnconfigure(2, weight=1)

        # ============ map ============

        self.map_widget = TkinterMapView(self.frame_right, width=500, height=250, corner_radius=9)
        self.map_widget.grid(row=0, rowspan=1, column=0, columnspan=5, sticky="nswe", padx=15, pady=15)
        self.map_widget.set_address("yaoundé")

        # ============ search ============

        self.entry = customtkinter.CTkEntry(master=self.frame_left,placeholder_text="Localisation...",width=120,height=30,corner_radius=8)
        self.entry.grid(row=3, column=0, sticky="we", padx=20, pady=10,columnspan=4)
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

        self.bar = customtkinter.CTkButton(master=self.frame_left,text="MENU",width=300, height=30,corner_radius=8)
        self.bar.grid(pady=8, padx=10, row=1, column=0,columnspan=4)


        # ============ slides ============

        self.slider_1 = customtkinter.CTkSlider(master=self.frame_left,width=250,height=15,from_=0, to=19,border_width=5,command=self.slider_event)
        self.slider_1.grid(row=2, column=0, padx=10, pady=10,columnspan=4)
        self.slider_1.set(self.map_widget.zoom)

        self.switch_2 = customtkinter.CTkSwitch(master=self.frame_left,text="Dark Mode",command=self.change_mode)
        self.switch_2.grid(pady=5, padx=10, row=8, column=2)

        self.marker_list_box = tkinter.Listbox(self.frame_right, height=8)
        self.marker_list_box.grid(row=1, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

        self.marker_list_dis = tkinter.Listbox(self.frame_right, height=8)
        self.marker_list_dis.grid(row=1, column=3, columnspan=3, sticky="ew", padx=10, pady=10)

        self.space_data = tkinter.Listbox(self.frame_left, height=8)
        self.space_data.grid(row=7, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

        combo_search = ttk.Combobox(master=self.frame_left,textvariable=self.lang,font=("times new roman",10),width=6)
        combo_search.grid(row=8,column=0,pady=5,padx=10,sticky="W")


        lang={'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'or': 'odia', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'}
        for kes in lang.keys():
            liste_lang.append(kes)
        combo_search['values']= tuple(liste_lang)
        self.lang.set('en')
        liste_lang=[]


    def search_event(self, event=None):
        if not self.search_in_progress:
            self.search_in_progress = True
            if self.search_marker not in self.marker_list:
                self.map_widget.delete(self.search_marker)

            address = self.entry.get()
            self.search_marker = self.map_widget.set_address(address, marker=True)
            current_position = self.map_widget.get_position()
            if self.search_marker is False:
                speak('sir; this address is not exit!')
                self.search_marker = None
                
            self.search_in_progress = False

    def save_marker(self):
        if self.search_marker is not None:
            self.marker_list_box.insert(tkinter.END, f" {len(self.marker_list)}. {self.search_marker.text} ")
            self.marker_list_box.see(tkinter.END)
            self.marker_list.append(self.search_marker)

    def clear_marker_list(self):
        for marker in self.marker_list:
            self.map_widget.delete(marker)

        self.marker_list_box.delete(0, tkinter.END)
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


    def search_event0(self, event=None):
        self.map_widget.set_address(self.entry.get())
        self.slider_1.set(self.map_widget.zoom)

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
    if float(customtkinter.__version__) > 3.2:
        print("Please update customtkinter: pip3 install customtkinter --upgrade")
        exit()

    app = App()
    app.start()
