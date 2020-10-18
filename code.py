while True:
  language=input('Выберите язык (А-анлийский Б-русский): ') #выбор языка для реализации программы
  alphabet='' #переменная для хранения алфавита
  if language=='А': #анализ введеного значения
     alphabet='abcdefghijklmnopqrstuvwxyz'
  elif language=='Б':
    alphabet='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
  while language!='А' and language!='Б':
    print('Неверно выбран язык.')
    convert=input('Попробовать снова?(Да/Нет): ')
    if convert=='Да':
        language=input('Выберите язык (А-анлийский Б-русский): ')
    else:
        break
  mode=input('Выберите режим работы (В-шифрование Г-дешифрование): ') #выбор режима работы
  while mode!='В' and mode!='Г':
    print('Неверно выбран режим.')
    mode=input('Выберите режим работы (В-шифрование Г-дешифрование): ')

  text=input('Введите текст: ').lower() #ввод текста
  step=int(input('Введите шаг: ')) #ввод шага
  result = '' #переменная для хранения результата
  if mode=='В': #шифрование
       for c in text:
              result += alphabet[(alphabet.index(c) + step) % len(alphabet)] #формула для шифрования текста с использованием шифра Цезаря
       print('Зашифрованный текст: ', result)
       result=''
  elif mode=='Г': #дешифрование
       for c in text:
             result += alphabet[(alphabet.index(c) - step) % len(alphabet)] #формула для дешифрования текста с использованием шифра Цезаря
       print('Расшифрованнный текст: ', result)
       result=''
  P=input('Ещё раз?(Да/Нет): ')
  if P=='Да':
      continue
  else:
      print('Пока!')
      break
