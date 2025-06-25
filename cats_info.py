from pathlib import Path


def get_cats_info(path):
    cats_list = []
    try:
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                words = line.strip().split(",")
                id, name, age = words
                cats_list.append({"id": id, "name": name, "age": age})

    except FileNotFoundError:
        print(f"File not found: {path}")
    except UnicodeDecodeError:
        print(f"File is broken")
    return cats_list


relative_path = Path("data/cats_info.txt")
absolute_path = relative_path.absolute()


cats_info = get_cats_info(absolute_path)
print(cats_info)
