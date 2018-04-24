#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Name: getA.py
Author: Wesley Lee
Assignment: Introduction to Cryptography Project
Date: 04-23-2018

Description:
	Gets the Central Map that will be used in both the encryption and decryption process.
"""

from numpy import *

# Sets the number in the 'A' matrix, can only be in first column of matrix
# If the index = 1, leave it as 1
# If the index = 0, set it as 1
def set_num(x, matrix):
	if matrix[x][0] == 0:
		matrix[x][0] = 1
		return

# Creates the Central Map
def getA(password, plaintext):

	# Creates an Identity matrix based on the length of the plaintext/ciphertext
	A = eye(len(plaintext), dtype=int)

	# Modulos by the length of the plaintext
	modPW = [int(a) % len(plaintext) for a in password]

	# Loops through modPW and sets a 1 on the specific row
	for x in range(len(modPW)):
		idx = modPW[x]
		set_num(idx, A)
	return A
