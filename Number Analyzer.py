import parser



def seekROMMON(text):
    pass


#Fase 1: Abrir archivo de interes
parsed = open("Parsed Show Tech.txt","r")
text = parsed.read()
#Fase 2: Selección de los valores numéricos que son de interes
version = parser.searchVersion(text)
print(version)