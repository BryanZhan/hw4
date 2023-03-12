#Different window sizes
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


src=cv.imread("images.jpg",cv.IMREAD_COLOR)
src_gray=cv.cvtColor(src,cv.COLOR_BGR2GRAY)
src_blur=cv.GaussianBlur(src_gray,(5,5),0)

i_x=cv.Sobel(src_blur,cv.CV_64F,1,0)
i_y=cv.Sobel(src_blur,cv.CV_64F,0,1)
i_xx=np.multiply(i_x,i_x)
i_xy=np.multiply(i_x,i_y)
i_yy=np.multiply(i_y,i_y)

k=0.04
det=np.multiply(i_xx,i_yy)-np.multiply(i_xy,i_xy)
trace=i_xx+i_yy
R=det-(k*np.multiply(trace,trace))
thresh=abs(R)>0.0001*abs(R).max()
#cv.imwrite("corner_before_find_local_maximum3.jpg",thresh*255)
l_corner=[]
def CompareToNeighbor(R,x,y):
    #print(x,y)
    temp=R[max(0,y-10):min(R.shape[0],y+11) ,max(0,x-10):min(R.shape[1],x+11) ]
    #print(np.array(temp).shape)
    #print((abs(temp).max()),abs(R[y][x]))
    if((abs(temp).max())==abs(R[y][x])):
        return True
    else:
        return False

for y in range(thresh.shape[0]):
    for x in range(thresh.shape[1]):
        if(thresh[y][x]==True):
            if(CompareToNeighbor(R,x,y)==True):
                l_corner.append((x,y))
for e in l_corner:
    cv.circle(src,(e[0],e[1]),3,(0,0,255),-1)
cv.imwrite("55image.jpg",src)


