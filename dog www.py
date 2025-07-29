from tkinter import *
import requests #для загрузки изображений из интернета
from PIL import Image, ImageTk
from io import BytesIO #для обработки изображений

window = Tk()
window.title("Картинки собачки")
window.geometry('360x420')

label= Label()#тут будут выходить картинки
label.pack(pady=10)


button = Button(text="Загрузить изображение", command=show_image)
button.pack(pade=10)





window.mainloop()
