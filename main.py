class Calculator:
    def __init__(self):
        pass

    def add(self, x1, x2):
        return x1 + x2

    def multiply(self, x1, x2):
        return x1 * x2

    def subtract(self, x1, x2):
        return x1 - x2

    def divide(self, x1, x2):
        if x2 != 0:
            return x1 / x2


print ('Приветствуем вас в калькуляторе Python')
q1 = int (input('Введите число x1: '))
q2 = int (input('Введите число x2: '))
calculator = Calculator()

v = int (input('Какую операцию вы хотите выполнить? \n 1 Сложение \n 2 Вычитание \n 3 Деление \n 4 Умножение \n'))

if v == 1:
    t = "сложение"
    r = calculator.add(q1, q2)
if v == 2:
    r = calculator.subtract(q1, q2)
    t = 'вычитания'
if v == 3:
    r = calculator.divide(q1, q2)
    t = 'деления'
if v == 4:
    r = calculator.multiply(q1, q2)
    t = 'умножения'
print ('Результат ', t,' = ', r)