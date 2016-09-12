#!/usr/bin/env python3

SIZE = {}
NAME = {}
NEXT = {}

def slit(v, w, p, q):
	global NAME, NEXT, SIZE
	NAME[w] = p
	u = NEXT[w]
	while NAME[u]!=p:
		NAME[u] = p
		u = NEXT[u]
	v1 = NEXT[v]
	w1 = NEXT[w]
	NEXT[v] = w1
	NEXT[w] = v1
	SIZE[p] += SIZE[q] 

def main():
	global NAME, NEXT, SIZE
	queue = []
	res = {}
	with open('in.txt') as f:
		n = int(f.readline())
		for v in range(1, n+1):
			res[v] = []
			NAME[v] = v
			NEXT[v] = v
			SIZE[v] = 1
			line = f.readline().split()
			queue.extend([(v, int(w), int(c)) for w, c in zip(line[:-1:2], line[1:-1:2])])
	queue.sort(key=lambda x: x[2])
	ostov = []
	while len(ostov)<n-1:
		v, w, c = queue.pop(0)
		p = NAME[v]
		q = NAME[w]
		if p != q:
			ostov.append((v, w, c))
			#ostov.append((w, v, c))
			if SIZE[q] < SIZE[p]:
				slit(v, w, p, q)
			else:
				slit(w, v, q, p)
	s = 0
	for v, w, c in ostov:
		res[v].append((w, c))
		res[w].append((v, c))
		s += c
	with open('out.txt', 'w') as f:
		for v in range(1, n+1):
			res[v].sort(key=lambda x: x[0])
			for edge in res[v]:
				f.write(' '.join([str(e) for e in edge])+ ' ')
			f.write('\n')
		f.write(str(s)+'\n')



if __name__ == '__main__':
	main()
