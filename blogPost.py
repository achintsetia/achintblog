import json

from dbtools import *
from jinjaEnv import *

class BlogPostHandler(JinjaHandler):
	def get(self, key):
		if self.format == 'html':
			#get the key and render the page
			post = BlogPosts.get_by_key_name(key)
			if post:
				self.render("blogentry.html", subject=post.subject,
							created=post.created, content=post.content)
			else:
				self.write("No Blog Entry for this key")
		elif self.format == 'json':
			self.response.headers['Content-Type'] = 'application/json; charset=UTF-8'			
			post = BlogPosts.get_by_key_name(key)
			if post:
				self.write(json.dumps(post.as_dict()))