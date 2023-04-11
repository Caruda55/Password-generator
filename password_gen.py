import random

digits = '0123456789'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = uppercase_letters.lower()
punctuation = '!#$%&*+-=?@^_'
qw = 'il1Lo0O'
chars = ''

while True:
    kol_vo = input('Количество паролей для генерации?:  ')
    lengt = input('Длинна одного пароля:  ')
    if kol_vo.isdigit() == False or lengt.isdigit() == False:
        print('Обязательное поле, только числа!')
    else:
        break

while True:
    dig = input('Включать ли цифры? "ДА/НЕТ":  ')
    if dig.lower() == 'да':
        chars += digits
    elif dig.lower() == 'нет':
        print('Средняя надёжность')
    let_up = input('Включать ли прописные буквы? "ДА/НЕТ":  ')
    if let_up.lower() == 'да':
        chars += uppercase_letters
    elif let_up.lower() == 'нет':
        print('Средняя надёжность')
    let_low = input('Включать ли строчные буквы? "ДА/НЕТ":  ')
    if let_low.lower() == 'да':
        chars += lowercase_letters
    elif let_low.lower() == 'нет':
        print('Низкая надёжность')
    spec = input('Включать ли символы (!#$%&*+-=?@^_)? "ДА/НЕТ":  ')
    if spec.lower() == 'да':
        chars += punctuation
    elif spec.lower() == 'нет':
        print('Низкая наджность')
    if dig.lower() == 'нет' and let_up.lower() == 'нет' and let_low.lower() == 'нет' and spec.lower() == 'нет':
        print('Введите параметры!')
        continue

    spec_2 = input('Исключать ли неоднозначные символы (il1Lo0O)? "ДА/НЕТ":  ')
    if spec_2.lower() == 'да':
        for i in qw:
            chars = chars.replace(i, '')
    break

def generate_password(arg_1, arg_2):
    password = ''
    for i in range(int(arg_1)):
        password += random.choice(arg_2)
    return password
print('')
print(*[generate_password(lengt, chars) for _ in range(int(kol_vo))], sep='\n')

input()
