from tkinter import *
import requests #для загрузки изображений из интернета
from PIL import Image, ImageTk
from io import BytesIO #для обработки изображений
from tkinter import messagebox as mb


def show_image():
    image_url = get_doc_image()#ссылка на картинку с помощью гет док имадж
    if image_url:#если ссылка не пустая
        try:
            response = requests.get(image_url, stream=True)#ответ будет равен запросу получаем из интернета
            response.raise_for_status() #обрабатываем ошибки
            img_data = BytesIO(response.content)
            img = Image.open(img_data)
            img.thumbnail((300,300))
            label.config(image=img)#загружаем в метку изображение
            label.image = img #чтобы компьютер в мусор не выкинул
        except Exception as e:
            mb.showerror('Ошибка',"Возникла ошибка {e}")







window = Tk()
window.title("Картинки собачки")
window.geometry('360x420')

label= Label()#тут будут выходить картинки
label.pack(pady=10)


button = Button(text="Загрузить изображение", command=show_image)
button.pack(pade=10)





window.mainloop()
