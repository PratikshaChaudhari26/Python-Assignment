import os
from sys import *
from os.path import exists

def Open_File(path, ):
    os.path.exists(path)
    path_to_file = 'Demo.txt'
    path = path(path_to_file)

    if path.is_file():
        print(f'The file {path_to_file} exists')
    else:
        print(f'The file {path_to_file} does not exist')
        
def main():
    print("Enter the file name to Open")
    Name = input()
    Open_File(Name)

if __name__ == "__main__":
    main()