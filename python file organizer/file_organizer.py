import os
import shutil
import json
from datetime import datetime

# ================= CONFIG =================

# Automatically detect Downloads folder (Windows/macOS/Linux)
BASE_FOLDER = os.path.join(os.path.expanduser("~"), "Downloads")

# Log file for undo operation
LOG_FILE = "organizer_log.json"

# File categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".java", ".c", ".cpp"]
}

# ================= FUNCTIONS =================

def get_category(extension):
    for folder, extensions in FILE_TYPES.items():
        if extension in extensions:
            return folder
    return "Others"


def organize_files(dry_run=False):
    moves = []

    for filename in os.listdir(BASE_FOLDER):
        source_path = os.path.join(BASE_FOLDER, filename)

        if os.path.isfile(source_path):
            ext = os.path.splitext(filename)[1].lower()
            category = get_category(ext)
            dest_folder = os.path.join(BASE_FOLDER, category)

            if not os.path.exists(dest_folder):
                if not dry_run:
                    os.makedirs(dest_folder)

            destination_path = os.path.join(dest_folder, filename)

            if dry_run:
                print(f"[DRY-RUN] {filename} → {category}/")
            else:
                shutil.move(source_path, destination_path)
                moves.append({
                    "from": destination_path,
                    "to": source_path
                })

    if not dry_run:
        with open(LOG_FILE, "w") as f:
            json.dump(moves, f, indent=4)

        print("Files organized successfully.")
        print("Undo log saved.")


def undo_changes():
    if not os.path.exists(LOG_FILE):
        print("No log file found. Nothing to undo.")
        return

    with open(LOG_FILE, "r") as f:
        moves = json.load(f)

    for move in moves:
        if os.path.exists(move["from"]):
            shutil.move(move["from"], move["to"])

    os.remove(LOG_FILE)
    print("Undo completed. Files restored.")


# ================= MAIN =================

if __name__ == "__main__":
    print("Python File Organizer")
    print("1. Dry Run (Preview)")
    print("2. Organize Files")
    print("3. Undo Last Operation")

    choice = input("Select an option (1/2/3): ").strip()

    if choice == "1":
        organize_files(dry_run=True)
    elif choice == "2":
        organize_files(dry_run=False)
    elif choice == "3":
        undo_changes()
    else:
        print("Invalid choice.")
