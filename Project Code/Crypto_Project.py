# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Name: Crypto_Project.py
Author: Wesley Lee - wtl5736@rit.edu
Assignment: Introduction to Cryptography Project
Date Created: 04-02-2018

Description:
    Crypto_Project.py implements a symmetric-key algorithm based on a special class of graphs.

    Encrypts and Decrypts .txt, .py, .java, .c, .asm files
"""

import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from encrypt import encrypt
from decrypt import decrypt
from getA import *


# GUI Class
class App(QDialog):
    # Global Variables
    openedFilePath, password_tbox = "", ""
    plaintext, ciphertext, finalText = "", "", ""

    # Initializes the size of the GUI box
    def __init__(self):
        super().__init__()
        self.title = 'Cryptography Project - Encrypt/Decrypt'
        self.left = 10
        self.top = 20
        self.width = 350
        self.height = 180
        self.initUI()

    # Initializes the GUI
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createGridLayout()

        # Bold Font
        myFont = QFont()
        myFont.setBold(True)

        # Author Label
        self.author_label = QLabel(self)
        self.author_label.setText("By: Wesley Lee - wtl5736@rit.edu")
        self.author_label.setAlignment(Qt.AlignRight)
        self.author_label.move(80, 165)
        self.author_label.resize(250, 350)
        self.author_label.setFont(myFont)

        # Time Label
        self.time_label = QLabel(self)
        self.time_label.setText("")
        self.time_label.setStyleSheet('color: red')
        self.time_label.setAlignment(Qt.AlignRight)
        self.time_label.move(80, 165)
        self.time_label.resize(250, 350)

        # Action Notification
        self.notification = QLabel(self)
        self.notification.setText("")
        self.notification.setStyleSheet('color: blue')
        self.notification.setAlignment(Qt.AlignCenter)
        self.notification.move(40, -150)
        self.notification.resize(250, 350)
        self.notification.setFont(myFont)

        # Grid Box
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        self.show()

    # Grid of Buttons
    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("")
        self.horizontalGroupBox.setStyleSheet("QGroupBox { border: 1px}")
        layout = QGridLayout()

        # File Browser Button
        self.fileBrowse_button = QPushButton("Choose File")
        self.fileBrowse_button.move(100, 100)
        self.fileBrowse_button.clicked.connect(self.openFileNameDialog)

        # Save File Button
        self.saveFile_button = QPushButton("Save File")
        self.saveFile_button.clicked.connect(self.saveFileDialog)

        # Encrypt/Decrypt Buttons
        self.encrypt_button = QPushButton('Encrypt', self)
        self.decrypt_button = QPushButton('Decrypt', self)
        self.encrypt_button.setIcon(QIcon(QPixmap("Pictures/Encrypt.png")))
        self.decrypt_button.setIcon(QIcon(QPixmap("Pictures/Decrypt.png")))
        self.encrypt_button.clicked.connect(self.on_click_encrypt)
        self.decrypt_button.clicked.connect(self.on_click_decrypt)

        # Password textbox
        self.password_tbox = QLineEdit(self)
        self.password_tbox.setPlaceholderText("Enter Password")
        self.password_tbox.setEchoMode(QLineEdit.Password)

        # Picture
        lock_logo = QLabel(self)
        pixmap = QPixmap('Pictures/Transparent_Troll_Face.png')
        lock_logo.setPixmap(pixmap)
        lock_logo.setAlignment(Qt.AlignCenter)

        # Sets grid
        layout.addWidget(self.fileBrowse_button, 0, 0)
        layout.addWidget(lock_logo, 0, 2)
        layout.addWidget(self.password_tbox, 1, 0)
        layout.addWidget(self.encrypt_button, 1, 2)
        layout.addWidget(self.decrypt_button, 2, 2)
        layout.addWidget(self.saveFile_button, 2, 0)
        self.horizontalGroupBox.setLayout(layout)

    # Opens a file from browser
    def openFileNameDialog(self):

        # Open Options
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Encrypted/Decrypted File", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)

        # Sets the opened file path to openedFilePath
        global openedFilePath
        openedFilePath = fileName

        # Error Notification if no file is selected
        if len(fileName) == 0:
            QMessageBox.about(self, "Error Notification", "No File Selected!")
        else:
            # Read in File
            openedFile = open(fileName, 'r')
            openedFile.close()

            # Notification
            if len(fileName) != 0:
                self.notification.setText("Opened: " + os.path.basename(fileName))

    # Saves a file using browser
    def saveFileDialog(self):
        self.time_label.setText("")
        self.author_label.setText("By: Wesley Lee - wtl5736@rit.edu")

        # Save Options
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "Save Encrypted/Decrypted File", "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)

        # Error Notification if no File Destination Selected
        if len(fileName) == 0:
            QMessageBox.about(self, "Error Notification", "File Destination Not Selected!")

        elif len(fileName) > 0:
            global finalText

            # Saves the File
            saveFile = open(fileName, 'w')
            saveFile.write(finalText)

            # Notification of Saved File
            self.notification.setText("Saved: " + os.path.basename(fileName))
            self.password_tbox.clear()
            saveFile.close()

    # Encrypts a File
    def on_click_encrypt(self):
        global plaintext, finalText, openedFilePath

        # Gets File Content
        password = self.password_tbox.text()
        encryptedFile = open(openedFilePath, 'r')
        plaintext = encryptedFile.read()

        # Encrypts File Content
        cipherText, time = encrypt(plaintext, password)
        asciiPW = [ord(b) for b in password]
        A = getA(asciiPW, cipherText)
        L_2 = matmul(A, cipherText)
        newL_2 = [int(a) % 127 for a in L_2]
        finalText = ' '.join(str(x) for x in newL_2)

        # Notification that file has been encrypted
        self.notification.setText("Encrypted: " + os.path.basename(encryptedFile.name))
        encryptedFile.close()

        # Shows Time Taken to Encrypt
        self.time_label.setText(time + " seconds")
        self.author_label.setText("")

    # Decrypts a File
    def on_click_decrypt(self):
        global ciphertext, finalText

        # Gets File Content
        password = self.password_tbox.text()
        encryptedFile = open(openedFilePath, 'r')
        ciphertext = encryptedFile.read()

        # Decrypts File Content
        plainText, time = decrypt(ciphertext, password)
        asciiPW = [ord(b) for b in password]
        A = getA(asciiPW, plainText)
        invA = linalg.inv(A)
        L_2 = matmul(invA, plainText)
        L2_1 = [int(a) % 127 for a in L_2]
        plainTextASCII = [chr(int(a)) for a in L2_1]
        finalText = ''.join(str(x) for x in plainTextASCII)

        # Notification that file has been Decrypted
        self.notification.setText("Decrypted: " + os.path.basename(encryptedFile.name))
        encryptedFile.close()

        # Shows Time Taken to Decrypt
        self.time_label.setText(time + " seconds")
        self.author_label.setText("")


# Runs GUI
def gui_main():
    app = QApplication(sys.argv)
    run = App()
    sys.exit(app.exec_())


if __name__ == '__main__':
    gui_main()
