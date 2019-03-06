To do list:
	-consider if there is a list comprehension case
	-consider if there is an iter(), iter.next() case
	-add functionality to only tqdm 1 level of for loops, not nested
	-add unit testing?

	-potential bugs:
		-checking if a .py file exists, what about .pyc?, or .py***
		-what if you run this python script from a different folder, or run
		this script on a file in a different folder? -> pathing for writing the file
		might screw up