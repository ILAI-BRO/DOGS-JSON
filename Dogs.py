from tkinter import *
import requests
from PIL import ImageTk, Image
from io import BytesIO


root = Tk()
root.title("Dogs images")
root.geometry("600x480")


label = Label(root, text="Dogs images")
label.pack(pady=10)

button = Button(text="Загрузить изображение", command=get_image)
button.pack(pady=10)


root.mainloop()
