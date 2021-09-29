# Unzip multiple child zipfiles in a parent zipfile
# Make sure the slash (/) is included appropriately for all path variables.

import os
import zipfile

source = "parent_zip_file_path/"
destination = "extracted_file_path/"
extension = ".zip"

for item in os.listdir(source):                         # loop through items in dir
    if item.endswith(extension):                        # check for ".zip" extension
        folder_name = item.replace(".zip", "")          # destination folder name for each child zip file (in case each child has multiple files in it)
        zipfile_name = os.path.abspath(source + item)   # get full path of files
        with zipfile.ZipFile(zipfile_name, 'r') as zip_file:
            zip_file.extractall(destination + folder_name)
