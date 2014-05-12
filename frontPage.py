from dbtools import *
from jinjaEnv import *

class FrontHandler(JinjaHandler):
    def get(self):
    	#render all blog entries
    	blogPosts = db.GqlQuery("SELECT * FROM BlogPosts ORDER BY created DESC")
        self.render("blog.html", blogPosts=blogPosts)