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
