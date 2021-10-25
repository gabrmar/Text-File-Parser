import re

def filter_text(file_object):

    patterns = ["--* show version --*","--* show running-config --*","--* show platform --*",
                   "--* show romvar --*","-* show inventory --*","--* show region --*"]
    pattern1 =  "--* show version --*"
    pattern2 = "--* show running-config --*"
    pattern3 = "--* show platform --*"
    pattern4 = "--* show romvar --*"
    pattern5 = "-* show inventory --*"
    pattern6 = "--* show region --*"
 

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

#Phase 1: Opening file 
showtech = open("Archivos de Prueba/ANB-RTR-WAN-1 sh tech.txt","r")
parsed = open("Parsed Show Tech.txt","w")

#Phase 2: Getting substring using regex
result = filter_text(showtech)
#listed = list(result)

#Phase 3: Save the substring into text file
writer(result,parsed)

#Phase 4: Close object files to clean system buffer 
showtech.close()
parsed.close()

 