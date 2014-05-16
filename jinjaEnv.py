import webapp2
import jinja2
import os

from cookietools import *
from dbtools import *


templateDir = os.path.join(os.path.dirname(__file__), 'templates')
jinjaEnv = jinja2.Environment(	loader = jinja2.FileSystemLoader(templateDir),
								autoescape=True)

class JinjaHandler(webapp2.RequestHandler):
	def write(self, *a, **kvpairs):
		if kvpairs:
			self.response.headers['Content-Type'] = 'text/plain'
		self.response.out.write(*a, **kvpairs)

	def renderStr(self, template, **params):
		t = jinjaEnv.get_template(template)
		return t.render(params)

	def render(self, template, **kvpairs):
		self.write(self.renderStr(template, **kvpairs))

	def setSecureCookie(self, name, value):
		cookieVal = makeSecureCookieVal(value)
		self.response.headers.add_header('Set-Cookie', 
							'%s=%s; Path=/' % (name, cookieVal))

	def readSecureCookie(self, name):
		cookieVal = self.request.cookies.get(name)
		if cookieVal and validCookie(cookieVal):
			return long(cookieVal.split('|')[0])

	def login(self, user):
		self.setSecureCookie('user-id', str(user.key().id()))

	def logout(self):
		self.response.delete_cookie('user-id')

	def initialize(self, *a, **kvpairs):
		webapp2.RequestHandler.initialize(self, *a, **kvpairs)
		uid = self.readSecureCookie('user-id')
		self.user = uid and Users.get_by_id(uid)
		if self.request.url.endswith('.json'):
			self.format = 'json'
		else:
			self.format = 'html'
