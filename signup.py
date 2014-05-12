from jinjaEnv import *
from dbtools import *
from retools import *

class SignUpHandler(JinjaHandler):
    def get(self):
        self.render("signup.html")

    def post(self):
    	username = self.request.get("username")
    	password = self.request.get("password")
    	verify	 = self.request.get("verify")
    	email = self.request.get("email")
    	errorOccured = False

    	if( validUsername(username)):
    		errorUsername = ''        
    	else:
    		errorOccured = True
    		errorUsername = 'That\'s not a valid username.'

        if( userExists(username)):
            errorOccured = True
            errorUsername = 'User already exists!!'

    	if( validPassword(password)):
    		errorPassword = ''
    	else:
    		errorOccured = True
    		errorPassword = 'That wasn\'t a valid password.'

    	if( not email or validEmail(email)):
    		errorEmail = ''
    	else:
    		errorOccured = True
    		errorEmail = 'That\'s not a valid email.'

    	if( password == verify):
    		errorVerify = ''
    	else:
    		errorOccured = True
    		errorVerify = 'Your passwords didn\'t match'

    	if( errorOccured == True):
    		self.render("signup.html", username=username, email=email,
    					 errorUsername=errorUsername, 
    					 errorPassword=errorPassword,
    					 errorVerify=errorVerify,
    					 errorEmail=errorEmail)
    		return

        user = Users(username=username, password=makePasswordHash(password), email=email)
        user.put()
        
        self.login(user)
    	self.redirect("/welcome")