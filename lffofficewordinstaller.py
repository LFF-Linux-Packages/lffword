import os
import getpass
import shutil

def search_files(directory, extension):
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(extension):
                files.append(os.path.join(root, filename))
    return files

# Directory to search within
directory_to_search = f'/etc/lff-linux'

# Search for lffofficeword.py files
lffword_python = search_files(directory_to_search, 'lffofficeword.py')
lffword_png = search_files(directory_to_search, 'lffofficeword.png')

def create_desktop_entry():
    desktop_entry = f'''[Desktop Entry]
Type=Application
Name=LFF Office Word
Exec=/usr/bin/python3 /usr/local/share/applications/LFF-Office/LFF-Word/lffofficeword.py
Terminal=false
Icon=/usr/local/share/applications/LFF-Office/LFF-Word/lffofficeword.png
Categories=Office;
'''

    # Specify the path and filename for the desktop entry file
    desktop_entry_file = f'/usr/local/share/applications/LFF-Office-Word.desktop'
    destination_dir = f'/usr/local/share/applications/LFF-Office/LFF-Word/'

    # Create the necessary directories
    os.makedirs(destination_dir, exist_ok=True)

    # Copy each lffofficeword.py file individually
    for file in lffword_python:
        filename = os.path.basename(file)
        destination = os.path.join(destination_dir, filename)
        shutil.copy2(file, destination)
    for file in lffword_png:
        filename = os.path.basename(file)
        destination = os.path.join(destination_dir, filename)
        shutil.copy2(file, destination)

    with open(desktop_entry_file, 'w') as f:
        f.write(desktop_entry)

    # Set execute permissions on the desktop entry file
    os.chmod(desktop_entry_file, 0o755)

# Run the create_desktop_entry() function to create the desktop entry
create_desktop_entry()
print('LFF Office Word has been successfully installed!')
