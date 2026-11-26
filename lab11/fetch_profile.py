import json
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


def fetch_profile(login):
    if not login.strip():
        raise ValueError("Логин не должен быть пустым")
    url = "https://api.github.com/users/" + quote(login.strip(), safe="")
    request = Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "python-course-lab11",
    })
    with urlopen(request, timeout=10) as response:
        data = json.loads(response.read().decode("utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("login"), str):
        raise ValueError("Ответ не похож на профиль пользователя")
    return data


def show_profile(data):
    print(f"Логин: {data['login']}")


def main():
    folder = Path(__file__).resolve().parent
    mode = input("Источник профиля (1 — GitHub, 2 — локальный пример): ").strip()
    try:
        if mode == "1":
            data = fetch_profile(input("Логин GitHub: "))
            output = folder / "profile.json"
            with output.open("w", encoding="utf-8") as target:
                json.dump(data, target, ensure_ascii=False, indent=2)
                target.write("\n")
            print("Профиль сохранён в profile.json")
        elif mode == "2":
            with (folder / "profile_sample.json").open(encoding="utf-8") as source:
                data = json.load(source)
        else:
            print("Выберите 1 или 2")
            return
        show_profile(data)
    except HTTPError as error:
        print(f"Сервер вернул HTTP {error.code}")
    except (URLError, TimeoutError):
        print("Не удалось получить ответ по сети")
    except ValueError as error:
        print(f"Ошибка данных: {error}")
    except OSError as error:
        print(f"Ошибка доступа: {error}")


if __name__ == "__main__":
    main()
