#!/usr/bin/python3

def main():
	neighbours = {}
	with open("in.txt") as f:
		n = int(f.readline())
		for i in range(1, n+1):
			neighbours[i] = [int(s) for s in f.readline().split()][:-1]
	flag = True
	res = []
	visited = []
	all_visited = []
	queue = [1]
	while flag:
		flag = False
		while queue:
			vertex = queue.pop(0)
			if vertex in visited:
				continue
			visited.append(vertex)
			all_visited.append(vertex)
			queue.extend(neighbours[vertex])
		res.append(visited)
		for vertex in neighbours.keys():
			if not vertex in all_visited:
				queue = [vertex]
				visited = []
				flag = True
				break
	with open("out.txt", "w") as f:
		f.write(str(len(res)))
		f.write("\n")
		for lst in res:
			lst.sort()
			lst.append(0)
			lst = [str(a) for a in lst]
			f.write(" ".join(lst))
			f.write("\n")


if __name__ == "__main__":
	main()