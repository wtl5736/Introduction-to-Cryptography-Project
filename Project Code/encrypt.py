#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Name: encrypt.py
Author: Wesley Lee - wtl5736@rit.edu
Assignment: Introduction to Cryptography Project
Date: 04-20-2018

Description:
    Encrypts a file usesing a symmetric-key algorithm based on a special class of graphs.
"""

from time import *
from getA import *

# Initializes the Matrix L1_1
# plaintext:    Inside contents of plaintext
# password:     Password used the encrypt file
def encrypt_init(plaintext, password):
    plaintextASCII = [ord(a) for a in plaintext]
    asciiPW = [ord(b) for b in password]
    A = getA(asciiPW, plaintextASCII)
    L_1 = matmul(A, plaintextASCII)
    newL_1 = [int(a) % 127 for a in L_1]
    return newL_1, asciiPW

# Encrypts the ciphertext
# plaintext:    Inside contents of plaintext
# password:     Password used the encrypt file
def encrypt(plaintext, password):

    # Starts Timer
    startTime = time()

    # Initializes
    p, t= encrypt_init(plaintext, password)
    n = len(p)
    l = list(range(n))
    prime = 127
    r = 0

    # Symmetric-key algorithm based on the central map created
    # F(p) = ciphertext
    for i in range(0, len(password)):
        if r == 0:
            l[0] = (p[0] + t[i]) % prime
            l[1] = (p[1] + p[0] * l[0]) % prime
            l[2] = (p[2] + p[0] * l[1]) % prime

            for j in range(3, n):
                if (j % 4) == 1 or (j % 4) == 2:
                    l[j] = (p[j] + p[0] * l[j - 2]) % prime
                else:
                    l[j] = (p[j] + p[j - 2] * l[0]) % prime
            r = 1

        else:
            p[0] = (l[0] + t[i]) % prime
            p[1] = (l[1] - p[0] * l[0]) % prime
            p[2] = (l[2] - p[0] * l[1]) % prime

            for j in range(3, n):
                if (j % 4) == 1 or (j % 4) == 2:
                    p[j] = (l[j] - p[0] * l[j - 2]) % prime
                else:
                    p[j] = (l[j] - p[j - 2] * l[0]) % prime
            r = 0

    # Stops Timer
    finishTime = time()
    timeTaken = '%f' % (finishTime - startTime)

    if r == 0:
        return p, str(timeTaken)
    elif r == 1:
        return l, str(timeTaken)
