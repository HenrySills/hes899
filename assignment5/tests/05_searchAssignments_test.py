import pytest

from codeToTest import searchAssignments

def assignmentFound():
	assert found('1') == True
	
def assignmentNotFound():
	assert notFound('6') == False