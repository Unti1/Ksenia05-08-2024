'''Многопроцессорная обработка изображений
- Запустите 4 процесса через multiprocessing.Process.
- Каждый процесс применяет фильтр (например, инверсия цвета) к разным изображениям.
- Используйте multiprocessing.Queue для передачи путей к изображениям.

'''
import threading

import time
import random
from multiprocessing import Process,Queue, Pool
from PIL import Image
import numpy as np
q=Queue()

def invert_colors(q):
    while not q.empty():
        input_image_path=q.get()
        image = Image.open(input_image_path)
        image_array = np.array(image)
        inverted_image_array = 255 - image_array
        inverted_image = Image.fromarray(inverted_image_array)
        inverted_image.save(input_image_path)
        inverted_image.show()

x=['/Users/ksenia/Downloads','/Users/ksenia/Downloads','/Users/ksenia/Downloads']

if __name__=='__main__':
    for xx in x:
        q.put(xx)
    x=0
    thread=[]
    for _ in range(4):
        p=Process(target=inve)

              










 







              
        


        
      
      
               
          
             
        
     
     
  
   
    

        
    

   

   





        









