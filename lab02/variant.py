total = int(input("Общее количество заданий: "))
capacity = int(input("Количество заданий в одном комплекте: "))

full_sets = total // capacity
remainder = total % capacity
minimum_sets = (total + capacity - 1) // capacity

print(f"Полностью заполненных комплектов: {full_sets}")
print(f"Осталось заданий: {remainder}")
print(f"Минимальное число комплектов: {minimum_sets}")
