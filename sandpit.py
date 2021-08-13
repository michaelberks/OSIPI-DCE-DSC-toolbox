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
import pandas as pd
import numpy as np

data = pd.read_csv('~/Downloads/data/gapminder_gdp_oceania.csv', index_col='country')
print(data)

# %%
mask = data.loc[:,:]==data.iloc[0,3]
nz = mask.to_numpy().nonzero()
print(data.index[nz[0]], data.columns[nz[1]])

# %%
