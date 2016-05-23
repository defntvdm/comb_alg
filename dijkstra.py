#!/usr/bin/python3

def main():
	matr = []
	d = []
	parent = {}
	unvisited = []
	with open("in.txt") as f:
		n = int(f.readline())
		for i in range(n):
			unvisited.append(i)
			d.append(0)
			arr = [int(e) for e in f.readline().split()[:-1]]
                        l = [1000000 for _ in range(n)]
                        for j in range(0, len(arr), 2):
                            l[arr[j]-1] = arr[j+1]
			matr.append(l)
		start = int(f.readline())-1
		end = int(f.readline())-1
		d[start] = 0
		parent[start] = None
	unvisited.remove(start)
	for v in unvisited:
		d[v] = matr[start][v]
		parent[v] = start
	for _ in range(n-1):
		k = 1000000
		w = 0
		for vert in unvisited:
			if d[vert] >= 0 and d[vert] < k:
				k = d[vert]
				w = vert
		try:
			unvisited.remove(w)
		except:
			pass
		for v in unvisited:
			if d[w]+matr[w][v]<d[v]:
				d[v] = d[w]+matr[w][v]
				parent[v] = w
	with open("out.txt", "w") as f:
		if d[end] == 1000000:
			f.write("N\n")
		else:
			path = []
			weights = []
			curr = end
			while parent[curr] != None:
				path.append(curr+1)
				weights.append(matr[parent[curr]][curr])
				curr = parent[curr]
			path.append(start+1)
			path.reverse()
			str_path = [str(e) for e in path]
			weights.sort()
			f.write("Y\n")
			f.write(" ".join(str_path)+"\n")
			f.write(str(d[end]))

if __name__ == "__main__":
	main()
