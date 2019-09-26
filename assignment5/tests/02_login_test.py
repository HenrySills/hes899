import pytest

from codeToTest import login

def login():
	
	user = userSuccess()
	password = passSuccess()
	assert user == 'hes899'
	assert password == 'softEng'
	
def loginFail():

	user = userFail()
	password = passFail()
	assert user == ''
	assert password == 'wrong'