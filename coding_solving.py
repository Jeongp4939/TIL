# orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
# orders = list(orders.split(','))

# order_set = list(set(orders))
# cnt = 0
# for i in order_set:
#     cnt += orders.count(i)
#     while i in orders:
#         orders.remove(i)
        
# print(f'총 {cnt}잔')
# print(sorted(order_set,reverse=True))


orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
orders = list(orders.split(','))

order_set = list(set(orders))
cnt = 0
for i in orders:
    if '아이스' in i:
        cnt += 1
print(f'아이스 음료 : 총 {cnt}잔\n')

for i in order_set:
    print(i, orders.count(i))
    while i in orders:
        orders.remove(i)
        
