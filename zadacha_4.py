# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open('E:\Документы\GeekBrains\Знакомство c Python\homework_5\zadacha_4,1.txt', 'r', encoding='utf-8') as file:
    text1 = file.read()

print(text1)
text2 = ''
mem = text1[0]
count = 1
step = 1
first = 0
index_mem = 0
# for i in range(1, len(text1), step):
#     if mem[index_mem] == text1[i]:
#         count += 1
#     else:
#         text2 = text2 + str(count) + mem[index_mem]
#         mem = text1[i]
#         count = 1

for i in range(0, len(text1), step):
    if mem[index_mem] == text1[i]:
        count += 1



print(text2)
