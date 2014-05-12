import hashlib

CookieSecret = 'ZAQWS123'

def makeSecureCookieVal(val):
	return '%s|%s' % (val, hashlib.sha256(val+CookieSecret).hexdigest())

def validCookie(cookieVal):
    cookieNow = cookieVal.split('|')[0]
    if cookieVal == makeSecureCookieVal(cookieNow):
        return cookieVal