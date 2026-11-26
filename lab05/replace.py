text = input("Введите текст: ")
replacement_count = text.count(":")
updated = text.replace(":", "-")

print(f"Количество замен: {replacement_count}")
print(f"Новая строка: {updated}")
