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
parsed.close() #Closing the file is necesary to open the file with the changes. This requires more
#Research
parsed = open("Parsed Show Tech.txt","r+")
text = parsed.read()
version = tparser.searchVersion(text)
numbers, validation_1 = tparser.IOSvalidation(version) 
firmware = tparser.searchROMMON(text)
suggested_firm,validation_2 = tparser.ROMMONvalidation(firmware)
parsed.write("\n\n")  #No se puede usar tparser.writer() porque fue diseñado para una lista de sub-cadenas
#de caracteres
parsed.write("---------- Observaciones ----------")
parsed.write("\n\n")
parsed.write(validation_1)
parsed.write("\n\n")
parsed.write(validation_2)

#Phase 4: Close object files to clean system buffer 
showtech.close()
parsed.close()
print("La versión de IOS-XE del equipo es",version) 
print("La versión de ROMMON del equipo es",firmware)
print("La versión recomendada de ROMMMON para es equipo es",suggested_firm)
print("Rutina finalizada con exito")
 