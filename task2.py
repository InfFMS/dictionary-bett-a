# Напишите программу, которая получает на вход строку чисел, разделенных пробелами,
# и формирует словарь,
#  в котором ключами служат числа, а значениями – слово "четное" или "нечетное".

dct = dict()
lst = list(map(int, input().split()))
def check_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

for i in lst:
    if check_even(i):
        dct[i] = "четное"
    else:
        dct[i] = "нечетное"

print(dct)