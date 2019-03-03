if __name__ == '__main__':
	content = []
	with open('test.py',"r") as f:
		lines = f.read().split('\n')
		print(lines)
		for line in f:
			content.append(line)
	with open('test.py', 'w') as f:
		f.write('\n'.join(['1'] + lines[1:]))
	# print(content)