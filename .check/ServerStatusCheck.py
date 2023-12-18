R = '\033[31m'
G = '\033[32m' 
C = '\033[36m'
W = '\033[0m' 

from shutil import which
import time
import os
import csv
import sys
import json
import argparse
import requests
import subprocess as subp

row = []
info = ''
result = ''
systemR = 'online'

def sys_check():
	print(G + '[+]' + C + ' Checking server Status....', end='')
	sys_url = 'https://raw.githubusercontent.com/mishakorzik/AllHackingTools/main/Castom/ServerStatus.txt'
	try:
		sys_rqst = requests.get(sys_url)
		sys_sc = sys_rqst.status_code
		if sys_sc == 200:
			github_sys = sys_rqst.text
			github_sys = github_sys.strip()

			if systemR == github_sys:
				print(C + '[' + G + ' Online ' + C +']' + '\n')
				print(G + '[+] ' + C + 'Server actived!')
			else:
				print(C + '[' + R + ' Offline ' + C +']' + '\n')
				print(R + '[-] ' + C + 'Server disabled!')
		else:
			print(C + '[' + R + ' Status : {} '.format(sys_sc) + C + ']' + '\n')
	except Exception as e:
		print('\n' + R + '[-]' + C + ' Exception : ' + W + str(e))

try:
	sys_check()
