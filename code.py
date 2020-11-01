import logging

logger = logging.getLogger('NewLogger')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('myapp.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.info('Программа начала работу')
while True:
  language=input('Выберите язык (А-анлийский Б-русский): ') #выбор языка для реализации программы
  alphabet='' #переменная для хранения алфавита
  if language=='А': #анализ введеного значения
     logger.info('Выбран анлийский язык')
     alphabet='abcdefghijklmnopqrstuvwxyz'
  elif language=='Б':
    logger.info('Выбран русский язык')
    alphabet='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
  while language!='А' and language!='Б':
    print('Неверно выбран язык.')
    logger.error('Произошла ошибка при выборе языка программы')
    convert=input('Попробовать снова?(Да/Нет): ')
    if convert=='Да':
        language=input('Выберите язык (А-анлийский Б-русский): ')
        if language=='А': #анализ введеного значения
            logger.info('Выбран анлийский язык')
            alphabet='abcdefghijklmnopqrstuvwxyz'
        elif language=='Б':
            logger.info('Выбран русский язык')
            alphabet='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    else:
        break
  mode=input('Выберите режим работы (В-шифрование Г-дешифрование): ') #выбор режима работы
  while mode!='В' and mode!='Г':
    print('Неверно выбран режим.')
    logger.error('Произошла ошибка при выборе режима программы')
    mode=input('Выберите режим работы (В-шифрование Г-дешифрование): ')

  text=input('Введите текст: ').lower() #ввод текста
  step=int(input('Введите шаг: ')) #ввод шага
  result = '' #переменная для хранения результата
  logger.info('Введенный текст: %s ; введенный шаг: %s ' % (text, step))
  if mode=='В': #шифрование
       logger.info('Выбран режим: шифрование')
       for c in text:
              result += alphabet[(alphabet.index(c) + step) % len(alphabet)] #формула для шифрования текста с использованием шифра Цезаря
       logger.info('Выведен зашифрованый текст: %s ' % result)
       print('Зашифрованный текст: ', result)
       result=''
  elif mode=='Г': #дешифрование
       logger.info('Выбран режим: дешифрование')
       for c in text:
             result += alphabet[(alphabet.index(c) - step) % len(alphabet)] #формула для дешифрования текста с использованием шифра Цезаря
       logger.info('Выведен расшифрованый текст: %s ' % result)
       print('Расшифрованнный текст: ', result)
       result=''
  P=input('Ещё раз?(Да/Нет): ')
  if P=='Да':
      logger.info('Программа продолжает работу')
      continue
  else:
      print('Пока!')
      logger.info('Программа закончила работу')
      break
