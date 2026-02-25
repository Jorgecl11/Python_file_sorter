import os
import shutil # used to move files
import time #needed for sleep timers
from datetime import datetime #This imports the datetime library for timestamps

#This finds your 'user' folder automatically.
home = os.path.expanduser("~")
folder_path = os.path.join(home, "Downloads")
#this will create a folder inside downloads to keep it neat.
target_folder = os.path.join(folder_path, "PowerPoint_Backups")
log_file = os.path.join(folder_path, "activity_log.txt") # the new log file.

#create backup folder if it doesnt exist yet.
if not os.path.exists(target_folder):
    os.makedirs(target_folder)
    print(f"Created: {target_folder}")
print(f"Service started. Monitoring {folder_path}... (Ctrl+C to stop.)")


#The Infinite Loop
while True:
    files = os.listdir(folder_path)
    files_found = False
    #'a' appends at the end of the file instead of overwriting it.
    with open(log_file, "a", encoding="utf-8") as log: #utf-8 handles special characters
        for file_name in files:
            #look for .ppt or .pptx
            if file_name.lower().endswith((".ppt", ".pptx")):
                #if any files found this if block executes.
                files_found = True

                now = datetime.now()
                #get the current time for the log.
                timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
                old_path = os.path.join(folder_path, file_name)
                new_path = os.path.join(target_folder, file_name)

                #--check for duplicate files--
                if os.path.exists(new_path):
                    #split the name and the extension
                    name, extension = os.path.splitext(file_name)
                    unique_suffix = now.strftime("Copy_%H%M%S")
                    file_name = f"{name}_{unique_suffix}{extension}"
                    new_path = os.path.join(target_folder, file_name)
                #--Duplicate check end--
                try:
                    shutil.move(old_path, new_path)
                
                    #write to the file and the terminal
                    log_entry = f"[{timestamp}] MOVED: {file_name}\n"
                    log.write(log_entry)
                    print(log_entry.strip())
                except Exception as e:
                    print(f"Error moving {file_name}: {e}")
    if not files_found:
        print(f"No PowerPoint files found in {folder_path}.")
  

    time.sleep(60)