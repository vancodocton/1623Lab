import sys
import pyAesCrypt
import getpass
from os import stat, remove

seperatingLine = "======================================="
bufferSize = 64 * 1024

# show menu interface
def I_Menu():
    print(seperatingLine)
    print("\tSimple File Encryptor")
    print(seperatingLine)
    print("Option 1: Encrypt a file")
    print("Option 2: Decrypt a file")
    print("Option 0: Exit")
    print(seperatingLine)

def Encrypt():
    try:
        FilePath = input("Enter file path for encryption: ")

        with open(FilePath, "rb") as File:

            pwd = getpass.getpass("Enter password: ")
            rePwd = getpass.getpass("Re-enter password: ")

            # Validate password before encrypt
            if (pwd != rePwd):
                print("Password entered is not match")     
            else:
                # Encript file with password
                enFilePath = FilePath+".aes"
                with open(enFilePath, "wb") as deFile:
                    pyAesCrypt.encryptStream(File, deFile, pwd, bufferSize)
                    print("File is encrypted sucessfully")
                    print("file is: ", enFilePath) 
    # Show error
    except Exception as error:        
        print(str(error))
                
def Decrypt():
    try:
        enFilePath = input("Enter file path for decryption: ")

        with open(enFilePath, "rb") as enFile:
            deFilePath = enFilePath+".txt"

            pwd = getpass.getpass("Enter password: ")

            try:                    
                with open(deFilePath, "wb") as deFile:
                    enFileSize = stat(enFilePath).st_size
                    pyAesCrypt.decryptStream(enFile, deFile, pwd, bufferSize, enFileSize)
                    print("File is decrypted sucessfully")
                    print("file is: ", deFilePath)  
            except ValueError as error:
                print(str(error))
                remove(deFilePath)       
    except Exception as error:
        print(str(error))

def I_InvalidOptionMessage():
    print("Invalid option! Please try again...")

def main():
    while (True):
        # Show menu option

        I_Menu()
        # Choose and execute option
        try:
            option = {
                1: Encrypt,
                2: Decrypt,
                0: exit
            }
            func = option.get(int(input("Your option: ")),I_InvalidOptionMessage)
            func()
        except ValueError:
            I_InvalidOptionMessage()

if __name__ == "__main__":
    main()
