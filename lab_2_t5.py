a = int(input('Введите целое делимое: '))
b = int(input('Введите целый делитель: '))

if b == 0:
  print('Вы ввели 0 как делитель, математическая ошибка!')
elif a % b == 0:
  print('а делится на b без отстатка, частное равно ', (a / b))
else:
  print('При делении числа а на число b неполное частное равно ', (a / b) , ', а остаток равен', (a % b))