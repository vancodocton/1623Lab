# import sys
import pyAesCrypt
import getpass
from os import stat, remove

seperatingLine = "=============================================="
bufferSize = 64 * 1024

# show menu interface
def I_Menu():
    print(seperatingLine)
    print("\tSimple Force Ecryption File")
    print(seperatingLine)
    print(" Option 1: Force to decrypt a file by passguessing")
    print(" Option 2: Force to decrypt a file brute")
    print(" Option 0: Exit")
    print(seperatingLine)

def PassGuess():
    # Enter encrypted file path for decryption
    enFilePath = input(" Enter file path: ")
    print("\t...")
    print(" Processing")
    print("\t...")
    # Open and raise error of file is not existed
    with open("PassGuess.txt", "r") as Passwds:
        pwds = Passwds.read().split('\n')
    for pwd in pwds:
        flag = Decrypt(enFilePath, pwd)
        if (flag == 0 or flag == -1):
            return
    print(" Password guesting is failed")

    

def Decrypt(enFilePath, pwd):
    try:
        with open(enFilePath, "rb") as enFile:
            deFilePath = enFilePath+".txt"
            enFileSize = stat(enFilePath).st_size

            with open(deFilePath, "wb") as deFile:
                enFileSize = stat(enFilePath).st_size
                pyAesCrypt.decryptStream(enFile, deFile, pwd, bufferSize, enFileSize)
                print(" File is decrypted sucessfully")
                print(" File is:", deFilePath)
                print(" Password is:", pwd)
                return 0
    except FileNotFoundError:
        print(" File not found")
        return 0
    except ValueError:
        remove(deFilePath)
        return 1
    except Exception as error:
        print(str(error))
        return -1
        
# Show invalid option message
def I_InvalidOptionMessage():
    print(" Invalid option! Please try again...")

def PassForce():
    print(" The option is unavailable")

def main():
    while (True):
        # Show menu option
        I_Menu()
        # Choose and execute option
        try:
            option = {
                1: PassGuess,
                2: PassForce,
                0: exit
            }
            func = option.get(int(input(" Your option: ")),I_InvalidOptionMessage)
            func()
        except ValueError:
            I_InvalidOptionMessage()
# Run the function main if directly run the script
if __name__ == "__main__":
    main()
