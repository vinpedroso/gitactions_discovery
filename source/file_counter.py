import os, os.path

DIR = './source'

file_count: int = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

print(f"there are {file_count} files in source folder")
