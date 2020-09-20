language=input('Выберите язык (A-анлийский В-русский): ') #выбор языка для реализации программы
alphabet='' #переменная для хранения алфавита
if language=='A': #анализ введенного значения
     alphabet='abcdefghijklmnopqrstuvwxyz'
elif language=='B':
    alphabet='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
else:
    print('Неверно выбран язык.')
