import sys
import os

def DirectoryFileSearch(DirName, Extension):
    if not os.path.isabs(DirName):
        DirName = os.path.abspath(DirName)
        
    if os.path.isdir(DirName):
        print(f"Listing all files with extension {Extension} in directory {DirName}")
        for foldername, subfoldername, filename in os.walk(DirName):
            for name in filename:
                if name.lower().endswith(Extension):
                    print("Found file: ", os.path.join(foldername, name))
    else:
        print("There is no such directory")

def main():
    print("---------------- Directory File Search -------------------")

    if len(sys.argv) == 2:
        if sys.argv[1].lower() == "--h":
            print("This script is used to search for files with a specific extension in a directory")
            exit()

        if sys.argv[1].lower() == "--u":
            print("Usage of the script : ")
            print("DirectoryFileSearch.py  Name_Of_Directory  Extension_Of_File")
            exit()

    if len(sys.argv) == 3:
        try:
            DirectoryFileSearch(sys.argv[1], sys.argv[2])
        except Exception as e:
            print("Unable to perform the task due to ", e)
    else:
        print("Invalid option")
        print("Use --h option to get the help and use --u option to get the usage of application")
        exit()

    print("--------- Thank you for using our script -------------")

if __name__ == "__main__":
    main()
