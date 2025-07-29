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
            img_size = (int(width_spinbox.get()), int(height_spinbox.get()))
            img.thumbnail(img_size)
            img = ImageTk.PhotoImage(img)
            # new_window = Toplevel(window)
            # new_window.title("случайное изображение")
            tab = ttk.Frame(notebook) #таб занчит хзакладка
            notebook.add(tab, text=f"Картинка №{notebook.index('end') + 1}") #адд значит добавить
            lb = ttk.Label(tab, image=img)
            lb.pack(padx=10,pady=10)
            lb.image = img
            # label.config(image=img)#загружаем в метку изображение
            # label.image = img #чтобы компьютер в мусор не выкинул
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

#создаем вручную размер изображения
width_lebel = ttk.Label(text= 'Ширина:')
width_lebel.pack(side='left', padx=(10, 0))#лефт к левой стороне прижата, падх обозначает , что слева будет отступ 10 пикселей, а справа 0 отступ
width_spinbox = ttk.Spinbox(from_=200, to=500, increment=50, width=5)
width_spinbox.pack(side='left', padx=(0, 10))
height_label = ttk.Label(text='Высота: ')
height_label.pack(side='left', padx=(10, 0))
height_spinbox = ttk.Spinbox(from_=200, to=500, increment=50, width=5)
height_spinbox.pack(side='left', padx=(0, 10))

#добавляем виджет Notepad
#теперь будет не много новвых окон, а одно , но с закладкамии
top_level_window = Toplevel(window)
top_level_window.title("Изображение собачек")
notebook = ttk.Notebook(top_level_window)
notebook.pack(expand=True, fill='both', padx=10, pady=10)#чтобы заполнить всё пространство


window.mainloop()
