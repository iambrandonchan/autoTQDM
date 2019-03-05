from tqdm import tqdm
import time
import os


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
				print(fileLines[index])
	# print(fileLines)
	return fileLines



	return fileLines

def addTQDMWrapper(line):
	# print(line.split())
	# print(line)
	startOfIterable = line.find('in') + 2
	endOfIterable = line.find(':')
	if endOfIterable != -1:
		#is a list comprehension rip
		# print(line[0:startOfIterable + 1] + 'tqdm(' + line[startOfIterable + 1:endOfIterable] + ')' + line[endOfIterable:])
		tqdmLine = line[0:startOfIterable + 1] + 'tqdm(' + line[startOfIterable + 1:endOfIterable] + ')' + line[endOfIterable:]
		return tqdmLine
	else:
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
	a = os.system("python test.py")
