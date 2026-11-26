# Вариант 8. Слова с одной кириллической буквой «а».
text = input("Введите текст: ")
match_count = 0

for word in text.split():
    cleaned_word = word.strip(".,!?;:").lower()
    if not cleaned_word:
        continue
    if cleaned_word.count("а") == 1:
        print(cleaned_word)
        match_count += 1

if match_count == 0:
    print("Нет совпадений")
print(f"Количество: {match_count}")
