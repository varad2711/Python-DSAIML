import sys
import os
import hashlib
import logging

def setup_logging():
    """Setup logging to write to Log.txt in the current directory."""
    logging.basicConfig(filename='Log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def find_duplicate_files(directory):
    """Find and return a list of duplicate files in the given directory."""
    file_hashes = {}
    duplicates = []

    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_hash = hash_file(file_path)

            if file_hash in file_hashes:
                duplicates.append(filename)
            else:
                file_hashes[file_hash] = file_path

    return duplicates

def hash_file(file_path):
    """Generate a hash for a file."""
    hash_alg = hashlib.md5()
    
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_alg.update(chunk)
    except Exception as e:
        logging.error(f"Error hashing file {file_path}: {e}")
    
    return hash_alg.hexdigest()

def main():
    setup_logging()
    
    if len(sys.argv) != 2:
        logging.error("Invalid number of arguments.")
        logging.info("Usage: python main.py <directory_name>")
        sys.exit(1)

    directory = sys.argv[1]

    if not os.path.isdir(directory):
        logging.error(f"The directory '{directory}' does not exist.")
        sys.exit(1)

    try:
        duplicates = find_duplicate_files(directory)
        if duplicates:
            logging.info(f"Duplicate files found: {', '.join(duplicates)}")
        else:
            logging.info("No duplicate files found.")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
