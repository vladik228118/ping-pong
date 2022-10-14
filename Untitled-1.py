age = input('Введи возраст: ')
print(type(age))
while True:
    try:
        age = int(age)
        break
    except:
        print('Эй урод напиши число!')
        age = input('Введи возраст: ')
    
print(type(age))