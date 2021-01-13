# File Docx: FF-BlogSpot
# Author: John Cole
# Date: Jan 11, 2021
# Purpose: The FF-BlogSpot is a fantasy football themed blog site.
# This CRUD program incorporates the first use of packages (WTForms, flask_sqlalchemy, flask_bcrypt, flask_login, flask_mail, os, itsdangerous, PIL, secrets)
# This program practices the first-time use of Blueprints, WTForms, TimedJSONWebSignatureSerializer, and PIL.
## Functionality ## 
# It enables a user to register an account and create blog posts under the forum time. 
# Each post is unqiue to the user, and only the current user can update or delete their previous posts. 
# Each account enables the user to update their sign-in credentials, as well as, add a profile picture. 
# A forgot passward feature has been added to enable users to recover their account. 

# ============== Import Statements ============== #
from flaskblog import create_app



app = create_app()



if __name__ == "__main__":
    app.run(debug=True)