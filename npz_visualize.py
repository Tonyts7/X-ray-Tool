import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman'],
    'mathtext.fontset': 'stix',
    'font.size': 15
})

#font_properties = {'family': 'Times New Roman', 'style': 'normal', 'size': 14}

# Load the .npz file
npz_file = 'E:/Experiment data/NSLS/2023.3/TKoga/waxs/analysis/qr_image/Zhixing_A1_pos1_T159.897C_x0.000_th0.200_60.00s_940590_waxs_stitched.npz'
data = np.load(npz_file)

# Extract data arrays
image = data['image']
x_axis = data['x_axis']
y_axis = data['y_axis']

#  colorbar/scalebar range modify image use
vmin = 40
vmax = 170

# Create a meshgrid for plotting
X, Y = np.meshgrid(x_axis, y_axis)

# image 2D pattern
plt.figure(figsize=(8, 6))
plt.pcolormesh(X, Y, image, shading='auto', cmap='viridis', vmin=vmin, vmax=vmax)
#plt.colorbar(label='Intensity')
plt.xlabel(r'$\text{q}_{\text{xy}}$ $(\text{Å}^{-1})$', fontsize=15) # x-axis label (qxy)
plt.ylabel(r'$\text{q}_{\text{z}}$ $(\text{Å}^{-1})$', fontsize=15) # y-axis label (qz)
plt.title('PS30K bulk at 170℃') #image title

cbar = plt.colorbar(shrink=0.68)  # Adjust colorbar length
cbar.set_label('Intensity', fontsize=12, family='Times New Roman') # scalebar character name, font and size

# Set axis limits to adjust the q-range displayed
plt.xlim([-1.3, 2.0])  # Replace  q_xy range
plt.ylim([0, 2.5])  # Replace q_z range
plt.gca().set_aspect(0.9) # image aspect
plt.show()

#REMEMBER TO CLOSE THE IMAGE WINDOW!

'''
#For checking available colormap
import matplotlib.pyplot as plt
print(plt.colormaps())
'''

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