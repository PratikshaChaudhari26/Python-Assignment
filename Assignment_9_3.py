#Write a program which accept file name from user and create new file named as Demo.
#txt and copy all contents from existing file into new file. Accept file name through command line arguments. 
#Input : ABC.txt Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt 

import os
import sys

def CreateFile(FileName):
    fd = open(FileName, "w")
    if(os.path.exists(FileName)):
        print("File is already existing")
        return
    else:
        fd = open(FileName,"w")   

def Read_File(FileName):
    if(os.path.exists(FileName)):
        fd = open(FileName, "r")
        Data = fd.read()
        print("Data from the file is ")
        print(Data)
    
        fd.close()
        
    else:
        print("File is not existing")
        return

def main():
    
    if (len(argv[1]) != 2):
        print("Error : Invalid number of arguments")
        exit()
    
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        CreateFile(argv[1])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")

if __name__ == "__main__":
    main()



