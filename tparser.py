import re

def ROM2numbers(text):
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
    numbers = [num,num2,num3]

    return numbers

            

def filter_text(file_object):

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

    while k <= len(borders)/2 + 1: #colocar notas al respecto de como funciona este ciclo
        substrings.append(text[borders[k]:borders[k+1]-1])
        k=k+2
        
    return substrings

def writer(snippet_list,output_file):
    
    for i in snippet_list:
        output_file.write(i)
        output_file.write("\n\n")

def versionChecker(version):
    pass

def ROMMON_Validator(ROMMON):
    suggestion = open("Suggested ROMMON.txt","r")
    file = suggestion.read()
    version = re.search("[0-9]{1,2}.[0-9]{1,2}\([0-9]{1,2}r\)",file)
    version_text = version.group()
    suggested_numbers = ROM2numbers(version_text)
    ROMMON_numbers = ROM2numbers(ROMMON)

    return (suggested_numbers,ROMMON_numbers,version_text)

def compareROMMON(suggestedROM,currentROM):
    pass

def searchROMMON(text):
    patterns = ["R0        [0-9]*            [0-9]{1,2}.[0-9]\([0-9]{1,2}r\)"]
    matches = []

    for i in patterns:
        matches.append(re.search(i,text))
    
    firmware = matches[0].group()
    match2 = re.search("[0-9]{1,2}.[0-9]\([0-9]{1,2}r\)",firmware)
    number = match2.group()
    suggested, ROMMON, notes = ROMMON_Validator(number)
    print(suggested)
    print(ROMMON)

    return (number,notes)

def searchVersion(text):

    patterns = [ "Version [0-9]{1,2}\.[0-9]{1,2}\.[0-9]{1,2}"]
    matches = []
  
    for i in patterns:
        matches.append(re.search(i,text))

    version = matches[0].group()
    notes = versionChecker(version)
    match2 = re.search("[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{1,2}",version)
    number = match2.group()
    
    return number