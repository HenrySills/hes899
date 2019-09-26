import pytest

from codeToTest import upload

def uploadedSuccess():

	upload = upload.uploadSuccess('Assignment', '.txt')	
	
	assert upload == True


def uploadFailed():

	upload = upload.uploadFail('Assignment' , '.jpg')
	
	assert upload == False