import cv2
img = cv2.imread("img1.png")

while True:
     
    cv2.imshow("Kitty", img)
    
    #if we've waited at least 1 ms AND we've pressed the esc
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows() 


    
        
