#Вычисление цифрового корня итерационным методом
#ФИО группа

#функция для вычисления цифрового корня
def digital_root(n):
    if n == 0: #если число 0
        return 0 #то его числовой корень 0
    if n % 9 == 0: #если число кратно 9
        return 9 #числовой корень всегда 9
    while n > 9: #в другом случае, пока число > 9
        n -= 9 #уменьшаем его на 9
    return n #остаток и будет цифровым корнем

#dr(0) = 0
#dr(1377) = 9
#dr(2325) = 3

print(digital_root(0))
print(digital_root(1377))
print(digital_root(2325))

#функция содержит 3 блока, функциональным же является только 1. Использование подобных конструкций уступает в эффективности и читаемости рекурсивной реализации