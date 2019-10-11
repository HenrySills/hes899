import pytest

def createAssignment(assignment, list):
    list.append(assignment)

def test_createAssignment():
    assignmentList = ['assignment1','assignment2']
    createAssignment('assignment3', assignmentList)
    assert 'assignment3' in assignmentList

def test_dontCreate():
    assignmentList = ['assignment1','assignment2']
    createAssignment('assignment3', assignmentList)
    assert 'assignment7' in assignmentList
	#assert create('Assignment1')
 
 
 
 
 
 
 
 
 
'''
def createAssignment(assignment):
     if (assignment in assignmentList):
         return True
     else:
         return False

def dontCreate(assignment):
     if (assignment in assignmentList):
         return False
     else:
         return True
'''
