first = float(input("Первое число: "))
second = float(input("Второе число: "))
operation = input("Операция (+, -, *, /): ")

if operation == "+":
    print(f"{first + second:.2f}")
elif operation == "-":
    print(f"{first - second:.2f}")
elif operation == "*":
    print(f"{first * second:.2f}")
elif operation == "/":
    if second == 0:
        print("Деление на ноль запрещено")
    else:
        print(f"{first / second:.2f}")
else:
    print("Неизвестная операция")
