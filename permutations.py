from itertools import permutations as p
x,y = input().split()
in1=int(y)
for i in p(sorted(x),in1):
    print("".join(i))