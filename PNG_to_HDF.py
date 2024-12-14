import numpy as np
from PIL import Image
import h5py
import matplotlib.pyplot as plt
import os


image_path = r"D:\NSLS2_20247\TKoga2\waxs\analysis\Pilatus800_custom-mask.png"  # Input PNG image
output_folder = r"D:\Mask_elena\2024_7"  # Output folder
os.makedirs(output_folder, exist_ok=True)  # Ensure the output folder exists

# File paths for HDF5 files
hdf5_file_path = os.path.join(output_folder, 'python_exported_waxs_2024_7mask.hdf')  # Intermediate HDF5 file
final_hdf5_file_path = os.path.join(output_folder, 'WAXS_offcial_mask_2024_12.hdf')  # Final HDF5 file

# Step 1: Load PNG and save to HDF5
# Load the PNG image and convert to a NumPy array
image = Image.open(image_path)
image_array = np.array(image)

# Transpose the array for correct X and Y orientation
image_array = np.transpose(image_array, (1, 0, 2))

# Save the image array to an HDF5 file with UTF-8 encoding
with h5py.File(hdf5_file_path, 'w') as hdf5_file:
    dataset = hdf5_file.create_dataset('M_ROIMask', data=image_array, dtype=np.uint8)
    dataset.attrs['encoding'] = np.bytes_('UTF-8')  # Use np.bytes_ instead of np.string_

print(f"Image array saved to {hdf5_file_path} with M_ROIMask dataset name and UTF-8 encoding.")

# Step 2: Read HDF5, convert to grayscale, and save to a new HDF5 file
with h5py.File(hdf5_file_path, 'r') as input_hdf_file:
    # Load the image data from the dataset
    image_data = np.array(input_hdf_file['M_ROIMask'])

# If the image has 4 channels (RGBA), convert it to grayscale
if image_data.shape[-1] == 4:
    image_data = np.mean(image_data[:, :, :3], axis=-1)  # Average RGB channels

# Save the grayscale image data to a new HDF5 file
with h5py.File(final_hdf5_file_path, 'w') as output_hdf_file:
    output_hdf_file.create_dataset('grayscale_image', data=image_data)

print(f"Grayscale image saved to {final_hdf5_file_path} with dataset name 'grayscale_image'.")

# Step 3: Display the grayscale image
plt.imshow(image_data, cmap='gray')
plt.title("Grayscale Image")
plt.show()

# Optionally display using PIL
image = Image.fromarray(image_data.astype(np.uint8), mode='L')
image.show()

'''
Library:
contourpy	1.3.1	1.3.1
cycler	0.12.1	0.12.1
fonttools	4.55.0	4.55.2
h5py	3.12.1	3.12.1
kiwisolver	1.4.7	1.4.7
lxml	5.3.0	5.3.0
matplotlib	3.9.3	3.9.3
numpy	2.1.3	2.1.3
packaging	24.2	24.2
pillow	11.0.0	11.0.0
pip	24.3.1	24.3.1
pyparsing	3.2.0	3.2.0
python-dateutil	2.9.0.post0	2.9.0.post0
scipy	1.14.1	1.14.1
six	1.16.0	1.17.0
standard	1.0.3	1.0.3
termcolor	2.5.0	2.5.0
'''