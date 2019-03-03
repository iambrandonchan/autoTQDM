import time

if __name__ == '__main__':
	content = []
	# with open('test.py',"r") as f:
	# 	lines = f.read().split('\n')
	# 	print(lines)
	# 	for line in tqdm(f):
	# 		content.append(line)
	# with open('test.py', 'w') as f:
	# 	f.write('\n'.join(['1'] + lines[1:]))
	# # print(content)
	# for i in tqdm(range(0, 2000)):
	# 	a = 1+1
	# 	time.sleep(0.01)
	for x in tqdm(range(10000), desc='yo'):
		a = 1
		for y in tqdm(range(5)):
			a = 2
			b = [g for g in tqdm(range(55))]