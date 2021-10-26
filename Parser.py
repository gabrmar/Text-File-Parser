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

def something():
    test = [ "Version [0-9][0-9].[0-9][0-9].[0-9][0-9]",
    "R0        [0-9]*            [0-9][0-9].[0-9]\([0-9]{1,2}r\)"]
    pass