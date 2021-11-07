import zipfile
import os
import pyfiglet
from tqdm import tqdm
os.system("clear")
print(pyfiglet.figlet_format("Zip-Craker",font="slant"))
print("")
print("Developed By King-Nazim")
print("")
zip_file = input("Enter Zip File: ")
wordlist = input("Enter Wordlist: ")
zip_file = zipfile.ZipFile(zip_file)
nwords = len(list(open(wordlist,"rb")))
print("Number of passwords to test: ",nwords)
with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=nwords, unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("[+] Password found:", word.decode().strip())
            exit()
print("[!] Password not found, try other wordlist.")
