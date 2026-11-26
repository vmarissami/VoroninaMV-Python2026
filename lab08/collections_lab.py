def word_counts(text):
    counts = {}
    for word in text.lower().split():
        cleaned = word.strip(".,!?;:")
        if cleaned:
            counts[cleaned] = counts.get(cleaned, 0) + 1
    return counts


def print_word_counts(counts):
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")


def common_topics(first, second):
    return sorted(set(first) & set(second))


def all_topics(first, second):
    return sorted(set(first) | set(second))


def totals_by_category(records):
    totals = {}
    for record in records:
        category = record["category"]
        totals[category] = totals.get(category, 0) + record["amount"]
    return totals


def titles_in_category(records, category):
    return [record["title"] for record in records if record["category"] == category]


def ranked_totals(records):
    totals = totals_by_category(records)
    return sorted(totals.items(), key=lambda pair: (-pair[1], pair[0]))


def main():
    print("Частоты слов")
    text = input("Введите текст: ")
    print_word_counts(word_counts(text))

    print("\nУчебные интересы")
    first = input("Темы первого студента через пробел: ").split()
    second = input("Темы второго студента через пробел: ").split()
    print(f"Общие темы: {common_topics(first, second)}")
    print(f"Все темы: {all_topics(first, second)}")

    print("\nЗапись и пара")
    lesson = {"title": "Python", "hours": 4}
    lesson["hours"] = 6
    lesson["completed"] = False
    pair = (lesson["title"], lesson["hours"])
    title, hours = pair
    print(f"Запись: {lesson}")
    print(f"Пара: {title}, {hours}")

    print("\nТуристические маршруты")
    records = [
        {"title": "Тропа вдоль Усманки", "category": "пеший", "amount": 8},
        {"title": "Маршрут по нагорной дубраве", "category": "пеший", "amount": 12},
        {"title": "Велокруг вокруг водохранилища", "category": "велосипедный", "amount": 24},
        {"title": "Сплав по реке Воронеж", "category": "водный", "amount": 14},
        {"title": "Сплав по Дону", "category": "водный", "amount": 10},
    ]
    totals = totals_by_category(records)
    for category in sorted(totals):
        print(f"{category}: {totals[category]} км")
    category = input("Категория маршрута: ").strip()
    print(f"Найденные маршруты: {titles_in_category(records, category)}")
    print(f"Категории по суммарной протяжённости: {ranked_totals(records)}")


if __name__ == "__main__":
    main()
