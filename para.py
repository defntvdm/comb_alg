#!/usr/bin/python3


def pvg(v, mt, used, g):
	if used[v]:
		return False
	used[v] = True;
	for i in range(len(g[v])):
		to = g[v][i] - 1
		if mt[to] == -1 or pvg(mt[to], mt, used, g):
			mt[to] = v
			return True
	return False

def main():
	g = []
	numbers = set()

	with open('in.txt', 'r') as f:
		n = int(f.readline())
		for _ in range(n):
			arr = [int(e) for e in f.readline().split()[:-1]]
			numbers = numbers.union(set(arr))
			g.append(arr)
	k = max(numbers)

	mt = [-1 for _ in range(k)]
	for v in range(n):
		used = [False for _ in range(n)]
		pvg(v, mt, used, g)

	indexs = []

	for i in range(n):
		try:
			indexs.append(str(mt.index(i) + 1))
		except:
			pass

	with open('out.txt', 'w') as f:
		if len(indexs) == n:
			f.write('Y\n')
			f.write(' '.join(indexs))
			f.write('\n')
		else:
			f.write('N\n')

if __name__ == '__main__':
	main()
