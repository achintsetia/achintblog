import hashlib
import random
import string

def getSalt():
    #Generates random character string of length 5
    return ''.join( random.choice(string.ascii_letters+string.digits)
                for _ in range(5))

def hashStr(word, salt):
    return hashlib.sha256(word+salt).hexdigest() + '|' + salt

def makePasswordHash(password):
    salt = getSalt()
    return hashStr(password, salt)

def confirmPassword(dbpassword, password):
	salt = dbpassword.split('|')[1]
	if( dbpassword == hashStr(password, salt)):
		return True
	else:
		return False