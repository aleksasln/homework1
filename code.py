language=input('Выберите язык (A-анлийский В-русский): ') #выбор языка для реализации программы
alphabet='' #переменная для хранения алфавита
if language=='A': #анализ введенного значения
     alphabet='abcdefghijklmnopqrstuvwxyz'
elif language=='B':
    alphabet='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
else:
    print('Неверно выбран язык.')
mode=input('Выберите реежим работы (C-шифрование D-дешифрование): ') #выбор режима работы
text=input('Введите текст: ').lower() #ввод текста
step=int(input('Введите шаг: ')) #ввод шага
result = '' #переменная для хранения результата
if mode=='C': #шифрование
    for c in text:
       result += alphabet[(alphabet.index(c) + step) % len(alphabet)] #формула для шифрования текста с использованием шифра Цезаря
    print('Зашифрованный текст: ', result)
