import tparser



def seekROMMON(text):
    pass


#Fase 1: Abrir archivo de interes
parsed = open("Parsed Show Tech.txt","r")
text = parsed.read()
#Fase 2: Selección de los valores numéricos que son de interes
version = tparser.searchVersion(text)
ROMMON = tparser.searchROMMON(text)
print("Version:{a}".format(a=version) + "\n" + "ROMMON:{b}".format(b=ROMMON))
