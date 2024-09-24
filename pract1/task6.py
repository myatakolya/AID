#Функция в которой и будет проводится отбор комплексный чисел, но с немного хитрым решением))
def answer():
    result = []
    for sublist in numbers:
        for num in sublist:
            if isinstance(num, complex):
                result.append(num)
    result = tuple(result)
    return(result)

#Вторая функция, которую Вы скорее всего хотели бы видеть, но я не очень люблю решения в одну строчку
def answer2():
    result = tuple(num for sublist in numbers for num in sublist if isinstance(num, complex))
    return result

#Создаём произвольный двухуровненый список
numbers = [
    [1, 2.5, 3 + 4j],
    [5, 6.1, 7.5],
    [8 + 2j, 9, 10.0],
    [11j, 12, 13.3]
]

print(answer(numbers))
print(answer2(numbers))