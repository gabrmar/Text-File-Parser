#Phase 1: Get strings from the txt file
#import os <--- This is for debugging purposes 
#import sys <--- This is for debugging purposes
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
    #snippet = showtech.read(3430) #If we specifiy an amount of bytes as parameter, the buffer will move to the position ahead those bytes,
    #that is to say that repeating the funciton .read() with the byte parameter will provide the next bytes availale.
    #at thhe moment this is a test to define 

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


"""
Not needed at this moment

showtech.seek(120) #Changing the buffer position to 1000 bytes after the start of the text
print("The initial file position is",showtech.tell()) #Testing the .tell() method
snippet = showtech.read(3430) #If we specifiy an amount of bytes as parameter, the buffer will move to the position ahead those bytes,
#that is to say that repeating the funciton .read() with the byte parameter will provide the next bytes availale.
#at thhe moment this is a test to define 
print("The final file position is",showtech.tell()) #Testing the .tell() method
"""
#Interesting Notes

    #Proposal to get the substriing

    #Once the borders are met using RegEx, a while loop can be implemented to collect all the lines until
    #meeting position. The algorithm is presented below:

        #Inputs: position of the initial and final border
        
        #showtech.seek(position)
        #while position < final line:
            
            #snippet = showtech.readlines(1) <--- Verify if this will work
            #showtech.seek(position) <---- Confirm if this is possible


    #Iterable File Object Instances

    #File Object instances are iterable, that is to say they can be used in for loops 
     
#The binary mode on the open() fucnition will allow you to work with non-text files such as images

#About RegEx Module on Python

    #Based on the YouTube tutorial I can get the indeces of the substring which matches the pattern, so
    #I need to confirm if I can use those indices on the Object File instance  on my benefit to get the 
    # show version.
 