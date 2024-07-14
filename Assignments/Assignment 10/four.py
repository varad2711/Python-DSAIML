import sys
import os
import shutil

def DirectoryCopy(source_dir, destination_dir):
    source_dir = os.path.abspath(source_dir)
    destination_dir = os.path.abspath(destination_dir)

    if os.path.isdir(source_dir):
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
        else:
            print(f"Directory '{destination_dir}' already exists.")

        print(f"Copying files from '{source_dir}' to '{destination_dir}'...")
        for item in os.listdir(source_dir):
            source_item = os.path.join(source_dir, item)
            destination_item = os.path.join(destination_dir, item)
            if os.path.isdir(source_item):
                shutil.copytree(source_item, destination_item)
            else:
                shutil.copy2(source_item, destination_dir)
                print(f"Copied file: {item}")
        print("Files copied successfully.")
    else:
        print(f"Source directory '{source_dir}' does not exist.")

def main():
    print("---------------- Directory Copy -------------------")

    if len(sys.argv) == 2:
        if sys.argv[1].lower() == "--h":
            print("This script is used to copy all files from one directory to another.")
            exit()
        if sys.argv[1].lower() == "--u":
            print("Usage of the script:")
            print("DirectoryCopy.py Source_Directory Destination_Directory")
            exit()

    if len(sys.argv) == 3:
        try:
            DirectoryCopy(sys.argv[1], sys.argv[2])
        except Exception as e:
            print("Unable to perform the task due to ", e)
    else:
        print("Invalid option")
        print("Use --h option to get the help and use --u option to get the usage of the application")
        exit()

    print("--------- Thank you for using our script -------------")

if __name__ == "__main__":
    main()
