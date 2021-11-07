import os
import sys
import math

def clear():
	os.system("clear")

def banner():
	print('''
\033[1;37m██████╗ ██████╗ ██╗   ██╗████████╗███████╗██████╗  ██████╗ ██╗  ██╗\033[00m
\033[1;36m██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝██╔══██╗██╔═══██╗╚██╗██╔╝\033[00m
\033[1;32m██████╔╝██████╔╝██║   ██║   ██║   █████╗  ██████╔╝██║   ██║ ╚███╔╝ \033[00m
\033[1;33m██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  ██╔══██╗██║   ██║ ██╔██╗ \033[00m
\033[1;33m██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗██████╔╝╚██████╔╝██╔╝ ██╗\033[00m
\033[1;31m╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝\033[0;00m''')

def exit():
	os.system("exit")


clear()
banner()
print("")
print("\033[1;36m======================\033[00m")
print("\033[1;41mDevloped By King-Nazim\033[0;00m")
print("\033[\033[1;36m======================\033[0;00m")
print("")
print("\033[1;4;32m Select Your Option \033[0;0;00m")
print("\033[1;32m1]\033[2;34mInstagram\033[0;00m")
print("\033[1;32m2]\033[2;34mFacebook\033[0;00m")
print("\033[1;32m3]\033[2;34mGmail\033[0;00m")
print("\033[1;32m4]\033[2;34mTwitter\033[0;00m")
print("\033[1;32m5]\033[2;34mNetflix\033[0;00m")
print("\033[1;32m6]\033[2;34mZip\033[0;00m")
print("\033[1;32m7]\033[2;34mDownload A Password List\033[0;00m")
print("\033[1;32m8]\033[3;35mAbout\033[0;00m")
print("\033[1;32m00]\033[3;35mExit\033[0;00m")
main=int(input("\033[32mEnter Your Option: \033[00m"))
if main==1:
	os.system("python core/tools/insta.py")

if main==2:
	os.system("python core/tools/fb.py")

if main==3:
	os.system("python core/tools/gmail.py")

if main==4:
	os.system("python core/tools/twitter.py")

if main==5:
	os.system("python core/tools/netflix.py")

if main==6:
	os.system("python core/tools/zip.py")


if main==7:
	os.system("clear")
	print("\033[35m")
	os.system("figlet RockYou")
	print("\033[00m")
	print("Installing.............")
	os.system("sleep 8")
	os.system("git clone https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt")
	os.system("clear")
	os.system("figlet Installed")
	os.system("sleep 4")
	os.system("python main.py")

if main==8:
	os.system("clear")
	print("\033[36m==================================\033[00m")
	print("      \033[41m Create by King-Nazim \033[00m      ")
	print("\033[36m==================================\033[00m")
	print("\033[31m       ++++++++++++++++++++       \033[32m")
	print('    ,` -.)                  ')
	print('   ( _/-\\-._               ')
	print('  /,|`--._,-^|            , ')
	print('  \_| |`-._/||          , | ')
	print('    |  `-, / |         /  / ')
	print('    |     || |        /  /  ')
	print('     `r-._||/   __   /  /   ')
	print(' __,-<_     )`-/  `./  /    ')
	print(' \   `---    \   / /  /     ')
	print('    |           |./  /      ')
	print('    /           //  /       ')
	print('\_/  \         |/  /        ')
	print(' |    |   _,^- /  /         ')
	print(' |    , ``  (\/  /_         ')
	print('  \,.->._    \X-=/^         ')
	print('  (  /   `-._//^`           ')
	print('   `Y-.____(__}             ')
	print('    |     {__)              ')
	print('          ()   V.1.0        ')
	print("\033[00m")
	print("\033[36m=======================\033[00m")
	print("\033[41mDeveloped By King-Nazim\033[00m")
	print("\033[36m=======================\033[00m")
	print("\033[34m")
	print('''This Is A Bunch Of Brute Force Attacking Tools.''')
	print("\033[00m")
	print("")
	print("")
	print("\033[41m My Social Media:- \033[00m")
	print("\033[32mInstagram            :https://www.instagram.com/nazimcp7/")
	print("Github               :https://www.github.com/King-Nazim/")
	print("Telegram             :https://www.t.me/NazimCp")
	print("Website              :https://nazimcp.ml\033[00m")
	os.system("sleep 5")
	os.system("python main.py")

if main==00:
	exit()



