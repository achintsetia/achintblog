from jinjaEnv import *

class LogoutHandler(JinjaHandler):
    def get(self):
    		self.logout()
    		self.redirect('/signup')