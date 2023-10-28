import os

from deep_translator import GoogleTranslator


for file in os.listdir(r"text") :
   with open(os.path.join(r"text", file), 'r',encoding="utf-16") as fichier:
      i= fichier.read()
      if "Endou" in i:
          print(fichier)
   fichier.close()
