# 📚 Homework: Working with Files and the Modular System

## Description

This project includes four separate tasks that demonstrate practical skills in file handling, building CLI applications, error handling, setting up virtual environments, and organizing code using modules in Python.

---

## 🧩 Tasks

### ✅ Task 1: Salary Calculation

Function: `total_salary(path)`

* Accepts the path to a text file with developer salaries.
* Returns the total and average salary as a tuple.

📄 **Example file content:**

```
Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000
```

---

### ✅ Task 2: Cat Information

Function: `get_cats_info(path)`

* Accepts the path to a file containing cat data.
* Returns a list of dictionaries with information about each cat.

📄 **Example file content:**

```
60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
```

---

### ✅ Task 3: Directory Tree Visualization

Script: `hw03.py`

* Takes a directory path as a command-line argument.
* Displays the folder structure using colored output with the `colorama` library.

🔧 **To run:**

```bash
python hw03.py /path/to/your/directory
```

---

### ✅ Task 4: CLI Assistant Bot

File: `assistant_bot.py`

* A command-line assistant bot that recognizes the following commands:

  * `hello`, `add`, `change`, `phone`, `all`, `exit`, `close`
* Stores contacts in a Python dictionary.
* Implements a request-response loop and command parsing.

---

## 📦 How to Run

1. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

2. Install dependencies:

   ```bash
   pip install colorama
   ```

3. Run the scripts:

   ```bash
   python salary_calc.py
   python cats_info.py
   python hw03.py /path/to/dir
   python assistant_bot.py
   ```

---

## 🗃️ Project Structure

```
goit-pycore-hw-04/
├── README.md
├── data/
│   ├── salary_file.txt       # Sample salary data for Task 1
│   └── cats_file.txt         # Sample cat data for Task 2
├── scripts/
│   ├── salary_calc.py        # Task 1: total_salary()
│   ├── cats_info.py          # Task 2: get_cats_info()
│   ├── dir_visualizer.py     # Task 3: directory structure display
│   └── assistant_bot.py      # Task 4: CLI assistant bot
├── .gitignore                # Optional: to exclude venv, __pycache__, etc.
└── venv/                     # Python virtual environment (excluded from Git)

```

---

## 📑 Requirements

* Python 3.10+
* `colorama` package (used in Task 3)
