'''Многопроцессорный генератор отчетов
- Процесс DataFetcher получает данные из API (можно замокать).
- Процесс ReportGenerator формирует PDF-отчет (шаблон reportlab).
- Свяжите процессы через multiprocessing.Queue.

'''

import multiprocessing
import time
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import pdfencrypt

def func(q):
    print('Получаем данные из API')
    time.sleep(2)
    x={"title": "Отчет", "content": "Это пример отчета, сгенерированного на основе данных API."}
    q.put(x)
    print('Данные отправлены')

def func1(q):
    print("Ожидание данных для отчета...")
    x = q.get() 
    print("Данные получены для генерации отчета.")
    

    file = "/Users/ksenia/Downloads/Новая папка/report.pdf"
    c = canvas.Canvas(file, pagesize=letter)
    pdfencrypt.registerFont(TTFont('Arial', '/path/to/Arial.ttf'))  # Путь к шрифту

# Устанавливаем шрифт
    c.setFont("Arial", 12)

    c.drawString(100, 750, f"Название: {x['title']}")
    c.drawString(100, 730, f"Содержание: {x['content']}")
    c.save()
    
    print(f"Отчет сгенерирован и сохранен в {file}")  

if __name__=='__main__':
    q=multiprocessing.Queue()
    t1=multiprocessing.Process(target=func,args=(q,))   
    t2=multiprocessing.Process(target=func1,args=(q,))   
    t1.start()
    t2.start()
    t1.join()
    t2.join()  
