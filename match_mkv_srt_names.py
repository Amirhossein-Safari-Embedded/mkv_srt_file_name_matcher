import os
import shutil
import msvcrt

current_folder = os.getcwd()  # Get the current working directory

# Get a list of all .mkv and .srt files in the current folder
mkv_files = [file for file in os.listdir(current_folder) if file.endswith(".mkv")]
srt_files = [file for file in os.listdir(current_folder) if file.endswith(".srt")]

# Sort the files alphabetically
mkv_files.sort()
srt_files.sort()

# Check if the number of .mkv and .srt files match
if len(mkv_files) != len(srt_files):
    print("Error: Number of .mkv and .srt files do not match!")
elif len(mkv_files) == 0:
    print("Error: There is no .mkv or .srt file in the folder!")
else:
    # Rename .srt files
    for index, srt_file in enumerate(srt_files):
        mkv_name = os.path.splitext(mkv_files[index])[0]  # Get the .mkv file name without extension
        new_srt_name = f"{mkv_name}.srt"  # Construct the new .srt file name

        # Construct the full file paths
        old_srt_path = os.path.join(current_folder, srt_file)
        new_srt_path = os.path.join(current_folder, new_srt_name)

        # Rename the .srt file
        os.rename(old_srt_path, new_srt_path)
    # Display result message
    print("File names copied and renamed successfully.")  

# Wait for any key to close the program
print("Press any key to exit...")
msvcrt.getch()
    
