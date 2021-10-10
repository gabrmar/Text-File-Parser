#Phase 1: Get strings from the txt file
#import os <--- This is for debugging purposes 
#import sys <--- This is for debugging purposes

showtech = open("Archivos de Prueba/ANB-RTR-WAN-1 sh tech.txt","r")
parsed = open("Parsed Show Tech.txt","w")
#Test
#a = "a"
#print("The size of the char is ",sys.getsizeof(a)) <--- This is to get the amount of bytes needed to store a 
#variable/data type


#Phase 2: Filter the string
    #Find the borders of the substring
    #Extract the substring and provide it as filtered string

#Interesting Commands:

    #File_object.readlines() <---- show lines found on the opened file including escape caracthers 
    #File_object.readline() <----- show fisrt line available. If this command is exceuted multiple times, it will always get the next line,
    #that is it won't give you the same line twice.
    #File_obejct.tell() <--- Show the ccurrent position of the file pointer/buffer
    #File_object.seek(position) <--- Move the file pointer/buffer to the position set as parameter 

#Interesting Deployements

    # with open("file.txt", "r") as File_object <--- Using the context manager to invoke the line kind of as a function
        #pass 

    #for line in File_object:
        #print(line, end="") <---- this is a way to read one line at a time and close it if the file object is hanled by a context manager

    #Reading large files 

        #size_to_read = 100

        #contents = File_ibhect.read(size_to_read)
        
        #while len(contents) > 0:
            #print(File_object, end="")
            #content = File_object.read(size_to_read) <--- It will go for the next bytes available 

    #Copying files

        #<snip> <---- Creation of file objext isntances 

        #for line in Read_File_Object:
            #Write_File_Object.write(line)

#Interesting Notes

    #The binary mode on the open() fucnition will allow you to work with non-text files such as images

snippet = showtech.read(3542) # <--- If we specifiy an amount of bytes as parameter, the buffer will move to the position ahead those bytes,
#that is to say that repeating the funciton .read() with the byte parameter will provide the next bytes availale.
#at thhe moment this is a test to define 
print("The file position is",showtech.tell()) # <--- Testing the .tell() method           

#Phase 3: Present filtered string 

#print(snippet)

#Phase 4: Save the filtered data  into a .txt file

parsed.write(snippet)

showtech.close()
parsed.close()
