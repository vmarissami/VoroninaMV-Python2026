# Дополнительное задание. Фотопечать со скидкой.
order_name = input("Название заказа: ")
customer_name = input("Имя заказчика: ")

first_item = input("Название первой позиции: ")
first_quantity = int(input("Количество первой позиции: "))
first_price = float(input("Цена за единицу первой позиции, руб.: "))

second_item = input("Название второй позиции: ")
second_quantity = int(input("Количество второй позиции: "))
second_price = float(input("Цена за единицу второй позиции, руб.: "))

delivery = float(input("Стоимость доставки, руб.: "))
discount_percent = float(input("Скидка, %: "))
payment = float(input("Внесённая сумма, руб.: "))

first_cost = first_quantity * first_price
second_cost = second_quantity * second_price
goods_cost = first_cost + second_cost
discount = goods_cost * discount_percent / 100
total_cost = goods_cost - discount + delivery
total_quantity = first_quantity + second_quantity
change = round(payment - total_cost, 2) + 0.0

print(f"\nЗаказ: {order_name}")
print(f"Заказчик: {customer_name}")
print("Название | Количество | Цена, руб. | Стоимость, руб.")
print(f"{first_item} | {first_quantity} | {first_price:.2f} | {first_cost:.2f}")
print(f"{second_item} | {second_quantity} | {second_price:.2f} | {second_cost:.2f}")
print(f"Товары без доставки: {goods_cost:.2f} руб.")
print(f"Доставка: {delivery:.2f} руб.")
print(f"Скидка: {discount:.2f} руб.")
print(f"Общая сумма со скидкой: {total_cost:.2f} руб.")
print(f"Общее количество: {total_quantity}")
print(f"Внесено: {payment:.2f} руб.")
print(f"Сдача: {change:.2f} руб.")
