# file-organizer
# 📂 Python File Organizer

A Python application that automatically organizes files into folders based on their file extensions.

## ✨ Features

* Automatically creates folders for different file categories.
* Organizes files based on their extensions.
* Supports recursive folder scanning using `os.walk()`.
* Automatically creates the following folders:

  * Texts
  * Images
  * Presentations
  * Tables
  * Music
  * Others
* Moves unknown file types into the **Others** folder.
* Displays a summary of the organized files after completion.

## 🛠️ Technologies Used

* Python 3
* `os` module

## 📁 Supported File Types

| Category      | Extensions                              |
| ------------- | --------------------------------------- |
| Texts         | `.txt`, `.doc`, `.docx`                 |
| Images        | `.png`, `.jpg`, `.jpeg`, `.bmp`, `.gif` |
| Presentations | `.ppt`, `.pptx`                         |
| Tables        | `.xlsx`                                 |
| Music         | `.mp3`, `.wav`, `.midi`                 |

## 🚀 How to Use

1. Download or clone this repository.
2. Run the Python script.
3. Enter the path of the folder you want to organize (or configure the folder path in the script).
4. The program will automatically organize all supported files into their corresponding folders.

## 📌 Example

Before:

```
Project Folder/
├── photo.jpg
├── notes.docx
├── music.mp3
├── archive.zip
```

After:

```
Project Folder/
├── Images/
│   └── photo.jpg
├── Texts/
│   └── notes.docx
├── Music/
│   └── music.mp3
├── Others/
│   └── archive.zip
```

## 👨‍💻 Author

Created by **Turay Pasayev** as a Python practice project.
