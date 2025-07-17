
# 🍬 Sweet Shop Management System

A Python-based Sweet Shop Management System built using **Test-Driven Development (TDD)** and clean coding principles. It allows you to **add**, **view**, **update**, **delete**, **search**, and **sort** sweets using a backend logic.

---

## 📁 Project Structure

```
Sweet_Shop_TDD/
│
├── sweet.py                      # Sweet class model
├── sweet_manager.py             # Core business logic
├── data_persistence.py          # JSON file handling (save/load)
│
├── test/
│   ├── test_sweet_manager.py    # Unit tests for SweetManager
│
├── sweets.json                  # Data storage 
├── docs/
│   └── index.html               # HTML test report (viewable via GitHub Pages)
│
└── README.md                    # Project overview and instructions
```

---
## To See Test Results:
Click this : https://i-aana.github.io/Sweet_Shop_TDD/index.html

---

## ✅ Features

- Add new sweets with name, price, and category
- View all sweets
- Search sweets by name
- Delete sweets by name
- Sort sweets by price or name
- Save/load sweets to/from a JSON file
- Clean error handling with custom exceptions
- Fully test-driven using `unittest` framework

---

## 🧪 Run Tests

```bash
python -m unittest discover -s test
```

---

## 🧠 Concepts & Principles Followed

- ✅ **TDD (Test Driven Development)**
- ✅ **SOLID Principles**
- ✅ **SDLC Cycle (Design > Code > Test > Deploy)**
- ✅ **Clean Code & Modular Structure**
- ✅ **Version Control (Git)**

---
