import json

from dbtools import *
from jinjaEnv import *

class FrontHandler(JinjaHandler):
    def get(self):
    	if self.format == 'html':
    		#render all blog entries
    		blogPosts = db.GqlQuery("SELECT * FROM BlogPosts ORDER BY created DESC")
    		blogPosts = list(blogPosts)
        	self.render("blog.html", blogPosts=blogPosts)
        elif self.format == 'json':
        	self.response.headers['Content-Type'] = 'application/json; charset=UTF-8'
        	blogPosts = db.GqlQuery("SELECT * FROM BlogPosts ORDER BY created DESC")
        	blogPosts = list(blogPosts)
        	listPost = []
        	if blogPosts:
        		for post in blogPosts:
        			listPost.append(post.as_dict())
        	self.write(json.dumps(listPost))