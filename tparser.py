import re


#------------------------------Bloque Principal--------------------------------------------------------


def filter_text(file_object): #Función de filtrado del show tech 

    """Esta es la función principal de filtrado. Tiene los patrones fundamentales para filtrar un 
    archivo de show tech"""

    patterns = ["--* show version --*","--* show running-config --*","--* show platform --*",
                "--* show romvar --*","-* show inventory --*","--* show region --*"]
    text = file_object.read()
    matches = []
    borders = []
    substrings = []
    k = 0

    for i in patterns:
        matches.append(re.search(i,text))
    for j in matches:
        borders.append(j.start())

    while k <= len(borders)/2 + 1: #Obtiene porciones del show tech de acuerdo a las fronteras obtenidas
        #Por medio de expresiones regulares
        substrings.append(text[borders[k]:borders[k+1]-1])
        k=k+2
        
    return substrings

def writer(snippet_list,output_file): #Función de escritura de secciones filtradas
    
    for i in snippet_list:
        output_file.write(i)
        output_file.write("\n\n")


#------------------------------Rutinas de ROMMON--------------------------------------------------------

def compareROMMON(suggestedROM,currentROM): #Función de comparación  de versiones de ROMMON
    if len(suggestedROM) == len(currentROM):
        print("Valores de ROMMON aceptados...Iniciando comparación.")
        i=0
        comparator = []
        message = ""
        while i < len(suggestedROM):
            diff = suggestedROM[i] - currentROM[i]
            comparator.append(diff)
            i=i+1
        for i in comparator:
            if i > 0:
                message = "Version actual de ROMMON desactualizada."
                break
        return message
    else:
        print("Las dimensiones de los valores de ROMMON no coinciden. Revisar los valores entregados")
        return None


def ROM2numbers(text): #Esta función extrae los números que componen la versión de ROMMON 

    """El objetivo de esta función es partir el pedazo de la cadena de caracteres que tiene le versión
    de ROMMON en diferntes sub-cadenas para cada uno de las cifras de la versión (normalmente 3 cifras).
    Cada cifra es almacenada en una lista serpada"""

    num = text.split(".")
    num2 = []
    num3 = []
    for i in num:
        match = re.search("[0-9]{1,2}\([0-9]{1,2}r\)",i)
        if match != None: #re.search() entrega un None cuando no encuentra coincidencias para la regex
            num2 = i.split("(")
            index = num.index(i)
            num.pop(index)
    for j in num2:
        match = re.search("[a-z]\)",j)
        if match != None:
            match_text = match.group()
            num3.append(j.replace(match_text,"")) 
            index = num2.index(j)
            num2.pop(index)

    #formatear la lista para que sea una sola lista y no una lista de listas
    numbers = [int(num[0]),int(num2[0]),int(num3[0])]
    return numbers


def ROMMON_Validator(ROMMON):

    """Esta rutina es el cuerpo principal donde se encontrarán las sub-rutinas relacionados con 
    el análisis de la versión de ROMMON"""

    suggestion = open("Suggested ROMMON.txt","r")
    file = suggestion.read()
    version = re.search("[0-9]{1,2}.[0-9]{1,2}\([0-9]{1,2}r\)",file)
    version_text = version.group()
    suggested_numbers = ROM2numbers(version_text) #Obtener los números que componen el ROMMON
    ROMMON_numbers = ROM2numbers(ROMMON) #Lo mismo aquí
    validation = compareROMMON(suggested_numbers,ROMMON_numbers)

    return (version_text,validation)


def searchROMMON(text): #Función de extracción de la versión de ROMMON 
    #  Función central para el manejo de la versión de ROMMON 
    patterns = ["R0        [0-9]*            [0-9]{1,2}.[0-9]\([0-9]{1,2}r\)"]
    matches = []

    for i in patterns:
        matches.append(re.search(i,text))
    
    firmware = matches[0].group()
    match2 = re.search("[0-9]{1,2}.[0-9]\([0-9]{1,2}r\)",firmware) #Removiendo de la línea lo que no tiene
    #que ver con la versión de ROMMON
    number = match2.group()
    #suggested, ROMMON, notes = ROMMON_Validator(number)

    return number

#------------------------------Rutinas de IOS/IOS-XE--------------------------------------------------------

def compareIOS(suggestedIOS,currentIOS): #Función de comparación  de versiones de ROMMON
    if len(suggestedIOS) == len(currentIOS):
        print("Valores de IOS aceptados...Iniciando comparación")
        i=0
        comparator = []
        message = ""
        while i < len(suggestedIOS):
            diff = suggestedIOS[i] - currentIOS[i]
            comparator.append(diff)
            i=i+1
        for i in comparator:
            if i > 0:
                message = "Version actual de IOS/IOS-XE desactualizada."
                break
        return message
    else:
        print("Las dimensiones de los valores de IOS/IOS-XE no coinciden. Por favor revisar los valores entregados")
        return None


    

def IOS2numbers(text_version):#Extracción de números que componen la versión de IOS/IOS-XE

    """El objetivo de esta función es partir el pedazo de la cadena de caracteres que tiene le versión
    de IOS/IOS-XE en diferntes sub-cadenas para cada uno de las cifras de la versión (normalmente 3 cifras).
    Cada cifra es almacenada en una lista serpada"""

    aux = text_version.split(".") # Removindo los puntos de la cadena
    numbers = []
    #formatear la lista para que sea una sola lista y no una lista de listas
    for i in aux:
        numbers.append(int(i))
    return numbers

def searchVersion(text): #Función de extracción de la versión de IOS O IOS-XE
   
    patterns = [ "Version [0-9]{1,2}\.[0-9]{1,2}\.[0-9]{1,2}"]
    matches = []

    for i in patterns:
        matches.append(re.search(i,text))

    version = matches[0].group()
    match2 = re.search("[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{1,2}",version)
    number = match2.group()
    
    return number

def IOSvalidation(IOS):
    
    """Cuerpo principal de rutinas de IOS/IOS-XE"""

    suggestion = open("Suggested IOS or IOS-XE.txt","r") 
    file = suggestion.read()

    version = re.search(" [0-9]{1,2}\.[0-9]{1,2}\.[0-9]{1,2}",file)
    version_text = version.group()
    suggested_numbers = IOS2numbers(version_text)
    IOS_numbers = IOS2numbers(IOS)
    validation = compareIOS(suggested_numbers,IOS_numbers)

    return (IOS_numbers,validation)