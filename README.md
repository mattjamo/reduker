# Reduker
**Reduker the Reddit comment nuker**

A Python-based GUI application to edit and then wipe all comment history from a Reddit user account.

**File name**: reduker.py  
**Author**: Matthew O'Brien (mattjamo)  
**Created**: 2024-08-18  
**Version**: 1.0  
**Description**: This application allows a user to edit and then wipe all comment history from a specific user account. Generate a 'personal use script' token using Reddit's developer authorized applications webpage and set the global variables below to configure Reduker. Run using `python reduker.py`.

### Global Variable List:
- `_username`: The Reddit username of the account you want to wipe.
- `_password`: The user account password.
- `client_id`: Listed under "personal use script" text.
- `client_secret`: Listed beside "secret" text.
- `_user_agent`: A label to indicate the application using the Reddit API.
- `_phrase`: The text to replace all comments with prior to deletion.
- `_batchSize`: The number of comments to process at a time.

### Dependencies:
- Validated using Python 3.12.5
- PyQt5==5.15.11
- praw==7.7.1

### Installation Instructions:
1. Generate a developer token and ensure adequate permissions are set.
2. Install the dependencies:
   ```bash
   pip install PyQt5==5.15.11
   pip install praw==7.7.1
