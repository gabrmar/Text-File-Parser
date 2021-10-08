#Phase 1: Get strings from the txt file
#import os <--- This is for debugging purposes 

showtech = open("Archivos de Prueba/ANB-RTR-WAN-1 sh tech.txt","r")
snippet = showtech.read()

#Phase 2: Filter the string
    #Find the borders of the substring
    #Extract the substring and provide it as filtered string
#Phase 3: Present filtered string 

print(snippet)

#Phase 4: Save the filtered data  into a .txt file

showtech.close()

