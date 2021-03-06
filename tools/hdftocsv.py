#Coding: utf-8
from __future__ import print_function,division

import numpy as np
import tables

FILENAME = "spectrum.h5"
OUT_FILENAME = "spectrum.csv"
RESAMPLE = 100 # Take one dot out of RESAMPLE

h = tables.open_file(FILENAME)

arr = h.root.table.read(step=RESAMPLE)

arr = arr.astype(np.float)
factors = h.root.factor.read()
names = h.root.names.read()

for i,f in enumerate(factors):
  arr[:,i] *= f

i = 0
while i < len(names):
  if names[i].startswith('UNUSED'):
    del names[i]
    arr = np.delete(arr,i,1)
  i+=1

with open(OUT_FILENAME,'w') as f:
  f.write(','.join(names)+"\n")
  np.savetxt(f,arr)
