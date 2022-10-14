a = int(input('Введите число: '))
b = int(input('Введите сколько в данном числе цифр: '))

i = 0
k = b - 1
c = b - 1
s = 0
ak  = 0

while i <= b:
  s = (a % 10 ** c) * 10 ** k
  k -= 1
  c -= 1
  i += 1
  ak = s
print(ak)