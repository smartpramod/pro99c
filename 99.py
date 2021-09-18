import os
from typing import Text 
import shutil
import time

# source=input("Enter the path and name of file"+"Example : C:/Users/BALAJI/Desktop.file name")
# os.remove (source)

# folder = input("Enter the path and name of file"+"Example : C:/Users/BALAJI/Desktop.file name")
# for filename in os.listdir(folder):
#     file_path = os.path.join(folder, filename)
#     try:
#         if os.path.isfile(file_path) or os.path.islink(file_path):
#             os.unlink(file_path)
#         elif os.path.isdir(file_path):
#             shutil.rmtree(file_path)
#     except Exception as e:
#         print('Failed to delete %s. Reason: %s' % (file_path, e))

import os, shutil
folder = 'C:/Users/BALAJI/Desktop/PYTHON/PROJECT/PRO99/New folder'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))