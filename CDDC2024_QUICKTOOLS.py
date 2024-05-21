from time import sleep
import sys,os
# Decoding/Encoding #
import base58
import base64
import binascii
# Search #
import webbrowser

#### SET UP SETTINGS ####
### NOTE TO NEW USERS ###
# YOUR RELATIVE PATH OF CHOICE #
bing_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
webbrowser.register('bing', None,  
                    webbrowser.BackgroundBrowser(bing_path)) 


def drawmainbanner():
    print(",_,_,_,_,_,_,_,_,_,_|______________________________________________________\n\
|#|#|#|#|#|#|#|#|#|#|_____________________________________________________/\n\
      ___  ___   ___    ___          ___     __      ___    _ _    \n\
     / __||   \ |   \  / __|        |_  )   /  \    |_  )  | | |   \n\
    | (__ | |) || |) || (__          / /   | () |    / /   |_  _|  \n\
     \___||___/ |___/  \___|        /___|   \__/    /___|    |_|  \n\
             _____   ___    ___   _     _  __ ___  _____ \n\
            |_   _| / _ \  / _ \ | |   | |/ /|_ _||_   _|\n\
              | |  | (_) || (_) || |__ |   <  | |   | |  \n\
              |_|   \___/  \___/ |____||_|\_\|___|  |_|  \n\
.______________________________________________________|_._._._._._._._._._.\n\
 \_____________________________________________________|_#_#_#_#_#_#_#_#_#_|\n\
\n\
                        ##################\n\
                        ## BY Stickybit ##\n\
                        ##################\n")

def drawsubbanner():
    print("<===================================================================================>\n\
 _____   ___    ___   _           ___  ___  _     ___   ___  _____  ___   ___   _  _ \n\
|_   _| / _ \  / _ \ | |         / __|| __|| |   | __| / __||_   _||_ _| / _ \ | \| |\n\
  | |  | (_) || (_) || |__       \__ \| _| | |__ | _| | (__   | |   | | | (_) || .  |\n\
  |_|   \___/  \___/ |____|      |___/|___||____||___| \___|  |_|  |___| \___/ |_|\_|\n\
          \n\
<===================================================================================>\n\n")


def displayMenu():
    print("\
<=== Quick ===>\n\
a. Decode (Base)\n\
b. Encode (Base)\n\
c. Search (OSINT)\n\n\
<== Misc ==>\n\
1. OSINT\n\
2. Identify cipher\n\
3. Pwn send payload\n")

def quickEncode(string_to_encode):
    # Base64 #
    try:
        print("Attempting Base64 Encryption...")
        encoded_string = base64.b64encode(string_to_encode.encode())
        message = encoded_string.decode()
        print("Success!!!\nEncoded String => " + message)
    except (binascii.Error, ValueError):
        print("Failed.") 
    # Base32 #
    try:
        print("Attempting Base32 Encryption...")
        encoded_string = base64.b32encode(string_to_encode.encode())
        message = encoded_string.decode()
        print("Success!!!\nEncoded String => " + message)
    except (binascii.Error, ValueError):
        print("Failed.")
    # Base16 #
    try:
        print("Attempting Base16 Encryption...")
        encoded_string = base64.b16encode(string_to_encode.encode())
        message = encoded_string.decode()
        print("Success!!!\nEncoded String => " + message)
    except (binascii.Error, ValueError):
        print("Failed.")

    # Base58 #
    try:
        print("Attempting Base58 Encryption...")
        encoded_string = base58.b58encode(string_to_encode.encode())
        message = encoded_string.decode()
        print("Success!!!\nEncoded String => " + message)
    except (binascii.Error, ValueError):
        print("Failed.")

