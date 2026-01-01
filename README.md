# Python-File-Organizer
safe and customizable Python utility that automatically organizes files in a folder based on file type, with preview (dry-run) and undo support.

🚀 Features

Automatically organizes files by type (Images, Documents, Videos, Audio, etc.)
Auto-detects the Downloads folder (no manual path configuration needed)
Dry-run mode to preview changes before moving files
Undo option to restore files to their original locations
Creates folders automatically if they don’t exist
Cross-platform support (Windows, macOS, Linux)
Clean, beginner-friendly, and well-documented code

🧠 How It Works:

The script scans the target folder, identifies file types by extension, and moves each file into an appropriate category folder.
An undo log is generated so changes can be safely reversed.

📂 File Categories
Category	Extensions
Images	.jpg, .jpeg, .png, .gif, .bmp
Documents	.pdf, .docx, .doc, .txt, .xlsx, .pptx
Videos	.mp4, .mov, .avi, .mkv
Audio	.mp3, .wav, .aac
Archives	.zip, .rar, .7z, .tar, .gz
Scripts	.py, .js, .java, .c, .cpp
Others	Any unsupported file type

🛠️ Requirements
Python 3.7 or higher
No external libraries required

⚙️ Installation

1.Clone the repository:
git clone https://github.com/saif8671/python-file-organizer.git


2.Navigate to the project folder:
cd python-file-organizer


3.Run the script:
python file_organizer_pro.py

▶️ Usage
When you run the script, you will see the following menu:

Python File Organizer
1. Dry Run (Preview)
2. Organize Files
3. Undo Last Operation

Option 1 – Dry Run
Previews what files will be moved without making changes.

Option 2 – Organize Files
Moves files into categorized folders and saves an undo log.

Option 3 – Undo
Restores all files to their original locations using the log file.

📍 Default Folder
By default, the script automatically organizes the Downloads folder of the current user.
If you want to organize a custom folder, modify this line in the code:

BASE_FOLDER = r"PATH_TO_YOUR_FOLDER"

Example:
BASE_FOLDER = r"E:\MyFiles\TestFolder"

🔒 Safety Notes

Always test with Dry Run before organizing files
Keep backups of important data
Undo is available only for the most recent operation

💼 Use Cases

Organizing cluttered Downloads folders
Automating repetitive file management tasks
Learning Python file handling and automation
Demonstration project for freelancing portfolios

📄 License
This project is open-source and available for educational and personal use.

🤝 Author

Developed by Saif Ur Rahman
Computer Science Student | Python Automation | Cybersecurity Enthusiast
