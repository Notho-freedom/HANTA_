from deep_translator import GoogleTranslator

texte = input("Texte: ")
traduction = GoogleTranslator(source="auto", target="fr").translate(texte)
print(traduction)

traduction_fichier = GoogleTranslator(source="auto", target="fr").translate_file("file.txt")
print(traduction_fichier)

liste = ["Hello! This is some text in English.", "Hola. Bienvenido a mi video youtube."]
traduction_liste = GoogleTranslator(source="auto", target="fr").translate_batch(liste)
print(traduction_liste)
