from pathlib import Path


def total_salary(path):
    total = 0
    average = 0
    try:
        with open(path, encoding="utf-8") as fh:
            lines = [
                el.strip() for el in fh.readlines()
            ]  # Removes all spaces, tabs, and line breaks from the beginning and end of each line.
        for el in lines:
            name, salary = el.split(",")
            total += int(salary)

        if lines:
            average = total / len(lines)
        else:
            average = 0

    except FileNotFoundError:
        print(f"File not found: {path}")
    except UnicodeDecodeError:
        print(f"File is broken")

    return total, average


relative_path = Path("data/salary_info.txt")
absolute_path = relative_path.absolute()

total, average = total_salary(absolute_path)

print(f"Total salary: {total:g}, Average salary: {average:g}")
