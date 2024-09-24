def fibbonachi():
    a = 0
    b = 1
    while True:
        summa = a+b
        yield summa
        c = a
        a = b
        b = a+c
        #можно было записать как а,б=б,а+б, но я пошёл в пользу наглядности, что нам нужно сохранять предыдущее значение, перед тем как выдавать новое

def indexer(digits):
    index = 0
    fibbonachi_nums = fibbonachi()
    for i in fibbonachi_nums:
        if len(str(i)) <= digits:
            index += 1
        else:
            return index
            
digits = int(input("Введите число значащих цифр: "))

result = indexer(digits) #Важный момент, что наша последовательность Фиббоначи начинается с 1, не с нуля, в ином случае к индексу нужно делать +1
print(result)
