import pytest

from codeToTest import assignment

def createSuccess():
	assert create('Assignment2')

def createFail():
	assert create('Assignment1')