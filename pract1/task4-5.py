def eratosphere(N):
    if N == 0:
            N = int(input())
    primes = [i for i in range(N + 1)]
    primes[1] = 0
    i = 2
    while i <= N:
        if primes[i] != 0:
            j = i + i
            while j <= N:
                primes[j] = 0
                j = j + i
        i += 1
    primes = [i for i in primes if i != 0]
    print(f"Наибольшее простое число для числа {N} = {primes[-1]}")

def task4(N):
    if type(N) == int and N > 0:
         eratosphere(N)
    elif type(N) == int and N < 0:
        N = N * -1
        eratosphere(N)
    elif type(N) == float:
        N = round(N)
        eratosphere(N)
    elif type(N) == list:
         for i in N:
            if type(i) == int and i > 2:
                eratosphere(i)
            else:
                print("Ошибка, неверный ввод")
                return 0
    else:
         print("Ошибка, неверный ввод")
         return 0

def Test():
    t1 = 'jjgasllglsllaa'
    task4(t1)
    t2 = 10.999283421872
    task4(t2)
    t3 = True
    task4(t3)
    t4 = -10
    task4(t4)
    t5 = [10,11,15,2]
    task4(t5)

Test()
        