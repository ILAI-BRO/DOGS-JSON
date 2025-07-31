from tkinter import *
from tkinter import messagebox
import requests
from PIL import ImageTk, Image
from io import BytesIO






def show_img():
    img_url = get_img()
    if img_url:
        try:
            response = requests.get(img_url, stream=True)
            response.raise_for_status()
            img_data=BytesIO(response.content)
            img = Image.open(img_data)
            img.thumbnail((300, 300))
            label.config(image=img)
            label.image = img

        except Exception as e:
            messagebox.showerror("Ошибка!", e)




root = Tk()
root.title("Dogs images")
root.geometry("600x480")


label = Label(root, text="Dogs images")
label.pack(pady=10)

button = Button(text="Загрузить изображение", command=show_img)
button.pack(pady=10)


root.mainloop()
