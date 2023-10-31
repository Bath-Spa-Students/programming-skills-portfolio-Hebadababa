invitation=['william','doraemon','ash ketchum']
print(f'yo',invitation[0],'i am hosting a dinner party at seven tonight, i would be happy if you could attend')
print(f'greetings',invitation[1],'i have been a big fan of your series and i am hosting a dinner party at seven tonight,it would be awesome if youre there')
print(f'good evening',invitation[2],'dinner party at seven please attend thank you')
print(invitation[2],'cant attend the dinner party')
invitation[2]='chota bheem'
print(invitation)
print(f'yo',invitation[0],'i am hosting a dinner party at seven tonight, i would be happy if you could attend')
print(f'greetings',invitation[1],'i have been a big fan of your series and i am hosting a dinner party at seven tonight,it would be awesome if youre there')
print(f'good evening',invitation[2],'dinner party at seven please attend thank you')
print('table wont be arriving in time by dinner, only space for two people')
name=invitation.pop(2)
print((name),'sorry i cant invite you since my table didnt arrive, thank you')
print(f'hey!',invitation[0],'the dinner party is on ,yall are still invited')
print(f'hey!',invitation[1],'the dinner party is on ,yall are still invited')
del invitation[0]
del invitation[0]
print(invitation)