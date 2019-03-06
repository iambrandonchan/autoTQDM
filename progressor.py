from tqdm import tqdm
import time
import os
import argparse
import sys

def _parse_args():

    parser = argparse.ArgumentParser(description='progressor.py')
    parser.add_argument('-f', type=str, default=None, help='file to add tqdm, is required')
    parser.add_argument('-p', action='store_true', help='permanently add tqdm to the specified file')
    parser.add_argument('-c', action='store_true', help='make a copy of the tqdm file')
    parser.add_argument('-r', action='store_true', help='run the modified file')

    args = parser.parse_args()
    return args

def handleArguments(args):
	# kill the program if there is no such target file
	if args.f == None:
		sys.exit('no such target file..., specify path to file, use -f')
	# need to check if the file exists in the cwd, and if it's a python file
	elif not os.path.isfile(args.f) or not '.py' in args.f:
		sys.exit('invalid file..., must be a .py file')
	# we have a valid file
	else:
		print('success!')
		# we now need to handle the rest of the flags
		if args.p:
			print('p')
		elif args.c:
			print('c')
		elif args.r:
			print('r')
		else:
			print('r')
			args.r == True
	return args


def readLinesFromFile():
	lines = None
	with open(args.f,"r") as f:
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
				fileLines[index] = addTQDMWrapper(line)
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


def writeLinesToFile(lines, args):
	if args.c:
		args.f = 'tqdm-' + args.f	
	with open(args.f, 'w') as f:
		f.write('\n'.join(lines))

if __name__ == '__main__':

	args = _parse_args()
	args = handleArguments(args)

	fileLines = readLinesFromFile()

	modifiedFile = addTQDM(fileLines)
	writeLinesToFile(modifiedFile, args)
	if args.r:
		# print(args.f)
		a = os.system("python " + args.f)
