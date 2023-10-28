import os




for file in os.listdir(r"text") :
   with open(os.path.join(r"text", file), 'r',encoding="utf-16") as fichier:
      i= fichier.read()
      if "é" in i:
         i=i.replace("é","e")
      with open(os.path.join(r"text", file), 'w',encoding="utf-16") as fichier:
         fichier.write(i)
   fichier.close()
