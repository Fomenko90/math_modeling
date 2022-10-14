n1 = 1
n2 = 0

s = int(input('Введите количество чисел Фибоначчи: '))

i = 1
print(n1)
print('\n')
print(n2)
print('\n')
while i <= s:
  a = n1 + n2
  n2 = n1
  n1 = a
  i += 1
  print(a)
  print('\n')