import numpy as np
import nibabel as nib
import glob
import keras
from keras.utils import to_categorical
import matplotlib.pyplot as plt
from tifffile import imsave
import os
import random



TRAIN_DATASET_PATH = 'kits23/dataset/'
#VALIDATION_DATASET_PATH = 'BraTS2020_ValidationData/MICCAI_BraTS2020_ValidationData'
directory = TRAIN_DATASET_PATH + "case_00000/instances"
instances = []
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    instances.append(nib.load(f).get_fdata())

print(instances[0].shape)
   
n_slice= random.randint(0, instances[0].shape[2])
print(n_slice)
plt.figure(figsize=(12, 8))

plt.subplot(231)
first = instances[0]
plt.imshow(first[:,:,200])
plt.show()

#test_image_kidney=nib.load(TRAIN_DATASET_PATH + 'BraTS20_Training_355/BraTS20_Training_355_flair.nii').get_fdata()
