# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141,    10^(-1) ≤ d ≤10^(-10)

num = float(input('Введите число: '))
digits = float(input('Введите вещественное число определяющее точность: '))

count = 0

while digits < 1:
    digits *= 10
    count += 1

print(round(num, count))
