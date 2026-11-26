a = int(input("Начало диапазона: "))
b = int(input("Конец диапазона: "))

if a <= b:
    step = 1
else:
    step = -1

for number in range(a, b + step, step):
    print(number)
