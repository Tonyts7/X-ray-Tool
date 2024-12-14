import numpy as np
import matplotlib.pyplot as plt
from SciAnalysis.Data import Protocols

# Define the input data file and output directory
data_file = 'path/to/your/data/file.dat'  # Replace with your data file
output_dir = 'path/to/output/'  # Replace with your desired output directory

# Ensure the output directory exists
import os
os.makedirs(output_dir, exist_ok=True)

# Process and export the qr_image
def process_and_export_qr_image(input_file, output_dir):
    """
    Process the input data file using SciAnalysis and export the qr_image in .npz format.

    Parameters:
    - input_file (str): Path to the input data file.
    - output_dir (str): Directory to save the output files.
    """
    print(f"Processing file: {input_file}")

    # Process the data using the qr_image protocol
    qr_image_params = {
        'blur': None,
        'colorbar': True,
        'save_results': ['npz'],  # Save in npz format
        'transparent': False,
        'label_filename': True
    }

    # Generate qr_image using the SciAnalysis Protocols
    qr_image = Protocols.qr_image(input_file=input_file, **qr_image_params)

    # Save the qr_image to .npz format
    output_file = os.path.join(output_dir, 'qr_image.npz')
    np.savez(output_file, qr_image=qr_image)
    print(f"qr_image exported successfully to {output_file}")

    return qr_image, output_file


# Visualize qr_image
def visualize_qr_image(qr_image):
    """
    Visualize the qr_image using Matplotlib.

    Parameters:
    - qr_image (numpy.ndarray): The processed qr_image data.
    """
    plt.imshow(qr_image, cmap='gray')
    plt.colorbar()
    plt.title('qr_image')
    plt.show()


# Main script execution
if __name__ == '__main__':
    # Process and export the qr_image
    qr_image, output_file = process_and_export_qr_image(data_file, output_dir)

    # Load and verify the saved qr_image
    data = np.load(output_file)
    qr_image_loaded = data['qr_image']  # Adjust key if necessary

    # Visualize the qr_image
    visualize_qr_image(qr_image_loaded)



