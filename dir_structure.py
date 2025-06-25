import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація Colorama
init(autoreset=True)


def get_dir_structure(path=None):
    if path is None:
        path = Path(sys.argv[1])
    else:
        path = Path(path)

    if not path.exists():
        print(Fore.RED + "Error: Path does not exist.")
        sys.exit(1)

    if not path.is_dir():
        print(Fore.RED + "Error: Path is not a directory.")
        sys.exit(1)

    for el in path.iterdir():
        if el.is_dir():
            print(Fore.BLUE + f"This is folder: {el}")
            get_dir_structure(el)
        else:
            print(Fore.GREEN + f"This is file: {el}")


get_dir_structure()
