#!/usr/bin/python3

"""
Name: setup.py
Author: Wesley Lee
Assignment: Cryptography Project
Date: 04-23-2018
"""

import sys, platform
from os import *

def setup():
	os = platform.system()
	if os == 'Darwin':
		system("clear")
		system("echo Installing Necessary Dependencies to Run Crypto_Project.py")
		system("pip3 install PyQt5 numpy")
		system("echo '\nFinsihed Installing Dependencies...'")
		system("echo To Run Crypto_Project.py: ")
		system("echo '\t\tpython3 Crypto_Project.py\n'")
	elif os == 'Windows':
		system("cls")
		system("echo Installing Necessary Dependencies to Run Crypto_Project.py")
		system("py -m pip install PyQt5 numpy")
		system("echo ----------------------------------")
		system("echo Finsihed Installing Dependencies...")
		system("echo To Run Crypto_Project.py: ")
		system("echo 		python3 Crypto_Project.py")
	else:
		print "SMB_Detector.py can't be ran on", os
		sys.exit()
setup()