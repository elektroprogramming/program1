
import cv2 
import numpy as np 
#!rescale saja default 75 persen dari 640x320
def rescale_frame(frame,percent=75):
    width=int(frame.shape[1]* percent/100)
    height=int(frame.shape[0]* percent/100)
    dim = (width,height)
    return cv2.resize(frame,dim,interpolation=cv2.INTER_AREA)
##! port webcam di sesuaikan 0 untuk internal dan lainya untuk external
cap = cv2.VideoCapture(2)
while(True):  
    
    _, frame = cap.read()
    image = rescale_frame(frame,percent=50)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    ##! nilai 50 dan 400 atur sesuai dengan pencahayaan dan benda yang mau di deteksi
    edged = cv2.Canny(gray, 50, 200) 
    contours, hierarchy = cv2.findContours(edged,  
        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
    jumlah = str(len(contours))
    print("Number of Contours found = " + jumlah) 
    jumlah=int(jumlah)
   # print(jumlah)
    ##?perhitungan kontur untuk setiap benda yang terhitung
    for i in range (jumlah):
    ##! perhatikan jika nilai perimeter =0 maka akan muncul error  zero division
        area = cv2.contourArea(contours[i])          
        perimeter = cv2.arcLength(contours[i],True)
        TR=(4*np.pi*area)/(perimeter**2)
####? nilai TR ukur sendiri sesuai hasil dari benda dan labeli nama dengan bentuknya masing masing
        if TR<=0.73:
            bentuk='persegi panjang'
        elif TR>0.73:
            bentuk='persegi '
        else:
            bentuk='lainnya'
        print('Nilai Thinnes Ratio : ', TR)
        print('Bentuk benda :',bentuk)

  #  cv2.imshow('Canny Edges After Contouring', edged)   
    result=cv2.drawContours(image, contours, -1, (0, 255, 0), 3) 
    cv2.imshow('result', result) 
    cv2.imshow('Contours', edged) 
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27: # esc key
        break
cv2.waitKey(0) 
cv2.destroyAllWindows() 
