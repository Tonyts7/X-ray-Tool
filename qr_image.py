import numpy as np
import matplotlib.pyplot as plt
from SciAnalysis.Data import Protocols
import os

# Input data file and output directory
data_file = 'E:/Experiment data/NSLS/2023.3/TKoga/waxs/analysis/qr_image/Zhixing_A1_pos1_T30.006C_x0.000_th0.060_60.00s_940036_waxs_stitched.npz' #Replace the name of the file
output_dir = 'D:/npz_qr/'  #Output folder address
os.makedirs(output_dir, exist_ok=True)  # Ensure output directory exists

def process_qr_image(input_file, output_dir):
    """
    Process the input data file using SciAnalysis, save qr_image to .npz format,
    load it back, and visualize the result.

    Parameters:
    - input_file (str): Path to the input data file.
    - output_dir (str): Directory to save the output files.
    """
    print(f"Processing file: {input_file}")

    # Step 1: Process the data using the qr_image protocol
    qr_image_params = {
        'blur': None,
        'colorbar': True,
        'save_results': ['npz'],  # Save in .npz format
        'transparent': False,
        'label_filename': True
    }
    qr_image = Protocols.qr_image(input_file=input_file, **qr_image_params)

    # Step 2: Save the qr_image to .npz format
    output_file = os.path.join(output_dir, 'qr_image.npz')
    np.savez(output_file, qr_image=qr_image)
    print(f"qr_image exported successfully to {output_file}")

    # Step 3: Load the saved .npz file
    data = np.load(output_file)
    qr_image_loaded = data['qr_image']  # Adjust 'qr_image' key if necessary
    print(f"Loaded qr_image from .npz file. Shape: {qr_image_loaded.shape}")

    # Step 4: Visualize the qr_image
    plt.imshow(qr_image_loaded, cmap='gray')
    plt.colorbar()
    plt.title('qr_image')
    plt.show()


# Execute the full workflow
if __name__ == '__main__':
    process_qr_image(data_file, output_dir)
