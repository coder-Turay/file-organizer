import os

folder_path = input("Enter the folder path: ")
os.chdir(folder_path)
base = os.getcwd()

categories = {
    "Texts": [".docx", ".doc", ".txt"],
    "Images": [".png", ".jpg", ".jpeg", ".bmp", ".gif"],
    "Presentations": [".ppt", ".pptx"],
    "Tables": [".xlsx"],
    "Music": [".wav", ".midi", ".mp3"],
    "Others": []
}

for folder in categories:
    try:
        os.mkdir(folder)
    except FileExistsError:
        print(f"{folder} is already existed")
        continue

for root, dirs, files in os.walk(base):

    dirs2 = []

    for i in dirs:
        if i not in categories:
            dirs2.append(i)
    dirs[:] = dirs2

    for file in files:
        full_path = os.path.join(root, file)
        is_found = False

        for folder in categories:
            if os.path.splitext(full_path)[1] in categories[folder]:
                destination_path = os.path.join(base, folder, file)
                is_found = True

                try:
                    os.rename(full_path, destination_path)
                except Exception as e:
                    print(e)

        if not is_found:
            destination_path = os.path.join(base, "Others", file)
            try:
                os.rename(full_path, destination_path)
            except Exception as e:
                print(e)

print("Moved:")
for i in categories:
    print(i + ": " + str(len(os.listdir(i))))