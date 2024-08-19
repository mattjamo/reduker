#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File name: reduker.py
Author: Matthew O'Brien
Created: 2024-08-18
Version: 1.0
Description: This application allows a user to edit and than wipe all comment history from 
a specific user account. Generate a 'personal use script' token using a Reddit's developer 
authorized applications webpage and set the global variables below to configure Reduker.

Glonbal Variable List:
_username is the reddit username of the account in which you want to wipe
_password is the user account password
client_id is listed under "personal use script" text
client_secret is listed beside "secret" text
_user_agent is a label to indicate the application using the reddit API
_phrase is the text to replace all comments with prior to deletion
_batchSize is the number of comments to process at a time.

Dependancies:
Validated using Python 3.12.5
PyQt5==5.15.11
praw==7.7.1

Installion Instructions:
Generate developer token, ensure adaquate permissions are set.
pip install PyQt5==5.15.11
pip install praw==7.7.1
"""

# ------Global Variables------
_username       = ''
_password       = ''
_client_id      = ''
_client_secret  = ''
_user_agent     = 'reduker/1.0'
_phrase         = 'be happy'
_batchSize      = 10

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPlainTextEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QThread
import praw
from praw.exceptions import APIException, ClientException, PRAWException
import itertools

def count_iterable(iterable):
    iter1, iter2 = itertools.tee(iterable)
    return sum(1 for _ in iter1), iter2

class Reduker(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Reduker the Reddit Comment Nuker')
        self.setGeometry(100, 200, 800, 800)

        layout = QVBoxLayout()

        buttonLayout = QHBoxLayout()
        deleteButton = QPushButton("Change and Delete Comments")
        deleteButton.clicked.connect(self.deleteComments)
        buttonLayout.addWidget(deleteButton)

        cancelButton = QPushButton("Cancel Deletion")
        cancelButton.clicked.connect(self.cancel_deletion)
        buttonLayout.addWidget(cancelButton)
        layout.addLayout(buttonLayout)

        self.log_output = QPlainTextEdit(self)
        self.log_output.setReadOnly(True)  # Make it non-editable
        self.log_output.setLineWrapMode(QPlainTextEdit.NoWrap)  # Disable line wrapping
        layout.addWidget(self.log_output)

        self.setLayout(layout)
        self.abortNuke = False

    def append_log(self, message):
        self.log_output.appendPlainText(str(message)) # print to gui
        print (str(message)) # print to console
        QApplication.processEvents()

    def deleteComments(self):
        self.abortNuke == False
        if _username:
            try:
                self.append_log("Retrieving and deleting comments commencing...")
                # Create a Reddit instance with your app credentials
                reddit = praw.Reddit(
                    username=_username,
                    client_id=_client_id,
                    client_secret=_client_secret,
                    user_agent=_user_agent,
                    password=_password
                )
                if (reddit.read_only):
                    self.append_log ("Error: reddit in read only mode, check username and password")
                reddit.validate_on_submit = True
                redditor = reddit.redditor(_username)

                while (True):
                    QApplication.processEvents()
                    if (self.abortNuke == True):
                        break
                    comments = redditor.comments.new(limit=_batchSize)
                    count, comments = count_iterable(comments)
                    self.append_log(f"Comment Quantity Received: " + str(count))
                    if count == 0 or comments == None:
                        self.append_log(f"No Additional Comments")
                        break
                    for comment in comments:
                        if (self.abortNuke == True):
                            break
                        self.append_log(f"Comment ID: {comment.id}")
                        self.append_log(f"Comment Body: {comment.body}\n")
                        comment.edit(_phrase)
                        QApplication.processEvents()
                    QThread.sleep(1)
                    QApplication.processEvents()
                    comments = redditor.comments.new(limit=_batchSize)
                    for comment in comments:
                        if (self.abortNuke == True):
                            break
                        self.append_log(f"Comment ID: {comment.id}")
                        self.append_log(f"Comment Body: {comment.body}\n")
                        if comment.body == _phrase:
                            comment.delete()
                            self.append_log("Comment deleted")
                        QApplication.processEvents()
                    self.append_log ("Delete complete. sleeping 15 seconds.")
                    for i in range(15):
                        QApplication.processEvents()
                        if (self.abortNuke == True):
                            break
                        QThread.sleep(1)
                self.append_log("STOPPING")
            except APIException as e:
                print(f"APIException: {e.message}")
            except ClientException as e:
                print(f"ClientException: {e}")
            except PRAWException as e:
                print(f"PRAWException: {e}")
        else:
            self.append_log("Please update your username and password")

    def cancel_deletion(self):
        self.abortNuke == True
        self.append_log("Nuke cancelled!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    reduker = Reduker()
    reduker.show()
    sys.exit(app.exec_())