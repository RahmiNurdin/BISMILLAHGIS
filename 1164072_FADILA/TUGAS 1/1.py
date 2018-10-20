import shapefile #import modul yang bernama shapefile
w=shapefile.Writer() #sebagai pendeklarasian variabel
w.shapeType #menjalankan perintah pendeklarasian variabel diatas
 
w.field("kolom1","C") #membuat field/kolom dengan type character
w.field("kolom2","C") #membuat field/kolom dengan type character
 
w.record("ngek","satu") #mengisi kolom1 yang telah dibuat diatas
w.record("ngok","dua") #mengisi kolom2 yang telah dibuat diatas
 
w.point(1,1) #membuat titik 1,1
w.point(2,2) #membuat titik 2,2
 
w.save("soal1") #untuk menyimpan soal1