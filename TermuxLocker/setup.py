# Setup and activation of Termux-Lock

import os,sys

os.chdir('/data/data/com.termux/files/usr/etc')

opr = open('bash.bashrc','a')
opr.write("\nalias txl='python /data/data/com.termux/files/home/TermuxLocker/TermuxLocker/TermuxLocker.py -l'\n")
opr.write('txl\n')
opr.close()

os.system('apt install figlet')
os.system('pip install stdiomask')
os.system('pip install hashlib')
os.system('pip install stringcolor')
os.system('pip install os')
os.system('pip install os-sys')
