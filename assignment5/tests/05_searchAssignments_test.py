import pytest

assignments = ['1', '2', '3']

def found(number):
    if (number in assignments):
        return False
    else :
        return True
        
def notFound(number):
    return False

def test_assignmentFound():
	assert found('1') == True
	
def test_assignmentNotFound():
	assert notFound('6') == False
