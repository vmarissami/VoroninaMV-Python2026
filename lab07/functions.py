def sum_digits(number):
    """Вернуть сумму цифр модуля целого числа."""
    remaining = abs(number)
    total = 0
    while remaining > 0:
        total += remaining % 10
        remaining //= 10
    return total


def average(numbers):
    """Вернуть среднее или None для пустого списка."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


def normalize_text(text):
    """Привести текст к нижнему регистру и упорядочить пробелы."""
    return " ".join(text.lower().split())


def select_numbers(numbers, threshold):
    """Вернуть числа с модулем не больше порога, сохранив порядок."""
    selected = []
    for number in numbers:
        if abs(number) <= threshold:
            selected.append(number)
    return selected


def is_palindrome(text):
    """Проверить палиндром, игнорируя регистр и обычные пробелы."""
    cleaned = text.lower().replace(" ", "")
    return bool(cleaned) and cleaned == cleaned[::-1]
