import logging, os, os.path

DIR = './source'

file_count: int = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

logging.basicConfig(
    filename="source/logs.txt",
    format="%(asctime)s : %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
    level=logging.DEBUG,
)

logging.info(file_count)

print(f"there are {file_count} files in source folder")