Age=int(input('Enter your age:'))
if Age<2:
    print('you are a baby')
elif Age<4:
    print('you are a toddler')
elif Age<10:
    print('you are a kid')
elif Age<18:
    print('you are a teenager')
elif Age<50:
    print('you are an adult')
else:
    print('you are elder')