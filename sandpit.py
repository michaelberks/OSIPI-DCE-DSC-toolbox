#%%
import os
import shutil
import glob
#%%
#Move all mdm_<name>.h files to <name>.py
file_list = glob.glob('**/*.h', recursive=True)

for file in file_list:
  newpath = file.replace('.h', '.py').replace('mdm_', '')

  shutil.move(file, newpath)
  print(f'Moved {file} to {newpath}')

# %%
