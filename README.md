# FileAutoTransfer
📂 Auto File Transfer and Organizer by Code
This Python script scans a source folder for PDF files, detects specific code patterns in filenames (like NYC-GI-0001), and automatically copies each file to a matching destination subfolder that contains the same code. A detailed log of the operation is also generated.

📌 Features
✅ Detects files with naming patterns like NYC-XX-0000

📁 Copies matched files into corresponding folders in your destination root

📜 Logs each step of the process with timestamps

🧠 Skips non-PDF files and files with unmatched patterns

🛠️ Setup
Clone or download this repository to your machine.

Update the following lines in the script with your actual paths:

python
Copy
Edit
source_folder = r"your\source\folder\path"
destination_roots = [r"path\to\destination1",
    r"path\to\destination2",
    r"path\to\destination3"
]

🔍 How It Works
The script reads all .pdf files in your source_folder.

It searches for filenames containing a pattern like:

css
Copy
Edit
NYC-[A-Za-z]+-[0-9]+
Example match: NYC-GI-0246

If a match is found:

It checks every subfolder in the destination_root to see if the code is part of the folder name.

If a matching folder is found, the file is copied there.

All actions, including skips and errors, are logged to a text file named file_transfer_log.txt in your destination folder.

📁 Example Structure
Source Folder (input)
scss
Copy
Edit
NYC-RP-0200_Signed.pdf
Invoice_ABC.pdf          ← (Will be ignored)
Destination Folder
Copy
Edit
📁 NYC-RP-0200
After running the script, NYC-RP-0200_Signed.pdf will be copied into the NYC-RP-0200 folder.

📄 Log File
All actions are appended to file_transfer_log.txt, with timestamps:

csharp
Copy
Edit
[2025-04-23 17:30:00] 🔍 Found code 'NYC-RP-0200' in 'NYC-RP-0200_Signed.pdf'
[2025-04-23 17:30:00] ✅ Copied: NYC-RP-0200_Signed.pdf ➜ NYC-RP-0200
🧠 Notes
The script will skip non-PDF files.

It only copies to the first folder that matches the code (you can remove the break to allow multiple).

Logs will be appended, not overwritten.

📌 Requirements
Python 3.x

No external libraries needed – uses only built-in modules (os, shutil, re, datetime)

