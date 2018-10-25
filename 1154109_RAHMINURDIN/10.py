import shapefile #mengimpor modul shapefil
w=shapefile.Writer() #untuk membuat shapefile baru
w.shapeType #menyeting menggunakan jenis shape apa (point,polygon)
#membuat dbs dengan 2 field, berupa kolom
w.field("Nama Bidang","Bidang Ke")
w.field("Nama Bidang","Bidang Ke") #membuat dbs dengan 2 field, berupa kolom

w.record("belah ketupat","satu")
w.record("belah ketupat","dua")
w.record("belah ketupat","tiga")
w.record("belah ketupat","empat")
w.record("belah ketupat","lima")


#membuat 5 row 
w.poly(parts=[[[-2,1],[-1,2],[-2,3],[-3,2],[-2,1]]],shapeType=shapefile.POLYGON) #mengisi .shp dengan titik point
w.poly(parts=[[[-2,4],[-1,6],[-2,8],[-3,6],[-2,4]]],shapeType=shapefile.POLYGON) #mengisi .shp dengan titik point
w.poly(parts=[[[2,-1],[1,-2],[2,-3],[3,-2],[2,-1]]],shapeType=shapefile.POLYGON) #mengisi .shp dengan titik point
w.poly(parts=[[[-4,-1],[-2,-4],[-4,-7],[-6,-4],[-4,-1]]],shapeType=shapefile.POLYGON) #mengisi .shp dengan titik point
w.poly(parts=[[[6,2],[8,4],[6,6],[4,4],[6,2]]],shapeType=shapefile.POLYGON) #mengisi .shp dengan titik point

w.save("soal10")#melakukan save dengan nama (soal10)