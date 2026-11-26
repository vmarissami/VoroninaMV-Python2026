text = input("Введите текст: ")
cleaned = text.lower().replace(" ", "")

if not cleaned:
    print("Нет текста")
else:
    is_palindrome = True
    for index in range(len(cleaned) // 2):
        if cleaned[index] != cleaned[-index - 1]:
            is_palindrome = False
            break

    if is_palindrome:
        print("Палиндром")
    else:
        print("Не палиндром")
