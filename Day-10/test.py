import os

def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder)
        return files, None
    except FileNotFoundError:
        print("Please provide a valid folder name, looks like folder does not exist --> " + folder)
        return None, "Folder not Found!"
    except PermissionError:
        print("No access to this folder --> " + folder)
        return None, "Permission denied!"


def main():

    folder_paths = input("Please provide list of folders names with spaces in between: ").split()

    for folder_path in folder_paths:
        files, error_message = list_files_in_folder(folder_path)

        if files:
            print(f"Files in {folder_path}:")
            for file in files:
                print(file)
        else:
            print(f"Error in {folder_path}: {error_message}")

if __name__ == "__main__":
    main()