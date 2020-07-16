Name_1 = str(input('Ingrese su nombre: '))
Age_1 = int(input(f'{Name_1} Ingrese su edad: '))
Name_2 = str(input('Ingrese el siguiente nombre: '))
Age_2 = int(input(f'{Name_2} Ingrese su edad: '))


if User_1 > User_2:
    print(f'{Name_1} es mayor')
elif User_1 < User_2:
    print(f'{Name_2} es mayor')
else:
    print ('Tienen la misma edad')