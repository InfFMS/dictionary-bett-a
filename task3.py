# Напишите программу, которая получает на вход строку и подсчитывает, 
# сколько раз в ней встречается каждый символ (независимо от регистра).
# Результат нужно вывести без фигурных скобок
# Пример. 
# ввод:
# Абракадабра
# Вывод
# а-5 б-2 д-1 к-1 р-2
def output_dict(dct):
    b = sorted(dct.keys())
    for k in b:
        print(f'{k} - {dct[k]}', end='     ')

s = input().lower()
dct = dict()
for i in range(len(s)):
    if s[i] not in dct:
        dct[s[i]] = 1
    else:
        dct[s[i]] += 1

output_dict(dct)
