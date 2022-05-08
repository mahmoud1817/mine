import cv2 ; from numpy import *
# img = cv2.imread('c:/users/mahmoud/desktop/learn/res/images/css.png' , 0)
# img = cv2.resize(img,(400,400)) # (0,0,fx=0.5,fy=0.5)
# img = cv2.rotate(img,cv2.cv2.ROTATE_90_CLOCKWISE)
# cv2.imgwrite('modified.jpg',img)

# print(img)
# part=img[100:150,100:150]
# img[150:200,150:200] = part

# cv2.imshow('Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)

while True:
    a ,b = cap.read()
    w=int(cap.get(3))
    h=int(cap.get(4))

    # image = zeros(b.shape,uint8)
    # sf= cv2.resize(b,(0,0),fx=0.5,fy=0.5)

    # image[:h//2, :w//2] = cv2.rotate(sf,cv2.cv2.ROTATE_180)
    # image[h//2:, :w//2] = sf
    # image[:h//2, w//2:] = cv2.rotate(sf,cv2.cv2.ROTATE_180) 
    # image[h//2:, w//2:] = sf

    cv2.imshow('WTitle',b)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()