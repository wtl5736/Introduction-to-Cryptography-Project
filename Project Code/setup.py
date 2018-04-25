#!/usr/bin/python3

"""
Name: setup.py
Author: Wesley Lee - wtl5736@rit.edu
Assignment: Cryptography Project
Date: 04-23-2018

Description:
	Installs all necessary python modules to run the program successfully.
"""

import sys, platform
from os import *

def setup():
	os = platform.system()
	if os == 'Darwin' or or == 'Linux':
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
		print("Crypto_Project.py can't be ran on", os)
		sys.exit()
setup()
