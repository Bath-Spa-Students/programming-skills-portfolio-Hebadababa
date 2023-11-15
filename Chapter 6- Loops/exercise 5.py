sandwich_orders=['cheese','pastrami','salami','pastrami','egg','lettuce','pastrami']
finished_sanwiches=[]

print('deli has ran out of pastrami')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print('\n')
while sandwich_orders:
    preparing_sandwich=sandwich_orders.pop(0)
    print(f'i am making your ' + preparing_sandwich + ' sandwich.')
    finished_sanwiches.append(preparing_sandwich)

print('\n')
for sandwich in finished_sanwiches:
    print('I made your ' + sandwich,  'sandwich.')