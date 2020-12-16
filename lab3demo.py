import sys
import pyAesCrypt
import getpass
from os import stat, remove

seperatingLine = "======================================="
bufferSize = 64 * 1024

# show menu interface
def I_Menu():
    print(seperatingLine)
    print("\tSimple File Encryption ")
    print(seperatingLine)
    print("Option 1: Encrypt a file")
    print("Option 2: Decrypt a file")
    print("Option 0: Exit")
    print(seperatingLine)

def Encrypt():
    try:
        # Enter origin file path for encryption
        FilePath = input("Enter file path for encryption: ")
        # Open and raise error of file is not existed
        with open(FilePath, "rb") as File:
            # Enter password to encrypt
            pwd = getpass.getpass("Enter password: ")
            rePwd = getpass.getpass("Re-enter password: ")

            # Verify  password before encrypt
            if (pwd != rePwd):
                print("Password entered is not match")     
            else:
                # Once acceptable ertification, encrypt file with password
                enFilePath = FilePath+".aes"
                # Write file regardless the file is exist or not
                with open(enFilePath, "wb") as deFile:
                    pyAesCrypt.encryptStream(File, deFile, pwd, bufferSize)
                    print("File is encrypted sucessfully")
                    print("file is: ", enFilePath) 
    # Show error 
    except Exception as error:        
        print(str(error))
                
def Decrypt():
    try:
        # Enter encrypted file path for decryption
        enFilePath = input("Enter file path for decryption: ")
        # Open and raise error of file is not existed
        with open(enFilePath, "rb") as enFile:
            # Enter password of encrypted file
            pwd = getpass.getpass("Enter password: ")

            try:
                # Encrypt file with entered password                
                deFilePath = enFilePath+".txt"
                with open(deFilePath, "wb") as deFile:
                    enFileSize = stat(enFilePath).st_size
                    pyAesCrypt.decryptStream(enFile, deFile, pwd, bufferSize, enFileSize)
                    print("File is decrypted sucessfully")
                    print("file is: ", deFilePath)
            # Raise error if decription is failed
            except ValueError as error:
                print(str(error))
                remove(deFilePath)       
    # Raise another errors
    except Exception as error:
        print(str(error))

# Show invalid option message
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
# Run the function main if directly run the script
if __name__ == "__main__":
    main()
