cd
cd
cd AllHackingTools
python3 src/CheckVersion.py
python3 .check/CheckServerYesAndNo.py
sleep 3
clear
g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"
cd
cd
cd AllHackingTools 
mv ErrorServer254NotFound.py MainMenu.py
clear
echo -e $b"[ ✔ ]"$g"succesfull verifined"$w
python2 MainMenu.py
