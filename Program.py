import os
source_path = r'C:\Users\kuchi\OneDrive\Folders\Automations\jpg-file-mover'
destination_path = r'C:\Users\kuchi\OneDrive\Pictures'
file_names = os.listdir(source_path)
for file_name in file_names:
    if file_name.endswith('.jpg'):
        source_file_path = os.path.join(source_path, file_name)
        destination_file_path = os.path.join(destination_path, file_name)
        os.rename(source_file_path, destination_file_path)
