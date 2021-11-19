from os import read
import tparser

#Phase 1: Opening file 
showtech = open("Archivos de Prueba/ANB-RTR-WAN-1 sh tech.txt","r")
parsed = open("Parsed Show Tech.txt","w+")

#Phase 2: Getting substring using regex
result = tparser.filter_text(showtech) #It returs a list with the substrings we want to write
#on the parsed show tech file

#Phase 3: Save the substring into text file
tparser.writer(result,parsed)

#New phase. Analysis
#parsed.close() #Closing the file is necesary to open the file with the changes. This requires more
#Research
#parsed = open("Parsed Show Tech.txt","r+")
text = parsed.read()
version = tparser.searchVersion(text)


#Phase 4: Close object files to clean system buffer 
showtech.close()
parsed.close()
print("La versión de IOS-XE del equipo es",version)
print("Rutina finalizada con exito")
 