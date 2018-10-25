import shapefile #mengimpor modul shapefil
w=shapefile.Writer() #untuk membuat shapefile baru
w.shapeType #menyeting menggunakan jenis shape apa (point,polygon)
#membuat dbs dengan 2 field, berupa kolom
w.field("Nama Bidang","Bidang Ke")
w.field("Nama Bidang","Bidang Ke") #membuat dbs dengan 2 field, berupa kolom

w.record("jajargenjang","satu")



#membuat 5 row 
w.poly(parts=[[[-2,1],[-1,2],[-2,3],[-3,2],[-2,1]]],shapeType=shapefile.POLYGON) #mengisi .shp dengan titik point

w.save("soal10")#melakukan save dengan nama (soal10)