from tqdm import tqdm
import time

def readLinesFromFile():
	lines = None
	with open('test.py',"r") as f:
		lines = f.read().split('\n')
	return lines

def addModuleTQDM(fileLines):

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


def ModifyFile(fileLines):
	fileLines = addModuleTQDM(fileLines)
	return fileLines

def writeLinesToFile(lines):
	with open('test.py', 'w') as f:
		f.write('\n'.join(lines))

if __name__ == '__main__':
	fileLines = readLinesFromFile()

	ModifyFile(fileLines)
	writeLinesToFile(fileLines)

	# for line in tqdm(range(0, len(fileLines))):
	# 	print(fileLines[line])
