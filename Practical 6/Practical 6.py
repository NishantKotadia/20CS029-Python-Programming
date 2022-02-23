# Name: NISHANT KOTADIA
# ID: 20CS029

from collections import Counter
L=[]
for i in range(int(input())):
    L.append(input())

c=Counter(L)
print(len(c))
for i in c:
    print(c.get(i),end=' ')
print()