def quickDecode(encrypted_string,lst = []):
    base_encoding = lst
    message = ''
    # Base64 #
    try:
        print("Attempting Base64 Decryption...")
        decrypted_string = base64.b64decode(encrypted_string, validate=True)
        message = decrypted_string.decode()
        base_encoding.append("base64")
        print("Success!!!\nDecrypted String => " + message)
    except (binascii.Error, ValueError):
        print("Failed.") 
    # Base32 #
    try:
        print("Attempting Base32 Decryption...")
        decrypted_string = base64.b32decode(encrypted_string)
        message = decrypted_string.decode()
        base_encoding.append("base32")
        print("Success!!!\nDecrypted String => " + message)
    except (binascii.Error, ValueError):
        print("Failed.")
    # Base16 #
    try:
        print("Attempting Base16 Decryption...")
        decrypted_string = base64.b16decode(encrypted_string)
        message = decrypted_string.decode()
        base_encoding.append("base16")
        print("Success!!!\nDecrypted String => " + message)
    except (binascii.Error, ValueError):
        print("Failed.")
    # Base8 (Hex) #
    try:
        print("Attempting Base8 Decryption...")
        decrypted_string = bytearray.fromhex(encrypted_string)
        message = decrypted_string.decode()
        base_encoding.append("base8")
        print("Success!!!\nDecrypted String => " + message)
    except ValueError:
        print("Failed.")
    
    # Base58 #
    try:
        print("Attempting Base58 Decryption...")
        decrypted_string = base58.b58decode(encrypted_string)
        message = decrypted_string.decode()
        base_encoding.append("base58")
        print("Success!!!\nDecrypted String => " + message)
    except (binascii.Error, ValueError):
        print("Failed.")
    if message != "":
        tryRecursive(message,base_encoding)
    else:
        print("Unknown Base Encoding.")

def tryRecursive(string,lst = []):
    user = input("Try recursive decoding?: ")
    if user.lower() == 'y':
        quickDecode(string,lst)
        return 1
    else:
        print("\nFinal decrypted meesage => ",string)
        print("\nEncoding pattern: ",' => '.join(str(x) for x in lst))
        return 0


 
def quickSearch(keyword):
    print("Opening relevant sites...")
    normal_search = "https://www.bing.com/search?q="+keyword
    map_search = "https://www.google.com/maps/search/"+keyword
    ip_search = "https://www.shodan.io/host/"+keyword
    web_history_search = "https://web.archive.org/web/20240000000000*/"+keyword
    webbrowser.get('bing').open(normal_search, new = 0, autoraise = True)
    webbrowser.get('bing').open(map_search, new = 0)
    webbrowser.get('bing').open(ip_search, new = 0)
    webbrowser.get('bing').open(web_history_search, new = 0)
    print("Visit 'https://osintframework.com/' for more useful OSINT tools...\n")
    print("Other useful sites: 'https://haveibeenpwned.com/'")
    return 0


def main():
    drawmainbanner()
    drawsubbanner()
    displayMenu()
    while True:
        user = input("=> ")
        if user:
            if user.isnumeric():
                if user == '1':
                    pass
                elif user == '2':
                    identify_cipher = "https://www.dcode.fr/cipher-identifier"
                    webbrowser.get('bing').open(identify_cipher, new = 0, autoraise = True)
            else:
                if user.lower() == 'a':
                    encrypted_string = input("Enter encrypted string => ")
                    quickDecode(encrypted_string)
                elif user.lower() == 'b':
                    string_to_encode = input("Enter string to encode => ")
                    quickEncode(string_to_encode)
                elif user.lower() == 'c':
                    keyword = input("Keyword => ")
                    quickSearch(keyword)
                elif user.lower() == 'menu':
                    displayMenu()
                elif user.lower() == 'clr':
                    os.system('cls')
                    main()
                else:
                    continue
        else:
            continue

if __name__ == "__main__":
    main()


def typewriter(line,print_type):
    if print_type.upper() == "F":
        time = 0.01
    elif print_type.upper() == "M":
        time = 0.03
    elif print_type.upper() == "S":
        time = 0.05
    else:
        time = 1
    for char in line:
        print(char, end='')
        sys.stdout.flush()
        sleep(time)
