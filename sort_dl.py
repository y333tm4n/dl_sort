import os
import shutil

def organize_download_folder(download_folder):
    # Define the categories, their corresponding file types, and file extensions
    categories = {
        'Documents': {
            'Text': ['.txt'],
            'Word': ['.doc', '.docx'],
            'PDF': ['.pdf'],
            'Excel': ['.xlsx']
        },
        'Photos': {
            'Images': ['.png', '.jpg', '.jpeg', '.gif', '.bmp']
        },
        'Videos': {
            'MP4': ['.mp4'],
            'AVI': ['.avi'],
            'MOV': ['.mov'],
            'MKV': ['.mkv']
        },
        'Executables': {
            'Exe': ['.exe'],
            'Installer': ['.msi']
        },
        'Others': {}  # Any file without a specified extension will go here
    }

    # Create subfolders for each category and file type if they don't exist already
    for category in categories:
        category_path = os.path.join(download_folder, category)
        os.makedirs(category_path, exist_ok=True)

        for file_type in categories[category]:
            type_path = os.path.join(category_path, file_type)
            os.makedirs(type_path, exist_ok=True)

    # Loop through the files in the download folder and move them to their respective subfolders
    for filename in os.listdir(download_folder):
        file_path = os.path.join(download_folder, filename)
        if os.path.isfile(file_path):  # Make sure we're dealing with a file, not a subdirectory
            _, file_extension = os.path.splitext(filename)

            # Find the corresponding category and file type for the file extension
            target_category = 'Others'
            target_file_type = None

            for category, types in categories.items():
                for file_type, extensions in types.items():
                    if file_extension.lower() in extensions:
                        target_category = category
                        target_file_type = file_type
                        break

            # Move the file to the appropriate subfolder
            if target_category and target_file_type:
                target_folder = os.path.join(download_folder, target_category, target_file_type)
                shutil.move(file_path, target_folder)
            else:
                print(f"Error: Could not find target category or file type for file {filename}")

if __name__ == "__main__":
    download_folder = "/replace/file/path"  # Replace this with your actual download folder path
    organize_download_folder(download_folder)