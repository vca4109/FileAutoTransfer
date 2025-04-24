import os
import shutil
import re
from datetime import datetime

# 🔁 Set your folders
source_folder = r"file path source"
destination_roots = [
    r"path\to\destination1",
    r"path\to\destination2",
    r"path\to\destination3"
]

# Pattern to extract the code
pattern = r"(NYC-[A-Za-z]+-\d+)"

# Path to log file
log_file = os.path.join(destination_root, "file_transfer_log.txt")

# Function to log messages with timestamp and UTF-8 encoding
def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_message = f"[{timestamp}] {message}"
    print(full_message)
    with open(log_file, "a", encoding="utf-8") as log:  # Ensure the file is opened with UTF-8 encoding
        log.write(full_message + "\n")

# Loop through files
for filename in os.listdir(source_folder):
    if not filename.lower().endswith(".pdf"):
        continue

    file_path = os.path.join(source_folder, filename)
    match = re.search(pattern, filename)

    if not match:
        log_message(f"❌ No match found in filename: {filename}")
        continue

    code = match.group(1)
    log_message(f"🔍 Found code '{code}' in '{filename}'")

    matched = False

    for folder_name in os.listdir(destination_root):
        log_message(f"    🔄 Checking against folder: {folder_name}")

        if code in folder_name:
            dest_folder = os.path.join(destination_root, folder_name)
            os.makedirs(dest_folder, exist_ok=True)

            shutil.copy2(file_path, dest_folder)
            log_message(f"✅ Copied: {filename} ➜ {folder_name}")
            matched = True
            break  # Remove this 'break' if you want to copy to all matching folders

    if not matched:
        log_message(f"⚠️ No matching folder found for: {filename}")

log_message("✅ Done.")
