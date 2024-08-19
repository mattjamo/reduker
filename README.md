# reduker
Reduker the Reddit comment nuker

A python based GUI application to edit and than wipe all comment history from a reddit user account.

File name: reduker.py
Author: Matthew O'Brien (mattjamo)
Created: 2024-08-18
Version: 1.0
Description: This application allows a user to edit and than wipe all comment history from 
a specific user account. Generate a 'personal use script' token using Reddit's developer 
authorized applications webpage and set the global variables below to configure Reduker.
Run using "python reduker.py".

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
