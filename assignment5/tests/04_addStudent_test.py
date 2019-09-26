import pytest

from codeToTest import student


def addSuccess():
	assert addStudent('James')

def addFail():
	assert addStudnet('Sarah')