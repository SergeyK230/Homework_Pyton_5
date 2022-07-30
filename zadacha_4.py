# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


def First_Iteration_Pack(text1):
    text2 = ''
    mem = text1[0]
    count = 1
    i = 1
    while i < len(text1):
        if mem[0] == text1[i]:
            count += 1
            i += 1
        elif mem[0] != text1[i]:
            text2 = text2 + str(count) + mem[0]
            mem = text1[i]
            count = 1
            i += 1
            if i == len(text1):
                text2 = text2 + str(count) + mem[0]

    return text2

def Second_Iterarion_Pack(text1):
    text2 = ''
    first = -1
    last = -1
    i = 0
    while i < len(text1):
        if first == -1 and text1[i] != '1':
            text2 = text2 + text1[i]
            i += 1
        elif text1[i] == '1' and first == -1:
            first = i
            i += 1
        elif (first != -1 and text1[i].isdigit() and text1[i] != '1') or (i == (len(text1) - 1) and first != -1):
            last = i
            if i != len(text1) - 1:
                mem = text1[first:last]
            else:
                mem = text1[first:]
            mem = mem.replace('1','')
            text2 = text2 + '-' + str(len(mem)) + mem
            first = -1
            last = -1
            if i == len(text1) - 1:
                break
        else:    
            i +=1        
    return text2

def Repack(text1):
    text2 = ''
    i = 0
    coll = ''
    long = 0
    while i < len(text1):
        if text1[i] == '-':
            long = ''
            i += 1
        elif long != 0 and text1[i].isdigit():
            long += text1[i]
            i += 1
        elif long != 0 and not text1[i].isdigit():
            long = int(long)
            text2 += text1[i]
            i += 1
            long -= 1
        elif text1[i].isdigit() and long == 0:
            coll += text1[i]
            i += 1
        elif coll != '' and not text1[i].isdigit():
            text2 += Repack1(text1[i],int(coll))
            coll = ''
            i += 1
    return text2

def Repack1(text1,coll):
    text2 = ''
    for i in range(coll):
        text2 += text1
    return text2

with open('E:\Документы\GeekBrains\Знакомство c Python\homework_5\zadacha_4,1.txt', 'r', encoding='utf-8') as file:
    text1 = file.read()

text1 = First_Iteration_Pack(text1)
text1 = Second_Iterarion_Pack(text1)

with open('E:\Документы\GeekBrains\Знакомство c Python\homework_5\zadacha_4,2.txt', 'w', encoding='utf-8') as file:
    file.write(text1)

with open('E:\Документы\GeekBrains\Знакомство c Python\homework_5\zadacha_4,2.txt', 'r', encoding='utf-8') as file:
    text1 = file.read()

text1 = Repack(text1)

with open('E:\Документы\GeekBrains\Знакомство c Python\homework_5\zadacha_4,3.txt', 'w', encoding='utf-8') as file:
    file.write(text1)