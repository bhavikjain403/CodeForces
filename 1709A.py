for _ in range(int(input())):
	x = int(input())
	a = [0] + [int(x) for x in input().split()]
	print("YES" if a[x] != 0 and a[a[x]] != 0 else "NO")