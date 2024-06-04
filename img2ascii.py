import cv2
import numpy as np
img=cv2.imread("")#Enter your path
img=cv2.resize(img,(100,100))
aimg=np.array(img)


si=100
asc=[['.']*si for i in range(si)]
for i in range(0,si):
    for j in range(0,si):
        s=sum(aimg[i][j])//3
        if s<1:
            asc[i][j]='#'
        elif s<10:
            asc[i][j]='$'
        elif s<50:
            asc[i][j]='&'
        elif s<100:
            asc[i][j]='?'
        elif s<150:
            asc[i][j]='^'
        elif s<200:
            asc[i][j]=','
        else:
            asc[i][j]='.'
for i in asc:
    for j in i:
        print(j,end='')
    print()

