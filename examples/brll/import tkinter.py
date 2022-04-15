import tkinter
import customtkinter
from tkintermapview import TkinterMapView


class App(customtkinter.CTk):

    APP_NAME = "= =  H . A . N . TA  = ="
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

        self.marker_list = []

        # ============ create two CTkFrames ============

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=500,height=100)
        self.frame_left.grid(row=1, column=1, padx=5, pady=20, sticky="nsew", rowspan=1)

        self.frame_right = customtkinter.CTkFrame(master=self,
                                                  corner_radius=10)
        self.frame_right.grid(row=0, column=1, rowspan=1, pady=20, padx=5, sticky="nsew")

        self.lang=StringVar()
        liste_lang=[]
        combo_search = ttk.Combobox(master=self.frame_left,textvariable=self.lang,font=("times new roman",10),width=6)
        combo_search.grid(row=7,column=0,pady=5,padx=10,sticky="W")

        lang={'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'or': 'odia', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'}
        for kes in lang.keys():
            liste_lang.append(kes)
        combo_search['values']= tuple(liste_lang)
        # ============ frame_left ============

        self.frame_left.grid_rowconfigure(0, minsize=5)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Set",
                                                command=self.set_marker_event,
                                                width=60, height=15,
                                                border_width=0,
                                                corner_radius=8)
        self.button_1.grid(pady=5, padx=10, row=0, column=0)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Clear",
                                                command=self.clear_marker_event,
                                                width=60, height=15,
                                                border_width=0,
                                                corner_radius=8)
        self.button_2.grid(pady=5, padx=10, row=0, column=1)

        # ============ frame_right ============

        self.frame_right.grid_rowconfigure(0, weight=1)
        self.frame_right.grid_rowconfigure(1, weight=0)
        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_columnconfigure(1, weight=0)
        self.frame_right.grid_columnconfigure(2, weight=1)

        self.map_widget = TkinterMapView(self.frame_right, width=450, height=250, corner_radius=9)
        self.map_widget.grid(row=0, rowspan=1, column=0, columnspan=3, sticky="nswe", padx=20, pady=20)
        self.map_widget.set_address("Berlin")

        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            placeholder_text="type address",
                                            width=140,
                                            height=30,
                                            corner_radius=8)
        self.entry.grid(row=1, column=0, sticky="we", padx=20, pady=20)
        self.entry.entry.bind("<Return>", self.search_event)

        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                height=30,
                                                text="Search",
                                                command=self.search_event,
                                                border_width=0,
                                                corner_radius=8)
        self.button_5.grid(row=1, column=1, sticky="w", padx=10, pady=20)

        self.slider_1 = customtkinter.CTkSlider(master=self.frame_right,
                                                width=200,
                                                height=16,
                                                from_=0, to=19,
                                                border_width=5,
                                                command=self.slider_event)
        self.slider_1.grid(row=1, column=2, sticky="e", padx=20, pady=20)
        self.slider_1.set(self.map_widget.zoom)

    def search_event(self, event=None):
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



