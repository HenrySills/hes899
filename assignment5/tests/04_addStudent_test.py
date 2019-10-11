import pytest

studentList = ['Sarah', 'Mike', 'Tom', 'Matt']

def addStudent(name):
    if (name in studentList):
        return False
    else :
        return True

def test_addSuccess():
	assert addStudent('James')

def test_addFail():
	assert addStudnet('Sarah')
