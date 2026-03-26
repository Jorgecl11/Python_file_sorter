# 📂 Python File Sorter

A Python script that watches your Downloads folder and automatically moves supported files into organized backup folders.

I built this project to practice file automation with Python and create something actually useful for everyday cleanup.

## 🚀 Features
- Uses your home directory automatically, so there are no hardcoded usernames
- Sorts supported files into the right folder based on file type
- Handles duplicates by renaming files instead of overwriting them
- Checks that a file is fully downloaded or finished writing before moving it
- Logs file moves and errors to help track what happened
- Safe to share on GitHub without exposing personal information

## 🛠️ Built With
- Python 3.10+
- `os` for file paths and folder handling
- `shutil` for moving files
- `time` for file checks and scan intervals
- `datetime` for timestamps and logging

## 📦 How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/Jorgecl11/Python_file_sorter.git
