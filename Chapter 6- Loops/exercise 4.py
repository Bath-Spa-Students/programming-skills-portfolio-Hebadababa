sandwich_orders=['cheese','salami','egg','lettuce']
finished_sanwiches=[]
while sandwich_orders:
    now_preparing=sandwich_orders.pop(0)
    print(f'i am making your {now_preparing} sandwich')
    finished_sanwiches.append(now_preparing)

print('\n')
for sandwich in finished_sanwiches:
    print('I made your ' + sandwich,' sandwich')