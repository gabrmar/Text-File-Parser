import re

def filter_text(file_object):

    pattern1 =  "-* show version -*"
    pattern2 = "Configuration register is 0x.*"
    pattern3 = "-* show inventory _*"
    pattern4 = "-* show region -*"

    text = file_object.read()
    match = re.search(pattern1, text)
    match2 = re.search(pattern2, text)
    match3 = re.search(pattern3, text)
    match4 = re.search(pattern4, text)
    start1 = match.start()
    start2 = match2.start()
    start3 = match3.start()
    start4 = match4.start()
    end1 = match.end()
    end2 = match2.end()

    substring = text[start1:end2]
    substring2 = text[start3:start4-1]

    return (substring,substring2)


#Phase 1: Opening file 
showtech = open("Archivos de Prueba/ANB-RTR-WAN-1 sh tech.txt","r")
parsed = open("Parsed Show Tech.txt","w")

#Phase 2: Getting substring using regex
result = filter_text(showtech)
snippet, snippet2 = result

#Phase 3: Save the substring into text file
parsed.write(snippet)
parsed.write("\n\n\n")
parsed.write(snippet2)

#Phase 4: Close object files to clean system buffer 
showtech.close()
parsed.close()

 