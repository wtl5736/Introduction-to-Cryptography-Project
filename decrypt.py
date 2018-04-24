#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Name: decrypt.py
Author: Wesley Lee
Assignment: Introduction to Cryptography Project
Date: 04-20-2018

Description:
    Decrypts a file usesing a symmetric-key algorithm based on a special class of graphs.
"""

from time import *
from getA import *

# Initializes the Matrix L1_1
# ciphertext:   Inside contents of ciphertext
# password:     Password used the encrypt file
def decrypt_init(ciphertext, password):

    # Ciphertext and Password
    ciphertext = ciphertext.split(' ')
    ciphertext = [int(x) for x in ciphertext]
    asciiPW = [ord(a) for a in password]
    asciiPW.reverse()
    isEven = False

    # Matrix Stuff
    A = getA(asciiPW, ciphertext)
    invA = linalg.inv(A)
    L_1 = matmul(invA, ciphertext)
    L1_1 = [int(a) % 127 for a in L_1]
    if (len(password) % 2) == 0:
        isEven = True

    return L1_1, asciiPW, isEven

# Decrypts the ciphertext
# ciphertext:   Inside contents of ciphertext
# password:     Password used the encrypt file
def decrypt(ciphertext, password):

    # Start Timer
    startTime = time()

    # Initialize Matrix L1_1
    c, t, isEven = decrypt_init(ciphertext, password)
    n = len(c)
    prime = 127

    # Checks if length of password is even
    if isEven:
        r = 0
        p = c
        l = list(range(n))
    else:
        r = 1
        l = c
        p = list(range(n))

    # Symmetric-key algorithm based on the central map created
    # F(c) = plaintext
    for i in range(0, len(t)):
        if r == 0:
            l[0] = (p[0] - t[i]) % prime
            l[1] = (p[1] + p[0] * l[0]) % prime
            l[2] = (p[2] + p[0] * l[1]) % prime

            for j in range(3, n):
                if (j % 4) == 1 or (j % 4) == 2:
                    l[j] = (p[j] + p[0] * l[j - 2]) % prime
                else:
                    l[j] = (p[j] + p[j - 2] * l[0]) % prime
            r = 1
        else:
            p[0] = (l[0] - t[i]) % prime
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