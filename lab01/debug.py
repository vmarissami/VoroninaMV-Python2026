# А. Ожидается 5. Сложение строк "2" и "3" давало "23".
first = "2"
second = "3"
print("А. Типы до преобразования:", type(first).__name__, type(second).__name__)
first_number = int(first)
second_number = int(second)
print("А. Типы после преобразования:", type(first_number).__name__, type(second_number).__name__)
print("А. Сумма:", first_number + second_number)

# Б. При вводе 17 ожидается 18. Сложение str и int вызывало TypeError.
age_text = input("Возраст: ")
print("Б. Тип до преобразования:", type(age_text).__name__)
age = int(age_text)
print("Б. Тип после преобразования:", type(age).__name__)
print("Б. Возраст через год:", age + 1)

# В. Ожидается 7.0. Без скобок на 3 делилось только третье число.
first = 4
second = 7
third = 10
average = (first + second + third) / 3
print("В. Среднее:", average)
