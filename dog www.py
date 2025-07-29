from tkinter import *
import requests #для загрузки изображений из интернета
from PIL import Image, ImageTk
from io import BytesIO #для обработки изображений
from tkinter import messagebox as mb
from tkinter import ttk


def show_image():
    image_url = get_doc_image()#ссылка на картинку с помощью гет док имадж
    if image_url:#если ссылка не пустая
        try:
            response = requests.get(image_url, stream=True) #ответ будет равен запросу получаем из интернета
            response.raise_for_status() #обрабатываем ошибки
            img_data = BytesIO(response.content)
            img = Image.open(img_data)
            img.thumbnail((300,300))
            img = ImageTk.PhotoImage(img)
            label.config(image=img)#загружаем в метку изображение
            label.image = img #чтобы компьютер в мусор не выкинул
        except Exception as e:
            mb.showerror('Ошибка',"Возникла ошибка {e}")
    progress.stop()



def get_doc_image():#будем по ссылке обращаться к сайту док сео
    try:
        response = requests.get('https://dog.ceo/api/breeds/image/random')#этот респонс получит из интернета
        #респонс это штука на которую прилетает ссылка на картинку
        response.raise_for_status() #если статус не 200 , а другое , то не найден
        data = response.json() #получить изображение
        return data['message']
    except Exception as e:
        mb.showerror("Ошибка","Возникла ошибка при загрузке API {e}")
        return None #возвращаем пустоту после ошибки


def prog():
    progress['value'] = 0
    progress.start(30) #один раз в милиссекунды
    window.after(3000, show_image)


window = Tk()
window.title("Картинки собачки")
window.geometry('360x420')

label= ttk.Label()#тут будут выходить картинки
label.pack(pady=10)


button = ttk.Button(text="Загрузить изображение", command=prog)
button.pack(pady=10)

#линия загрузки изображения
progress = ttk.Progressbar(mode='determinate', length=300)
progress.pack(pady=10)




window.mainloop()
