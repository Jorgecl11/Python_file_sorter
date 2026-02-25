import os
import shutil
import time
from datetime import datetime


FILE_MAP = {
    ".pdf" : "PDF_Backups",
    ".docx" : "Word_Backups",
    ".xlsx" : "Excel_Backups",
    ".csv" : "Excel_Backups",
    ".ppt" : "PowerPoint_Backups",
    ".pptx": "PowerPoint_Backups",
    ".png" : "Images_backups",
    ".jpg" : "Images_backups",
    ".jpeg" : "Images_backups",
}
#This finds your 'user' folder automatically.
home = os.path.expanduser("~")
folder_path = os.path.join(home, "Downloads")
#this will create a folder inside downloads to keep it neat.
target_folder = os.path.join(folder_path, "PowerPoint_Backups")
log_file = os.path.join(folder_path, "activity_log.txt") # the new log file.
print(f"Service started. Monitoring {folder_path}... (Ctrl+C to stop.)")


#The Infinite Loop
while True:
    files = os.listdir(folder_path)
    files_found = False
    #'a' appends at the end of the file instead of overwriting it.
    with open(log_file, "a", encoding="utf-8") as log: #utf-8 handles special characters
        for file_name in files:
            name, extension = os.path.splitext(file_name)
            extension = extension.lower() 
            
            if extension in FILE_MAP:
                files_found = True

                category_folder = FILE_MAP[extension]
                # DYNAMIC PATH: This changes depending on the file type
                current_target_path = os.path.join(folder_path,category_folder)

                if not os.path.exists(current_target_path):
                    os.makedirs(current_target_path)
                    print(f"Created new category folder: {category_folder}")

                now = datetime.now()
                #get the current time for the log.
                timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

                old_path = os.path.join(folder_path, file_name)
                new_path = os.path.join(current_target_path, file_name)

                #--check for duplicate files--
                if os.path.exists(new_path):
                    #split the name and the extension
                    name, extension = os.path.splitext(file_name)
                    unique_suffix = now.strftime("Copy_%H%M%S")
                    file_name = f"{name}_{unique_suffix}{extension}"
                    new_path = os.path.join(current_target_path, file_name)
                #--Duplicate check end--
                try:
                    shutil.move(old_path, new_path)
                
                    #write to the file and the terminal
                    log_entry = f"[{timestamp}] MOVED: {file_name} to folder: {current_target_path}\n"
                    log.write(log_entry)
                    print(log_entry.strip())
                except Exception as e:
                    print(f"Error moving {file_name}: {e}")
    if not files_found:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Scan complete: No matching files found.")
  

    time.sleep(60)