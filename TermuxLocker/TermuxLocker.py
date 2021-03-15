#!/usr/bin/python3


#Modules
from stringcolor import * 
import stdiomask
import os,sys
import time
import hashlib

#Colors
green = '\033[32m'


#banner
banner = ("""
 \t\t╔╦╗┌─┐┬─┐┌┬┐┬ ┬─┐ ┬
 \t\t ║ ├┤ ├┬┘││││ │┌┴┬┘
 \t\t ╩ └─┘┴└─┴ ┴└─┘┴ └─
 """)

flag = True

#Menu
def menu():
    print(banner)
    decor = "="
    print(green + decor * 13 + ">" + " [+] Please Choose " + "<" + decor * 13)
    print("""
     1. Register
     2. Login
     3. Exit          
    """)

    
    
#Register   
def Register():
    global user,passwd
    decor = "="
    print(green + decor * 13 + ">" + " [+] Register " + "<" + decor * 13)
    user = input("[*] Enter Your Username: ")
    passwd = stdiomask.getpass('[*] Password: ', mask = '*')
    if len(passwd) <= 6:                                                                #Checking the number of the chars
        print(cs("[!] Password Must Be atleast 6 characters!", "yellow", "#ff0000"))
        exit()
    retype = stdiomask.getpass('[*] Retype Passwd: ', mask = '*')
    if passwd == retype:
        os.chdir('/data/data/com.termux/files/usr/share')
        hash_object = hashlib.md5(passwd.encode())                                      #Hashing the password to md5
        passdb = open("database", "w")                                          #Saving password hashed to database
        passdb.writelines(user +'\n')
        passdb.write(hash_object.hexdigest())
        passdb.close()
        print('[+] Saving Creds to database...')
        time.sleep(5)
        print('[+] Creds saved, Please Open a New Window')
        os.chdir('/data/data/com.termux/files/home')
    else: 
        print(cs("[!] " + user + " Password Doesn't Match! Are you drunk?!", "yellow", "#ff0000"))
    


#Login                      
def Login():
    decor = '='
    print(banner)
    print('\t\t[+] Coded by 1z3n')
    print('\t   [+] Don\'t be a scriptkidie!')
    print('\t' + decor * 13 + '> ' + '[+] Login' + ' <'+ decor * 13 + '\n')
    global flag,passwd,user
    username = input('[*] Username: ')
    password = stdiomask.getpass(prompt='[*] Password : ',mask='*')
    encode = hashlib.md5(password.encode())                             #hashing password input and comparing to the password hashed in database 
    hashed = encode.hexdigest()
    verify =  open('/data/data/com.termux/files/usr/share/database')
    check = verify.readlines()
    verify.close()
    if username + '\n' == check[0] and hashed  == check[1]:
       print('hello?')
       flag = False
    elif hashed != check[1]:
        tries = 0
        while hashed != check[1]:
            retry = stdiomask.getpass(prompt='[*]  Incorrect Password : ',mask='*')
            encode_retry = hashlib.md5(retry.encode())                                      #Encoding retry pass to bytes
            hashed_retry = encode_retry.hexdigest()                                     #Bytes to hash
            tries += 1
            if tries == 3:       #if the attemp of the user is < 3 or tries == 3 then exit 
                print('oppsss')
                Login()
            elif hashed_retry == check [1]:
                flag = False
                print(banner)
                Login()
    else:
        pass


#########
# LOGIN #
#########

if len(sys.argv) >=2:
        arg = sys.argv[1]
        if arg == '-l':
                Login()


###########
#  LOGOUT #
###########

def Logout():
	global flag
	print(banner)
	flag = False
	Logout   
    



########
# MENU #
########

while flag == True:
	main_menu = {1:Register, 2:Login, 3:Logout}
	menu()
	choice = int(input('\nEnter Ther number of your choice : '))
	main_menu[choice]()



    
    
