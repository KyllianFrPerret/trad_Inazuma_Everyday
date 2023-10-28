import os

from deep_translator import GoogleTranslator


for file in os.listdir(r"text") :
   with open(os.path.join(r"text", file), 'r',encoding="utf-16") as fichier:
      i= fichier.read()
      i= GoogleTranslator(source="ja", target="fr").translate(i)
   with open(os.path.join(r"text", file), 'w',encoding="utf-16") as fichier:
      fichier.write(i)
   fichier.close()



