# Directory structure of the source imageset
# .\\Middle_Resolution\\19062421\\S001\\L1\\E01\\image.jpg

ROOT_DIR = ".\\Middle_Resolution\\"
folder_names = os.listdir(ROOT_DIR)
extension = ".jpg"

# Create folders in the destination dir. 
  # Each folder will store images of one person. 
for name in folder_names:
   dest_dir = ".\\selected_imageset\\" + name
   os.makedirs(dest_dir)

# From the source directory,
for name in folder_names:
   dest_dir = ".\\selected_imageset\\" + name
   source_path = ROOT_DIR + name + "\\S001\\L1\\E01\\"
   image_dir = os.listdir(source_path)
    
   # Copy images of each individual from every folder to the destination folder.
   for image in image_dir:
      if extension in image:
         target_file = os.path.abspath(source_path + image)
         shutil.copy(target_file, dest_dir)
