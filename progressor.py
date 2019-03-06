from tqdm import tqdm
import time
import os
import argparse
import sys

# retrieve arguments
def _parse_args():
    parser = argparse.ArgumentParser(description='progressor.py')
    parser.add_argument('-f', type=str, default=None, help='file to add tqdm, is required')
    parser.add_argument('-p', action='store_true', help='permanently add tqdm to the specified file')
    parser.add_argument('-c', action='store_true', help='make a copy of the tqdm file')
    parser.add_argument('-r', action='store_true', help='run the modified file')

    args = parser.parse_args()
    return args

# handles arguments on how add tqdm wrappers, and invalid arguments
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
			args.c = True
	return args

# the file should exist, read the file and put the
# lines into a list to return
def readLinesFromFile():
	lines = None
	with open(args.f,"r") as f:
		lines = f.read().split('\n')
	return lines

# reads the each line in the file, determines if and where
# to include the tqdm import statement 
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

# iterate through the file lines, add tqdm if applicable
def addTQDMLines(fileLines):
	for index, line in enumerate(fileLines):
		if 'for' in line:
			# add tqdm wrapper
			if 'tqdm' not in line:
				fileLines[index] = addTQDMWrapper(line)
	return fileLines

# add tqdm wrapper to the line
# need to determine start of the iterable, and end of iterable
def addTQDMWrapper(line):
	startOfIterable = line.find(' in ') + 3
	endOfIterable = line.find(':')
	if endOfIterable != -1:
		tqdmLine = line[0:startOfIterable + 1] + 'tqdm(' + line[startOfIterable + 1:endOfIterable] + ')' + line[endOfIterable:]
		return tqdmLine
	else:
		return line

def addTQDM(fileLines):
	fileLines = addTQDMModule(fileLines)
	fileLines = addTQDMLines(fileLines)
	return fileLines

# write modified file out
def writeLinesToFile(lines, args):
	# we want a copy of the file
	if args.c:
		args.f = 'tqdm-' + args.f	
	with open(args.f, 'w') as f:
		f.write('\n'.join(lines))

if __name__ == '__main__':

	# get and handle arguments
	args = _parse_args()
	args = handleArguments(args)

	fileLines = readLinesFromFile()

	modifiedFile = addTQDM(fileLines)
	writeLinesToFile(modifiedFile, args)
	
	#optional run program
	if args.r:
		a = os.system("python " + args.f)
