import time
from tqdm import tqdm

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
	# x = [1,2,3]
	# y = iter(x)
	for x in range(10000):
		a = 1
		for y in range(5):
			a = 2
			b = [g for g in range(55)]