from math import gcd

class Frac:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Знаменаель не может быть равен нулю.")
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()  # Упростить дробь при создании

    def simplify(self):
        common_divisor = gcd(self.numerator, self.denominator) #использовал gcd, чтобы не искать наибольший общий делитель в отдельном блоке кода
        self.numerator //= common_divisor
        self.denominator //= common_divisor
        
        # Знаменатель всегда положителен
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    # Сложение дробей
    def __add__(self, other):
        if isinstance(other, Frac):
            new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
            new_denominator = self.denominator * other.denominator
            return Frac(new_numerator, new_denominator)
        return NotImplemented
    
    # Умножение дробей
    def __mul__(self, other):
        if isinstance(other, Frac):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Frac(new_numerator, new_denominator)
        return NotImplemented
    
    # Обратная дробь
    def reciprocal(self):
        if self.numerator == 0:
            raise ValueError("Обратная дробь для нулевой дроби не определена.")
        return Frac(self.denominator, self.numerator)

a1 = int(input("Введите числитель для первой дроби: "))
b1 = int(input("Введите знаменатель для первой дроби: "))
a2 = int(input("Введите числитель для второй дроби: "))
b2 = int(input("Введите знаменатель для второй дроби: "))

frac1 = Frac(a1, b1)  
frac2 = Frac(a2, b2)  


result_add = frac1 + frac2
print(f"Сложение: {frac1} + {frac2} = {result_add}")

result_mul = frac1 * frac2
print(f"Умножение: {frac1} * {frac2} = {result_mul}")

reciprocal_frac1 = frac1.reciprocal()
print(f"Обратная дробь для {frac1} = {reciprocal_frac1}")
reciprocal_frac2 = frac2.reciprocal()
print(f"Обратная дробь для {frac2} = {reciprocal_frac2}")