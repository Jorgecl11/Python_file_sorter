# 📂 Python File Sorter (PowerPoint Edition)

A lightweight, portable Python script that monitors your Downloads folder and automatically organizes PowerPoint presentations into a dedicated backup folder. 



## 🚀 Features
* **Portable Pathing:** Uses `os.path.expanduser` to work on any machine without hardcoded usernames.
* **Smart Detection:** Catches both `.ppt` and `.pptx` extensions using case-insensitive logic.
* **PII-Safe:** Designed to be shared on GitHub without exposing personal user information.
* **Automated Cleanup:** (In Progress) Will eventually run as a background service.

## 🛠️ Built With
* **Python 3.10+**
* **OS Library:** For directory navigation and path joining.
* **Shutil Library:** For high-level file operations.

## 📦 How to Use
1. Clone this repository:
   ```bash
   git clone [https://github.com/Jorgecl11/Python_file_sorter.git](https://github.com/Jorgecl11/Python_file_sorter.git)
