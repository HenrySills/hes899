import pytest 

def userSuccess():
	username = "hes899"
	return username
	
def passSuccess():
	password = "softEng"
	return password

def userFail():
	username = "henry"
	return username

def passFail():
	password = "wrong"
	return password

def test_login():	
	username = userSuccess()
	password = passSuccess()
	assert username == "hes899"
	assert password == "softEng"
	
	
def test_loginFail():
	username = userFail()
	password = passFail()
	assert username == "hes899"
	assert password == "softEng"
	