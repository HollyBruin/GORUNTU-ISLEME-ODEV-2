import cv2
import numpy as np

# Kamera başlatma
cap = cv2.VideoCapture(1)

while True:
    # Kameradan bir çerçeve al
    ret, frame = cap.read()

    # Görüntüyü HSV formatına dönüştür
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Renk aralıklarını belirleme (kırmızı ve kırmızıya yakın tonlar için HSV)
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # Belirlenen renk aralığındaki pikselleri beyaz yapma, diğer pikselleri siyah yapma
    mask = cv2.inRange(hsv_frame, lower_red, upper_red)

    # Orijinal görüntüde yalnızca belirlenen renkleri gösterme
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Görüntüleri gösterme
    cv2.imshow('Original', frame)
    cv2.imshow('Result', result)

    # Çıkış için "q" tuşuna basınca döngüyü sonlandır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera kapatma ve pencereyi kapatma
cap.release()
cv2.destroyAllWindows()
