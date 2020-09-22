
import cv2 
import numpy as np 
#!rescale saja default 75 persen dari 640x320
def rescale_frame(frame,percent=75):
    width=int(frame.shape[1]* percent/100)
    height=int(frame.shape[0]* percent/100)
    dim = (width,height)
    return cv2.resize(frame,dim,interpolation=cv2.INTER_AREA)
##! port webcam di sesuaikan 0 untuk internal dan lainya untuk external
cap = cv2.VideoCapture(0)

while(True):  
    _, frame = cap.read()
    image = rescale_frame(frame,percent=100)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    edge = cv2.Canny(gray,120,100)
    contours , hierarchy = cv2.findContours(edge,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    jumlah = str(len(contours))
    print("jumlah objek : ",jumlah)
    result_contour =  cv2.drawContours(image,contours,-1,(0,255,0),2)
    ##! tambahan 
    for i in range (int(jumlah)):
    ##! perhatikan jika nilai perimeter =0 maka akan muncul error  zero division
        area = cv2.contourArea(contours[i])          
        perimeter = cv2.arcLength(contours[i],True)
        TR=(4*np.pi*area)/(perimeter**2)
####? nilai TR ukur sendiri sesuai hasil dari benda dan labeli nama dengan bentuknya masing masing
        if TR<=0.6:
             bentuk='Segitiga'
        elif TR>0.6:
             bentuk='persegi panjang '
        # else:
        #     bentuk='lainnya'
        print('Nilai Thinnes Ratio : ', TR)
        print('Bentuk benda :',bentuk)
    cv2.imshow("result_contour",result_contour)
   # cv2.imshow("kamera",image)
    cv2.imshow("Canny",edge)
    
    
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27: # esc key
        break
cv2.waitKey(0) 
cv2.destroyAllWindows() 

