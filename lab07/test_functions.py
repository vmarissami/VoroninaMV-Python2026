from functions import average, is_palindrome, normalize_text, select_numbers, sum_digits

assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""

numbers = [1, 2]
original = numbers.copy()
assert abs(average(numbers) - 1.5) < 1e-9
assert numbers == original
assert normalize_text("\tЗДРАВСТВУЙ,\tМИР!\n") == "здравствуй, мир!"

assert select_numbers([-5, 0, 2, 5], 2) == [0, 2]
assert select_numbers([], 2) == []
assert select_numbers([-4, 3], 2) == []
assert select_numbers([-3, -2, -1, 0, 1, 2, 3], 2) == [-2, -1, 0, 1, 2]
assert select_numbers([-1, 0, 0, 1], 0) == [0, 0]

numbers = [2, 9, -2, 2, 0]
original = numbers.copy()
selected = select_numbers(numbers, 2)
assert selected == [2, -2, 2, 0]
assert numbers == original
assert selected is not numbers

assert is_palindrome("А роза упала на лапу Азора") is True
assert is_palindrome("а    ") is True
assert is_palindrome("") is False
assert is_palindrome("   ") is False
assert is_palindrome("Python") is False
assert is_palindrome("А!") is False
assert is_palindrome("А!а") is True
assert is_palindrome("А\t") is False

print("Все 26 проверок пройдены")
