# Представьте, что вы шпионы)
# Придумайте шифр, в котором буквы заменяются на какие-то символы
# и реализуйте шифроватор и дешифроватор

alphabet = {
    'а': '@',
    'б': '^',
    'в': '_',
    'г': '+',
    'д': '=',
    'е': '`',
    'ё': '♂', # alt + 11
    'ж': '~',
    'з': '↓', # alt + 25
    'и': '/',
    'й': '|',
    'к': '{',
    'л': '•', # alt + 0149
    'м': '☼', # alt + 15
    'н': ';',
    'о': '♠', # alt + 6
    'п': '♣', # alt + 5
    'р': '*',
    'с': '#',
    'т': '&',
    'у': '→', # alt + 26
    'ф': '←', # alt + 27
    'х': '%',
    'ц': '№',
    'ч': '▲', # alt + 30
    'ш': '$',
    'щ': '☺', # alt + 1
    'ъ': '☻', # alt + 2
    'ы': '◘', # alt + 8
    'ь': '♥', # alt + 3
    'э': '♦', # alt + 4
    'ю': '♪', # alt + 13
    'я': '○' # alt + 9
}

cipher = dict()
for k, j in alphabet.items():
    cipher[j] = k
#print(cipher)
def str_to_cipher(s):
    lst = list(s.lower())
    new_lst = list()
    for i in range(len(lst)):
        if lst[i] in alphabet:
            new_lst.append(alphabet[lst[i]])
        else:
            new_lst.append(lst[i])

    new_s = ''.join(new_lst)
    return new_s

def cipher_to_str(s):
    lst = list(s)
    new_lst = list()
    for i in range(len(lst)):
        if lst[i] in cipher:
            new_lst.append(cipher[lst[i]])
        else:
            new_lst.append(lst[i])

    new_s = ''.join(new_lst)
    return new_s

n = input()
print(str_to_cipher(n))
print(cipher_to_str(str_to_cipher(n)))
