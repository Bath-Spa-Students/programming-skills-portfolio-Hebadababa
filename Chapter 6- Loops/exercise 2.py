while True:
    age=input('Enter your age:')
    if age=='quit':
        break
    age=int(age)
    if age<3:
        print('your entry is free')
    elif 3 <=age<=12:
        print('your ticket costs 10$')
    elif 12<=age:
        print('your ticket costs 15$ ')
    else:
        break
    