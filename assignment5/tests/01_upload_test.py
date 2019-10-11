import pytest

def uploadSuccess(fileName, fileType):
	file = False
	if fileType == ".txt":
		file = True
		return file

def uploadFail(fileName, fileType):
	file = True
	if fileType != ".txt":
		file = False
		return file



def test_uploadedSuccess():

	upload = uploadSuccess("Assignment", ".txt")	
	
	assert upload == True


def test_uploadFailed():

	upload = uploadFail("Assignment" , ".jpg")
	
	assert upload == True