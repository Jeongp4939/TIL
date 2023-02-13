"""
# 삼각관계
lst = {'Amy':'Edger', 'Bob':'Amy', 'Chloe':'Bob','Diane':'Bob', 'Edger':''}
counts = {}
for i in lst.values():
    if i not in counts:
        counts[i]=1
    else:
        counts[i]+=1
max_n=0
max_person = ''
for i in counts.items():
    if i[1]>max_n:
        max_n = i[1]
        max_person=i[0]
print(max_person)
"""
"""
# 보스와 부하들
n = int(input())
nodes = [list(map(int,input().split())) for _ in range(n)]
boss = 0
under = []
for i in range(n):
    if nodes[i][0]==1:
        boss = i

for i in range(n):
    if nodes[0][i] == 1:
        under.append(i)
print(f'boss:{boss}')
print('under:', end='')
print(*under)
"""

