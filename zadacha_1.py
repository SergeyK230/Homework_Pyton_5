# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".



with open('E:\Документы\GeekBrains\Знакомство c Python\homework_5\zadacha_1,1.txt', 'r', encoding='utf-8') as file:
    text = file.read()

text = text.split()

for i in range(len(text)):
    if 'абв' and ',' in text[i]:
        text[i] = ','
    elif 'абв' and '.' in text[i]:
        text[i] = '.'
    elif 'абв' in text[i]:
        text[i] = ''

text = ' '.join( text)
text = text.replace('  ', ' ')
text = text.replace(' ,', ',')
text = text.replace(' .', '.')
with open('E:\Документы\GeekBrains\Знакомство c Python\homework_5\zadacha_1,2.txt', 'w', encoding='utf-8') as file:
    file.write(text)