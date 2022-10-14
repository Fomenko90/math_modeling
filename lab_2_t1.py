a = int(input('Введите целое число: '))

if type(a) == int:
  if a % 2 == 0:
    print('Число четное')
  else: print("Число нечетное")