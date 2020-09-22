# Deteksi bentuk
import cv2
import numpy as np

# Load an image and convert to binary
img1 = cv2.imread('segitiga.jpeg',0)    # 0 : load as grayscale
                                     # 1 : load as color
ret,img2 = cv2.threshold(img1, 50, 255, cv2.THRESH_BINARY)

# Object segmentation
#image,cnt, hier = cv2.findContours(img2,
#                  cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt, hier = cv2.findContours(img2,
            cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# Thinnes ratio
area = cv2.contourArea(cnt[0])          # contour ke-0
perimeter = cv2.arcLength(cnt[0],True)
TR=(4*np.pi*area)/(perimeter**2)

# Object detection
if TR>0.85:
   bentuk='Bundar'
elif TR>0.70:
   bentuk='Persegi'
else:
   bentuk='Segitiga'
print('Nilai Thinnes Ratio : ', TR)
print('Bentuk benda :',bentuk)

# Display image
cv2.imshow('Benda',img1)
cv2.waitKey(0)          # Menunggu keyboard ditekan
cv2.destroyAllWindows() # Window dari image hilang
