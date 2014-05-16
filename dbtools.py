from google.appengine.ext import db
from crypto import *

#Database Entity
class BlogPosts(db.Model):
	subject = db.StringProperty(required=True)
	content = db.TextProperty(required=True)
	created = db.DateTimeProperty(auto_now_add=True)

	def as_dict(self):
		timeFormat = "%d %b %Y %H:%M:%S"
		d = { 	'subject' : self.subject,
				'content' : self.content,
				'created' : self.created.strftime(timeFormat)}
		return d


class Users(db.Model):	
	username = db.StringProperty(required=True)
	password = db.StringProperty(required=True)
	email    = db.StringProperty()
	joined   = db.DateTimeProperty(auto_now_add=True)

def userExists(username):
    userDB = db.GqlQuery("SELECT * FROM Users Where username=:1", username)
    user = userDB.get()
    if user:
        return True

def verifyUserPassword(username, password):
	#verify the username and password and return user
	userDB = db.GqlQuery("SELECT * FROM Users Where username=:1", username)
	user = userDB.get()
	if user and confirmPassword(user.password, password):
		return user
	else:
		return None