import re

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

def searchVersion(text):

    patterns = [ "Version [0-9]{1,2}\.[0-9]{1,2}\.[0-9]{1,2}"]
    matches = []
  
    for i in patterns:
        matches.append(re.search(i,text))

    version = matches[0].group()
    match2 = re.search("[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{1,2}",version)
    number = match2.group()
    
    return number

def searchROMMON(text):
    patterns = ["R0        [0-9]*            [0-9]{1,2}.[0-9]\([0-9]{1,2}r\)"]
    matches = []

    for i in patterns:
        matches.append(re.search(i,text))
    
    firmware = matches[0].group()
    match2 = re.search("[0-9]{1,2}.[0-9]\([0-9]{1,2}r\)",firmware)
    number = match2.group()

    return number

def versionChecker():
    pass

def findProcessor():
    pass 