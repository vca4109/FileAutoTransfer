1	FileAutoTransfer
2	Description
This Python script scans a source folder for PDF files, detects specific code patterns in filenames (like NYC-GI-0001), and automatically copies each file to a matching destination subfolder containing the same code. It also generates a detailed log of the process.
3	Features
•	Detects files with naming patterns like NYC-XX-0000
•	Copies matched files into corresponding subfolders in the destination directory
•	Logs each step of the process with timestamps
•	Skips non-PDF files and files that don't match the pattern
4	Setup
•	Clone or download this repository.
•	Edit the following lines in the script to match your folder paths:
source_folder = r"your\source\folder\path"
destination_roots = [
   		 r"path\to\destination1",
   		 r"path\to\destination2",
    		 r"path\to\destination3"
]
5	How It Works
•	The script reads all .pdf files in the source folder.
•	It looks for filenames matching the pattern:
NYC-[A-Za-z]+-[0-9]+
Example: NYC-GI-0246
•	If a match is found, the script searches destination subfolders for a folder name that contains the code.
•	If a match is found, the file is copied there.
•	All actions are logged in a file named file_transfer_log.txt in the destination folder.
6	Example Folder Structure
Source Folder (input):
NYC-RP-0200_Signed.pdf  
Invoice_ABC.pdf   # This file will be ignored
Destination Folder:
NYC-RP-0200
After running the script, NYC-RP-0200_Signed.pdf will be copied into the NYC-RP-0200 folder.
7	Log File

A log file (file_transfer_log.txt) will record each action with a timestamp. Example log:
[2025-04-23 17:30:00] Found code 'NYC-RP-0200' in 'NYC-RP-0200_Signed.pdf'
[2025-04-23 17:30:00] Copied: NYC-RP-0200_Signed.pdf -> NYC-RP-0200

8	Notes
•	Only .pdf files are processed.
•	The script stops after the first matching folder (you can remove the break statement if you want to copy to all matches).
•	Logs are appended, not overwritten.

9	Requirements
•	Python 3.x
•	No external libraries needed (uses os, shutil, re, and datetime)

