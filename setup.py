#!/usr/bin/python3

"""
Name: setup.py
Author: Wesley Lee
Assignment: Cryptography Project
Date: 04-23-2018
"""

from os import *

def setup():
	system("clear")
	system("echo Installing Necessary Dependencies to Run Crypto_Project.py")
	system("pip3 install pyqt5 numpy")
	system("echo '\nFinsihed Installing Dependencies...'")
	system("echo To Run Crypto_Project.py: ")
	system("echo '\t\tpython3 Crypto_Project.py\n'")
setup()