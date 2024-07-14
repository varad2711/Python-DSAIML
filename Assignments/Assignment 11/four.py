import sys
import os
import hashlib
import logging
import time

def setup_logging():
    """Setup logging to write messages to Log.txt in the current directory."""
    logging.basicConfig(filename='Log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def find_and_delete_duplicates(directory):
    """Find and delete duplicate files in the given directory."""
    file_hashes = {}
    duplicates = []

    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_hash = hash_file(file_path)

            if file_hash in file_hashes:
                duplicates.append(file_path)
                os.remove(file_path)
                logging.info(f"Deleted duplicate file: {file_path}")
            else:
                file_hashes[file_hash] = file_path

    return duplicates

def hash_file(file_path):
    """Generate an MD5 hash for a file."""
    hash_alg = hashlib.md5()
    
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_alg.update(chunk)
    except Exception as e:
        logging.error(f"Error hashing file {file_path}: {e}")
        return None
    
    return hash_alg.hexdigest()

def validate_directory(directory):
    """Validate if the provided directory exists."""
    if not os.path.isdir(directory):
        logging.error(f"The directory '{directory}' does not exist.")
        sys.exit(1)

def main():
    setup_logging()
    
    if len(sys.argv) != 2:
        logging.error("Invalid number of arguments.")
        logging.info("Usage: python DirectoryDuplicateRemoval.py <directory_name>")
        sys.exit(1)

    directory = sys.argv[1]
    validate_directory(directory)

    try:
        start_time = time.time()
        duplicates = find_and_delete_duplicates(directory)
        end_time = time.time()
        
        if duplicates:
            logging.info(f"Duplicate files found and deleted: {', '.join(duplicates)}")
        else:
            logging.info("No duplicate files found.")
        
        logging.info(f"Execution time: {end_time - start_time:.2f} seconds")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
