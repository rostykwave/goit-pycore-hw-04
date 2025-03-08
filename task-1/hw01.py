from data import load_data, process_data_to_get_salaries
import pathlib
current_dir = pathlib.Path(__file__).parent

def total_salary(path: str) -> tuple[int, int]:
    try:
        raw_data = load_data(path)
        salaries = process_data_to_get_salaries(raw_data)
        total = sum(salaries)
        average = total // len(salaries)
        return total, average
    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
        return 0, 0
    except ValueError:
        print("Помилка: Некоректний формат даних у файлі.")
        return 0, 0
    except Exception as e:
        print(f"Помилка: {e}")
        return []

# Приклад використання
if __name__ == "__main__":
    total, average = total_salary(f"{current_dir}/salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
# Загальна сума заробітної плати: 6000, Середня заробітна плата: 2000
