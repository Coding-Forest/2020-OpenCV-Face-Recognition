# Directory structure of the source imageset
# .\\Middle_Resolution\\19062421\\S001\\L1\\E01\\image.jpg
import os
import shutil
from tqdm import tqdm
import time

ROOT_DIR = "C:\\Users\\admin\\Desktop\\Middle_Resolution_extracted\\"
folder_names = os.listdir(ROOT_DIR)
extension = ".jpg"
image_count = 0
start = time.process_time()

# Create folders in the destination dir.
  # Each folder will store images of one person.
for name in folder_names:
   dest_dir = "C:\\Users\\admin\\Desktop\\selected_imageset\\" + name
   os.makedirs(dest_dir)

# From the source directory,
for i in tqdm(range(1, 4)):
    for name in folder_names:
        source_path = ROOT_DIR + name + f"\\S001\\L1\\E0{i}\\"
        image_dir = os.listdir(source_path)

        # Copy images of each individual from every folder to the destination folder.
        for image in image_dir:
            if extension in image:
                target_file = os.path.abspath(source_path + image)
                dest_dir = f"C:\\Users\\admin\\Desktop\\selected_imageset\\{name}\\S001L1E0{i}{image}"
                shutil.copy(target_file, dest_dir)
                image_count += 1

end = time.process_time()
process_time = end - start


# Operation report
print("===== Report =====\n")
print(f"took {process_time} seconds to copy 24,000 images.")
print(f"took {process_time/image_count} seconds per copy.")



'''
100%|██████████| 3/3 [02:28<00:00, 49.55s/it]
===== Report =====

took 19.390625 seconds to copy 24,000 images.
took 0.0008079427083333334 seconds per copy.

Process finished with exit code 0
'''
