from PIL import Image
from tkinter import filedialog as fd
import os

FORMATS = (
    '.png', 
    '.jpg', 
    '.jpeg',
    '.bmp',
    '.gif',
    '.webp',
    '.tiff'
)
dir = fd.askdirectory()

for name in os.listdir(dir):
    f = os.path.join(dir, name).replace("\\","/")
    # checking if it is a file
    if f.lower().endswith(FORMATS):
        input = Image.open(f)
        input = input.convert('RGB')
        output = os.path.splitext(f)[0]+'.jpg'
        input.save(output, "JPEG",  optimize=True, quality=90, progressive=True)