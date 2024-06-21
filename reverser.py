import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageOps
import os


AUTHOR = r""" 

made by:
   _____           _   _     
  / ____|         | | (_)    
 | |    _   _ _ __| |_ _ ___ 
 | |   | | | | '__| __| / __|
 | |___| |_| | |  | |_| \__ \
  \_____\__,_|_|   \__|_|___/
                             
(for N forum...)"""

def reverse_image(image_path, destination_path=None):
    image = Image.open(image_path)
    # reverse the image
    reversed_image = ImageOps.mirror(image)
    # save the reversed image
    if destination_path is None:
        destination_path = os.path.join(os.path.dirname(image_path), f'reversed_{os.path.basename(image_path)}')
    reversed_image.save(destination_path)
    print(f'{image_path} -> {destination_path}')

def reverse_folder(folder_path):
    # create a folder called 'reversed_{folder_path}' in the same directory
    reversed_folder_path = os.path.join(os.path.dirname(folder_path), f'reversed_{os.path.basename(folder_path)}')
    os.makedirs(reversed_folder_path, exist_ok=True)
    # iterate over all files in the folder
    for file_name in os.listdir(folder_path):
        # reverse the image
        if file_name.endswith('.jpg') or file_name.endswith('.png'):
            reverse_image(os.path.join(folder_path, file_name), os.path.join(reversed_folder_path, file_name))

def main():
    print(AUTHOR)
    root = tk.Tk()
    root.withdraw()
    try:
        folder_path = filedialog.askdirectory()
        reverse_folder(folder_path)
    except FileNotFoundError:
        print('No folder selected\nExiting... (bozo)')
        return

if __name__ == '__main__':
    main()