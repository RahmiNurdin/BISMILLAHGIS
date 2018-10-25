import shapefile #mengimpor modul shapefil
w=shapefile.Writer() #untuk membuat shapefile baru
w.shapeType #menyeting menggunakan jenis shape apa (point,polygon)
#membuat dbs dengan 2 field, berupa kolom
w.field("Nama Bidang","Bidang Ke")
w.field("Nama Bidang","Bidang Ke")
#membuat dbs dengan 2 field, berupa kolom
w.record("Segitiga Sama kaki","one")
w.record("Segitiga Sama kaki","two")
w.record("Segitiga Sama kaki","three")
w.record("Segitiga Sama kaki","four")
w.record("Segitiga Sama kaki","five")
w.record("Segitiga Sama kaki","six")
w.record("Segitiga Sama kaki","seven")



#membuat 7 row karena menggunakan 
w.poly(parts=[[[-7,4],[-5,4], [-6,1],[-7,4]]],shapeType=shapefile.POLYGON) #mengisi .shp dengan titik point
w.poly(parts=[[[-7,-1],[-3,-2], [-7,-3],[-7,-1]]],shapeType=shapefile.POLYGON) #mengisi .shp dengan titik point
w.poly(parts=[[[-4,1],[-2,1], [-3,4],[-4,1]]],shapeType=shapefile.POLYGON) #mengisi .shp dengan titik point
w.poly(parts=[[[4,-1],[5,-4], [3,-4],[4,-1]]],shapeType=shapefile.POLYGON) #mengisi .shp dengan titik point
w.poly(parts=[[[-4,-3],[-2,-3], [-3,-6],[-4,-3]]],shapeType=shapefile.POLYGON) #mengisi .shp dengan titik point
w.poly(parts=[[[1,-1],[3,-1], [2,-4],[1,-1]]],shapeType=shapefile.POLYGON) #mengisi .shp dengan titik point
w.poly(parts=[[[-7,5],[-7,7], [-4,6],[-7,5]]],shapeType=shapefile.POLYGON) #mengisi .shp dengan titik point
w.save("soal10")#melakukan save dengan nama (soal1)