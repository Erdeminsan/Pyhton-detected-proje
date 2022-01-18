import time

import cv2

from tkinter import messagebox

cap = cv2.VideoCapture(0) #kamera açmak için

mycasecade = cv2.CascadeClassifier("C:\cascade\classifier\\cascade.xml")
mycascade_g = cv2.CascadeClassifier("C:\cascade-g\classifier\\cascade.xml")
font1 = cv2.FONT_HERSHEY_SIMPLEX

while 1:
    ret, frame = cap.read()  #ret, çerçeve mevcutsa true değerini döndüren boolean bir değişkendir
    frame = cv2.flip(frame, 1)
    # flip methodu diziyi eksen etrafında çevirmede kullanılır.(frame,1) y ekseninde çevir anlamına gelir
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    baret = mycasecade.detectMultiScale(gray, 1.3, 7)
    gozluk = mycascade_g.detectMultiScale(gray, 1.3, 7) #Algılanan nesneleri bir dikdörtgenler listesi olarak döndürür.
    if baret in mycasecade.detectMultiScale(gray, 1.3, 7):
        for (x, y, w, h) in baret:
            #time.sleep(1)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
            cv2.putText(frame, "Baret", (x, y), font1, 0.5, (0, 255, 0), cv2.LINE_4)
            if baret in mycasecade.detectMultiScale(gray, 1.3, 7):
                #messagebox.showinfo("KONTROL", "BARETİNİZ VAR ")
                print("BARETİNİZ VAR ")
    if gozluk in mycascade_g.detectMultiScale(gray, 1.3, 7):
        for (x, y, w, h) in gozluk:
            #time.sleep(1)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
            cv2.putText(frame, "Gozluk", (x, y), font1, 0.5, (0, 255, 0), cv2.LINE_4)
            if gozluk in mycascade_g.detectMultiScale(gray, 1.3, 7):
                #messagebox.showinfo("KONTROL", "GÖZLÜĞÜNÜZ VAR ")
                print("GÖZLÜĞÜNÜZ VAR ")
    if gozluk in mycascade_g.detectMultiScale(gray, 1.3, 7) and baret in mycasecade.detectMultiScale(gray, 1.3, 7):
        #messagebox.showinfo("KONTROL", "GÜVENLİ GEÇİŞ")
        print("GÜVENLİ GEÇİŞ")
    else:
        print("EKİPMANLARI KONTROL EDİNİZ")
    cv2.imshow("Kontrol Sistemi ", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):#Bir tuşa basana kadar ekranın açık kalmasını sağlar
        break


cap.release()
cv2.destroyAllWindows()
