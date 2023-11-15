while True:
    toppings=input('enter the toppings of your choice:(or type quit to finish:)')
    if toppings=='quit':
        print('you have customized your pizza toppings')
        break
    else:
        print(f'we will add',(toppings),'to your pizza')