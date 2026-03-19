from itertools import cycle
from PIL import Image, ImageTk
import time 
import tkinter as tk

root=tk.Tk()
root.title("Image slideshow Viewer")

#List of Image Path
image_paths = [
    r"E:\My pictures\IMG_20251216_192836078_HDR_PORTRAIT.jpg",
    r"E:\My pictures\IMG_20251216_191912070_HDR_PORTRAIT.jpg",
    r"E:\My pictures\DSCF0651.JPG",
    r"E:\My pictures\IMG_20250629_124630[1].jpg",
    r"E:\My pictures\JDS_2654.JPG",
]

#Resize the images to 1080x1080
image_size=(1080,1080)
images=[Image.open(path).resize(image_size) for path in image_paths]
photo_images=[ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)

slideshow = cycle(photo_images)

def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()

play_button = tk.Button(root, text='Play Slideshow', command=start_slideshow)
play_button.pack()

root.mainloop()