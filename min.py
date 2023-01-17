# lst=[['D','A','T','A','W'],['B','B','Q','K']]

# n = int(input())

# if n%2:
#     lst[0].sort()
# else:
#     lst[1].sort()
    
# for i in range(2):
#     for j in range(len(lst[i])):
#         print(lst[i][j],end='')
#     print()

lst = [['P','O','T','I','O'],['A','B','C','D','E'],['Y','O','U','R','E']]
lst_choose=[]
a, b = map(int, input().split())
for li in lst:
    for i in range(a,b+1):
        lst_choose.append(li[i])
for i in lst_choose:
    print(i,end='')
