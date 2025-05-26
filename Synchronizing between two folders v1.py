import os
import shutil
import filecmp
import argparse
from tqdm import tqdm

def check_directories(src_dir, dst_dir):
    if not os.path.exists(src_dir):
        print(f"\nSource directory '{src_dir}'does not exist.")
        return False
    
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
        print (f"\nDestination directory '{dst_dir}' created.")
        return True
    
def sync_dir(src_dir, dst_dir, delete=False):
    files_to_sync = []
    for root, dirs, files in os.walk(src_dir):
        for directory in dirs:
            files_to_sync.append(os.path.join(root, directory))
        for file in files:
            files_to_sync.append(os.path.join(root, file))
    
    with tqdm(total=len(files_to_sync), desc="Syncing files", unit="file") as pbar:
        for source_path in files_to_sync:
            replica_path = os.path.join(dst_dir, os.path.relpath(source_path, src_dir))
            
            if os.path.isdir(source_path):
                if not os.path.exists(replica_path):
                    os.makedirs(replica_path)
            else:
                if not os.path.exists(replica_path) or not filecmp.cmp(source_path, replica_path, shallow=False):
                    pbar.set_description(f"Processing '{source_path}'")
                    print(f"\nCopying {source_path} to {replica_path}")
                    
                    shutil.copy2(source_path, replica_path)
            
            pbar.update(1)
            
if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Synchronize files between two directories.")
    parser.add_argument("source directory", help="The source directory to synchronize from.")
    parser.add_argument("destination directory", help="The destination directory to synchronize to.")
    
    args = parser.parse_args()
    
    if not check_directories(args.source_directory, args.destination_directory):
        exit(1)
    
    sync_dir(args.source_directory, args.destination_directory)
    print(f"\nSynchronization complete.")