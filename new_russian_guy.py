#!/usr/bin/env python3

import re

def main():
	with open('in.txt') as f:
		n, m, start, num = [int(e) for e in f.readline().split(' ')]
		doors = {i: [] for i in range(1, m+1)}
		d = [1000000]*(n+1)
		unvisited = [True]*(n+1)
		matrix = [[0]*(n+1) for _ in range(n+1)]
		for i in range(1, n + 1):
			for door in [int(e) for e in f.readline().split(' ')[1:]]:
				doors[door].append(i)
		costs = [int(e) for e in re.findall('[\d]+', f.read())]
	for door in doors.keys():
		if len(doors[door]) < 2:
			doors[door].append(0)
	for door, v in doors.items():
		matrix[v[0]][v[1]] = costs[door-1]
		matrix[v[1]][v[0]] = costs[door-1]
	for i in range(n+1):
		for j in range(n+1):
			if not matrix[i][j]:
				matrix[i][j] = 1000000
	parent = {start: None}
	for v in range(n+1):
		d[v] = matrix[start][v]
		parent[v] = start
	d[start] = 0
	parent[start] = None
	unvisited[start] = False
	doors = {frozenset(value): key for key, value in doors.items()}
	for _ in range(n):
			k = 1000000
			w = 0
			for v in range(n+1):
				if unvisited[v] and d[v] < k:
					k = d[v]
					w = v
			unvisited[w] = False
			for v in range(n+1):
				if d[w]+matrix[w][v] < d[v] and unvisited[v]:
					d[v] = d[w] + matrix[w][v]
					parent[v] = w
	with open('out.txt', 'w') as f:
		if num < d[0]:
			f.write('N\n')
		else:
			f.write('Y\n')
			f.write(str(d[0])+'\n')
			path = []
			curr = 0
			while curr != start:
				path.append(str(doors[frozenset((curr, parent[curr]))]))
				curr = parent[curr]
			path.reverse()
			f.write(' '.join(path)+'\n')


if __name__ == '__main__':
	main()
