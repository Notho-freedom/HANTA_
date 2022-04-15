import pyttsx3 # si ce module n'est pas installer utiliser la commande << pip install pyttsx3 >> dans votre terminal

def speak(texte):
	engine= pyttsx3.init() # initialisation du module
	voices = engine.getProperty('voices') # importe les voix
	engine.setProperty('voice',voices[2].id) # id varie entre 0;1;2;3 et 4 en foction des mises à jours de votre pc
	engine.say(texte) # fait ressortir la voix
	engine.runAndWait() #...

speak("merci d'avoir regarder; aurevoir!")