import sys
from pathlib import Path
from colorama import init, Fore, Style

def visualize_directory_structure(directory: str, depth: int = 0): 
    try:
        base_path = Path(directory)
        if not base_path.exists() or not base_path.is_dir():
            print(Fore.RED + "Помилка: Вказаний шлях не є директорією або не існує." + Style.RESET_ALL)
            return
        
        items = sorted(base_path.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))

        for item in items:
            if item.is_dir():
                print(Fore.BLUE + "  " * depth + item.name + "/" + Style.RESET_ALL)
                visualize_directory_structure(item, depth + 1)
            else:
                print(Fore.GREEN + "  " * depth + item.name + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Помилка: {e}" + Style.RESET_ALL)

if __name__ == "__main__":
    init(autoreset=True)
    if len(sys.argv) != 2:
        print(Fore.YELLOW + "Використання: python hw03.py /шлях/до/директорії" + Style.RESET_ALL)
    else:
        visualize_directory_structure(sys.argv[1])
