import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import json


image = cv2.imread("ara.png")


decodedObjects = pyzbar.decode(image)
for obj in decodedObjects:
    print("Type:", obj.type)
    ou_data = obj.data
    print("Data: ", obj.data, "\n")

print('ou_data',ou_data,type(ou_data))
value = ou_data.decode('utf-8')
value = json.loads(value.replace("'",'"'))
print(value,type(value))

print("Name: ", value['name'])
print("DOB: ", value['DOB'])
print("Address: ",value['address'])

cv2.imshow("Frame", image)
cv2.waitKey(0)


