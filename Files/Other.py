import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mFree-Proxy  -  more free proxy servers")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mIntersect-2.5 - Script Creation Utility")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mExit System  -  exit AllHackingTools")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mBack To MainMenu  -  Back to MainMenu")

op=int(raw_input("OthErTo01s: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && bash Files/Proxy/Logo.sh && python2 Files/Proxy/menu.py && cd")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd Intersect-2.5 && python2 Create.py")
elif(op==3):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting System...")
 sys.exit()
elif(op==4):
 os.system("cd")
 os.system("cd AllHackingTools")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mInvalid input. Reloading Tools") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd AllHackingTools")
 os.system("python2 Files/Other.py")



