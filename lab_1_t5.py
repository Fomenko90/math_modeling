a = 'Шляпка гриба, покрытая ... кожиц..., держится на ... ножк.... Снизу Шляпка затянута ... пленкой. Когда ее уберешь, откроется нижняя ... сторона шляпк....'

a1 = 'Шляпка гриба, '

a2 = "покрытая "

a3 = '...'

b = ' '

b4a = "кожиц"

b5a = "..."

b6a = ", держится на "

b7a = "... "

c = ' '

b8a = "ножк"

b9a = "..."

b10a = ". Снизу шляпка затянута "

b11a = "..."

b12a = "пленкой. Когда ее уберешь, откроется нижняя "

b13a = "..."

f = ' '

b14a = "сторона шляпк"

b15a = '...'

b16a = '.'

print(a)

a3 = input('Введите первое пропущенное слово: ')

b5a = input('Введите пропущенную букву в слове кожица: ')

b7a = input('Введите второе пропущенное слово: ')

b9a = input('Введите пропущенную букву в слове ножка: ')

b11a = input('Введите третье пропущенное слово: ')

b13a = input('Введите четвертое пропущенное слово: ')

b15a = input('Введите пропущенную букву в слове шляпка: ')

print(a1 + a2 + a3 + b + b4a + b5a + b6a + b7a + c + b8a + b9a + b10a + b11a + b12a + b13a + f + b14a + b15a + b16a)