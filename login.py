from jinjaEnv import *
from dbtools import *

class LoginHandler(JinjaHandler):
    def get(self):
			self.render("login.html")
    def post(self):
		username = self.request.get("username")
		password = self.request.get("password")

		user = verifyUserPassword(username, password)
		if user:
			self.login(user)
			self.redirect('/welcome')
		else:
			self.render("login.html", username=username, 
						errorLogin="Invalid Username or Password")