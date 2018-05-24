import cv2
import numpy as np

#cap değişkenine görüntü kaydedildi
frame = cv2.imread('frame.jpg',)
input = cv2.imread('frame.jpg',)
blur = cv2.blur(frame,(25,25))

#hsv=Hue, Saturation, Lightness(Value)
gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
hsv = cv2.cvtColor(rgb, cv2.COLOR_BGR2HSV)

#Filtreleme aralığı belirleniyor
l_beyaz = np.array([ 0, 0, 190])
u_beyaz = np.array([255,255,255])

#Maskeleme yapılır
mask = cv2.inRange(hsv, l_beyaz, u_beyaz)

#Bölgeler bululnuyor
cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
center = None

#maskeleme gösteriliyor
cv2.imshow('mask', mask)

#kaç bölgenin maskelendiği a'ya yazdırırlıyor
a= len(cnts)
print(a)

#Eksik yumurta varsa hata veriyor
if a != 12:
    cv2.putText(frame, "HATALI", (200,400), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),5)

cv2.putText(frame, str(a), (100,200), cv2.FONT_HERSHEY_SIMPLEX, 6,(0, 255, 0),5)
cv2.imwrite('/home/pi/Documents/Yumurta/mask.jpg', mask)
cv2.imwrite('/home/pi/Documents/Yumurta/output.jpg', frame)
cv2.imshow('frame',frame)
cv2.imshow('input',input)

#kapatmak icin herhangibir tusa basılması bekleniyor
cv2.waitKey(0)
cv2.destroyAllWindows ()
