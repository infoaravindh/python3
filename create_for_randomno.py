
"""
Created on Fri May  3 15:01:17 2019

@author: Aravindhan
"""
import barcode
import random

def barcode_generator():
    num =  random.randrange(1,1000000000000)
    print(num)
    image = barcode.get_barcode_class('ean13')
    image_bar = image(u'{}'.format(num))
    file = open('E:\Python\Barcode\\aa.svg',"wb")
    image_bar.write(file)
    return("barcode generated successfully")

barcode_generator() 

   
    

