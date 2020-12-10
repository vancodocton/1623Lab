import pyAesCrypt
import sys
from os import stat, remove

# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024

def aes_encrypt():
    # Input file path for encryption
    input_file = input(" Please Input file path for encryption:")
    # Input password from key board
    password = input("Please input your password for AES encryption:")
    # output file will be input_file name + .aes
    output_file = input_file + ".aes"
    # encrypt
    with open(input_file, "rb") as fIn:
        with open(output_file, "wb") as fOut:
            pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)
    print("Your encrypted file is: ", output_file)
    
def aes_decrypt():
    # Input file path for encryption
    input_file = input(" Please Input file path for decryption:")
    # Input password from key board
    password = input("Please input your password for AES decryption:")
    # get encrypted file size
    encFileSize = stat(input_file).st_size
    # Output file will end with .txt
    output_file = input_file + ".txt"
    # decrypt
    with open(input_file, "rb") as fIn:
        try:
            with open(output_file, "wb") as fOut:
                # decrypt file stream
                pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
            print("Your decrypted file is: ", output_file)
            
        except ValueError:
            print("Your password is wrong! Please try again")
            # remove output file on error
            remove(output_file)
            
def main():
    while True:
        print("For encryption please press key 1 \nFor decryption please press key 2 \n")
        select_mode = input("Your selection is: ")
        if select_mode == "1":
            aes_encrypt()
            sys.exit()
        elif select_mode == "2":
            aes_decrypt()
            sys.exit()
        else:
           print("Please input 1 or 2")
           
if __name__ == "__main__":
    main()