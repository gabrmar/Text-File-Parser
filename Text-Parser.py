import parser

#Phase 1: Opening file 
showtech = open("Archivos de Prueba/ANB-RTR-WAN-1 sh tech.txt","r")
parsed = open("Parsed Show Tech.txt","w")

#Phase 2: Getting substring using regex
result = parser.filter_text(showtech)
#listed = list(result)

#Phase 3: Save the substring into text file
parser.writer(result,parsed)

#Phase 4: Close object files to clean system buffer 
showtech.close()
parsed.close()

 