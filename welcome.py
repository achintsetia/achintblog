from jinjaEnv import *
from cookietools import *
from dbtools import *

class WelcomeHandler(JinjaHandler):
    def get(self):
    	userId = self.readSecureCookie('user-id')
    	if( userId):
    		user = Users.get_by_id(userId)
    		if user:
    			username = user.username    		
    			self.render("welcome.html",username=username)
    	else:
    		self.redirect("/signup")