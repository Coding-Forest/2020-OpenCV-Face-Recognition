import os
import shutil
import time

SRC_DIR = "C:\\Users\\admin\\Desktop\\Middle_Resolution_extracted\\"
DEST_DIR = "C:\\Users\\admin\\Desktop\\selected test_images\\"
folder_start = time.process_time()

for i in range(1, 7):
    # create parent folders (6 levels).
    LEVEL_DIR = f"{DEST_DIR}level{i}\\"
    os.makedirs(LEVEL_DIR)

    # create children folders (400 persons) inside each level.
    id_names = os.listdir(SRC_DIR)
    for id in id_names:
        PERSON_DIR = f"{LEVEL_DIR}{id}\\"
        os.makedirs(PERSON_DIR)
folder_end = time.process_time()

copy_start = time.process_time()
ids = os.listdir(SRC_DIR)

for i in range(1, 7):
    for id in ids:
        src_path = f"{SRC_DIR}{id}\\S001\\L1\\E01\\C7.jpg"
        dest_path = f"{DEST_DIR}level{i}\\{id}\\C7.jpg"
        shutil.copy(src_path, dest_path)

copy_end = time.process_time()
folder_time = folder_end - folder_start
copy_time = copy_end - copy_start


'''
# Operation report
===== Report =====

took 0.375 seconds to create 2,400 folders.
took 1.453125 seconds to copy 2,400 images.

Process finished with exit code 0
'''
