import re

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

def validUsername(username):
	return USER_RE.match(username)

def validPassword(password):
	return PASS_RE.match(password)

def validEmail(email):
	return EMAIL_RE.match(email)