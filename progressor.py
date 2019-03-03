from tqdm import tqdm
import time

def readLinesFromFile():
	lines = None
	with open('test.py',"r") as f:
		lines = f.read().split('\n')
	return lines

def addTQDMModule(fileLines):

	hasTQDMImport = False
	tqdmImport = 'from tqdm import tqdm'
	lastImportLine = 0
	for line in fileLines:
		if tqdmImport in line:
			hasTQDMImport = True
			break
		if 'import' in line:
			lastImportLine += 1
	if not hasTQDMImport:
		#need to insert the import statement
		fileLines.insert(lastImportLine, tqdmImport)
	return fileLines

def addTQDMLines(fileLines):

	for index, line in enumerate(fileLines):
		if 'for' in line:
			if 'tqdm' not in line:
				# add tqdm wrapper
				# print(line)
				fileLines[index] = addTQDMWrapper(line)



	return fileLines

def addTQDMWrapper(line):
	print(line)

	return line


def addTQDM(fileLines):
	fileLines = addTQDMModule(fileLines)
	fileLines = addTQDMLines(fileLines)
	return fileLines

def writeLinesToFile(lines):
	with open('test.py', 'w') as f:
		f.write('\n'.join(lines))

if __name__ == '__main__':
	fileLines = readLinesFromFile()

	modifiedFile = addTQDM(fileLines)
	writeLinesToFile(modifiedFile)

