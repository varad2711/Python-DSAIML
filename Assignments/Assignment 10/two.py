import sys
import os

def DirectoryRename(DirName, OldExtension, NewExtension):
    if not os.path.isabs(DirName):
        DirName = os.path.abspath(DirName)
        
    if os.path.isdir(DirName):
        print(f"Renaming all files with extension {OldExtension} to {NewExtension} in directory {DirName}")
        for foldername, subfoldername, filename in os.walk(DirName):
            for name in filename:
                if name.lower().endswith(OldExtension):
                    old_file = os.path.join(foldername, name)
                    new_file = os.path.join(foldername, name[:-len(OldExtension)] + NewExtension)
                    os.rename(old_file, new_file)
                    print(f"Renamed file: {old_file} to {new_file}")
    else:
        print("There is no such directory")

def main():
    print("---------------- Directory File Rename -------------------")

    if len(sys.argv) == 2:
        if sys.argv[1].lower() == "--h":
            print("This script is used to rename files with a specific extension in a directory")
            exit()

        if sys.argv[1].lower() == "--u":
            print("Usage of the script : ")
            print("DirectoryRename.py  Name_Of_Directory  Old_Extension  New_Extension")
            exit()

    if len(sys.argv) == 4:
        try:
            DirectoryRename(sys.argv[1], sys.argv[2], sys.argv[3])
        except Exception as e:
            print("Unable to perform the task due to ", e)
    else:
        print("Invalid option")
        print("Use --h option to get the help and use --u option to get the usage of application")
        exit()

    print("--------- Thank you for using our script -------------")

if __name__ == "__main__":
    main()
