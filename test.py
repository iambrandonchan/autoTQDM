import time
from tqdm import tqdm

if __name__ == '__main__':
	content = []
	myList = [1,2,3]
	for x in tqdm(range(10000)):
		a = 1
		for y in tqdm(myList):
			a = 2
			b = [g for g in range(55)]