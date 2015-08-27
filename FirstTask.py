# -*- coding: utf-8 -*-
# !/usr/bin/env python
__author__ = 'Amir Galimullin 11-406'

import re
import random
import os

# Создаем первые 30 файлов
for i in range(30):
    # Генерируем имя
    name = str(random.randint(10, 50)) + '.' + random.choice(['txt', 'src', 'dat'])
    f = open(name, 'w+')
    f.close()

# Вторая партия 30 файлов
for i in range(30):
    # Генерируем имя
    name = str(random.randint(10, 50)) + '.' + random.choice(['txt', 'src', 'dat'])
    # Проверяем, создан ли файл
    if os.path.exists(name):
        f = open(name, 'w+')
        f.write('old')
        f.close()
    else:
        f = open(name, 'w+')
        f.write('new')
        f.close()
# Получаем список файлов в текущей папке
files = os.listdir('.')
for file in files:
    # Если файл начинается на 1 и имеет расширение txt, то переименовываем
    r = re.match(r'1*.txt', file)
    if r != None:
        newName = file[:len(file) - 4] + '.src'
        os.rename(file, newName)

files = os.listdir('.')
result = {'new': [], 'old': [], '': []}

# Получаем результат
for file in files:
    f = open(file, 'r+')
    str = f.read()
    if str == 'old':
        result['old'].append(file)
    if str == 'new':
        result['new'].append(file)
    if str == '':
        result[''].append(file)
    f.close()

print result
