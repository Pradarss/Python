import PIL
img = cv2. imread('X.jpg',2)
ret, bw_img = cv2. threshold(img,127,255,cv2.THRESH_BINARY)
cv2. imshow("Binary Image",bw_img)
cv2. waitKey(0)
