import os
import zipfile


def zip_with_progress(input_dir, output_zip_path):
    """Zip the contents of input_dir into output_zip_path, displaying progress."""

    # 1) Collect all files in the input directory.
    file_paths = []
    for root, dirs, files in os.walk(input_dir):
        for f in files:
            file_paths.append(os.path.join(root, f))

    # If no files found, just exit.
    total_files = len(file_paths)
    if total_files == 0:
        print(f"No files found in '{input_dir}'. Nothing to zip.")
        return

    # 2) Create the ZIP file.
    with zipfile.ZipFile(output_zip_path, mode="w", compression=zipfile.ZIP_DEFLATED) as zf:
        # Keep track of how many files have been added.
        count = 0
        for file_path in file_paths:
            # Make a relative path so your ZIP structure mirrors the folder structure.
            arcname = os.path.relpath(file_path, start=input_dir)
            zf.write(file_path, arcname=arcname)

            # Show basic percentage progress:
            count += 1
            percentage = (count / total_files) * 100
            print(f"Zipping progress: {percentage:.2f}% ({count}/{total_files})")

    print("Compression complete!")


if __name__ == "__main__":
    # Change the input and output folder yourself
    input_directory = r"D:\Last piece 2\AFM"
    output_zip = r"D:\Last piece 2\AFM_zip_241228.zip"

    # Call our function
    zip_with_progress(input_directory, output_zip)

    # Check if the file exists after creation
    if os.path.exists(output_zip):
        print("Archive created at:", output_zip)
    else:
        print("Archive not created.")
