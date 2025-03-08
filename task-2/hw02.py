import pathlib
current_dir = pathlib.Path(__file__).parent

def get_cats_info(path: str) -> list[dict[str, str]]:
    try:
        with open(path, "r", encoding="utf-8") as file:
            cats =[
                {"id": parts[0], "name": parts[1], "age": parts[2]} 
                for line in file if (parts := line.strip().split(',')) and len(parts) == 3
            ]
        return cats
    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
        return []
    except ValueError:
        print("Помилка: Некоректний формат даних у файлі.")
        return 0, 0
    except Exception as e:
        print(f"Помилка: {e}")
        return []


# Приклад використання
if __name__ == "__main__":
    cats_info = get_cats_info(f"{current_dir}/cats_file.txt")
    print(cats_info)
# [
#     {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
#     {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
#     {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
#     {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
#     {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
# ]

