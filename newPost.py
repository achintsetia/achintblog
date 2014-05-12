import datetime
from dbtools import *
from jinjaEnv import *

class NewPostHandler(JinjaHandler):
	def renderNewPost(self, subject="", content="", error=""):
		self.render("newpost.html", subject=subject, content=content,error=error)

	def get(self):
		#Render the empty New Post Template
		self.renderNewPost()		

	def post(self):
		#If all ok add the entry into the db otherwise show problem with the content
		#And redirect on success
		subject = self.request.get("subject")
		content = self.request.get("content")
		if subject and content:
			#Database entry
			dt = datetime.datetime.now()
			key = "%d%d%d%d%d" % (	dt.year, dt.month, dt.day, 
									dt.hour, dt.minute)
			BlogPosts.get_or_insert(key, subject=subject, content=content)
			self.redirect("/"+key)
		else:
			error = "subject and content, please!"
			self.renderNewPost(subject, content, error)