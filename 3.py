#!/usr/bin/python3

def main():
	matr = []
	neigh = {}
	weights = {}
	with open("in.txt") as f:
		n = int(f.readline())
		for _ in range(n):
			matr.append([int(e) for e in f.readline().split()])
		start = int(f.readline())
		end = int(f.readline())
	for i in range(1, n+1):
		neigh[i] = []
		for j in range(1, n+1):
			if matr[i-1][j-1] != -32768:
				neigh[i].append(j)
				weights[(i, j)] = matr[i-1][j-1]
	print(weights)

if __name__ == "__main__":
	main()