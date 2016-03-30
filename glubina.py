#!/usr/bin/python3

def main():
	with open("in.txt") as f:
		n = int(f.readline())
		m = int(f.readline())
		field = []
		for _ in range(n):
			field.append([int(e) for e in f.readline().split()])
		x1, y1 = [int(e)-1 for e in f.readline().split()]
		x2, y2 = [int(e)-1 for e in f.readline().split()]
	stack = [(x1, y1)]
	parent = {}
	flag = False
	visited = []
	while stack:
		i, j = stack.pop()
		if i == x2 and j == y2:
			flag = True
			break
		if not (i, j) in visited:
			for a, b in [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]:
				if -1<a<n and -1<b<m and field[a][b] == 0:
					if not (a, b) in visited:
						stack.append((a, b))
						parent[(a, b)] = (i, j)
			visited.append((i, j))
	with open("out.txt", "w") as f:
		if flag:
			res = []
			current = (x2, y2)
			while current != (x1, y1):
				res.append(current)
				current = parent[current]
			res.append((x1, y1))
			res.reverse()
			f.write("Y"+"\n")
			for i, j in res:
				f.write(str(i+1)+" "+str(j+1)+"\n")
		else:
			f.write("N"+"\n")


if __name__ == "__main__":
	main()