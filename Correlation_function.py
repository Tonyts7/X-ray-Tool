import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid
import os

# Load the data
data = np.loadtxt(r"D:\Last piece 2\TPX_E-L\2024-7\Correlation_function\TPX_G_ads_240.csv", delimiter=",")  # Raw data folder,adjust delimiter if necessary
q = data[:264, 1]  # q range
I = data[:264, 0]  # Intensity

# Constants
num = 10000  # Data points for r (Long period)
s = q / (2 * np.pi)  # Define s = q / 2pi
r = np.linspace(0, 10000, num)  # Correlation function r (long period) data zone is 0~10000

# Calculate G
G = I * s**2


denominator = cumulative_trapezoid(G, s, initial=0)
denomi = denominator[-1]

# Calculate R and Gamma
R = np.zeros_like(r)
for i, r_i in enumerate(r):
    F = I * s**2 * np.cos(2 * np.pi * r_i * s)
    numerator = cumulative_trapezoid(F, s, initial=0)
    R[i] = numerator[-1]

Gamma = R / denomi

# Export address and name
output_folder = r"D:\Last piece 2\TPX_E-L"  # Replace the folder address you want to export
output_file = "TPX_G_ads_240.txt"


os.makedirs(output_folder, exist_ok=True) #Check the folder exist or not

# Combine folder and file name
output_path = os.path.join(output_folder, output_file)

# Export the data
data_to_write = np.column_stack((r, Gamma))  # Combine r and Gamma into one matrix
np.savetxt(output_path, data_to_write, delimiter="\t", fmt="%.6e")

print(f"File exported to: {output_path} successfully")


plt.figure()
plt.plot(r, Gamma)
plt.title("Correlation_function_result")
plt.xlabel("r")
plt.ylabel("Gamma")
plt.show()

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


