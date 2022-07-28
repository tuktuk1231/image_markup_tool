import json
import cv2
import glob
import os
import numpy as np

img = []
n = 0
z = 0
h = ''
name = list(os.walk('dataset/'))
f = open('config.json')
data = json.load(f)
f1 = open('category.json')
data1 = json.load(f1)
newname = []
types =['.jpeg','.jpg','.png','.bmp','.gif']

listfiles = [os.path.join(root, file) for root, dirs, files in os.walk("dataset") for file in files]
for file in listfiles:
    name, type = os.path.splitext(file)
    if type in types:
        newname.append(file)
        z += 1

while 1:
    k = cv2.waitKey(0)
    if k == ord(data['HOT_KEY']['previous']):
        if n == 0:
            n = z-1
        else:
            n -= 1

    if k == ord(data['HOT_KEY']['next']):
        if n == z-1:
            n = 0
        else:
            n += 1

    if k == (data['HOT_KEY']['category']):
        print('Введите категорию изображения '+newname[n])
        kz = int(input())
        while kz > (len(data1['category'])):
            print('Такой категории нет!')
            print('Введите категорию еще раз:')
            kz = int(input())

        for i in range(len(data1['category'])):
            last_category = i
            if data1['category'][str(i+1)] == (data1['category'][str(kz)]):
                h = str(data1['category'][str(kz)])+str(' (')+str(i+1)+str(')')
        if not os.path.isdir(data1['category'][str(kz)]):
            os.mkdir(data1['category'][str(kz)])


    if k == (data['HOT_KEY']['save']):
        if kz == 0:
            print('Категория не была введена!')
            kz = int(input())
        img = cv2.imread(newname[n])
        save_dir = '%04i.jpg' % n


        cv2.imwrite(os.path.join(data1['category'][str(kz)], save_dir), img)
        print('Изображение: ', newname[n], ' Сохранено в папку: ',  data1['category'][str(kz)])

    if k == (data['HOT_KEY']['exit']):
        print('выход')
        break

    img = cv2.imread(newname[n])
    res_img = cv2.resize(img, (500, 500), cv2.INTER_NEAREST)
    constant = cv2.copyMakeBorder(res_img, 0, 50, 0, 0, cv2.BORDER_CONSTANT, value=[255,255,255])
    cv2.putText(constant, str(h), (0, 530), cv2.FONT_HERSHEY_SIMPLEX, 1, [0, 0, 0], 2)
    cv2.imwrite('output.png', constant)
    h = ''
    cv2.imshow("Display window", constant)




