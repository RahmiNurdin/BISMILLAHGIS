import shapefile #mengimpor modul shapefil
j=shapefile.Writer() #untuk membuat shapefile baru
j.shapeType #menyeting menggunakan jenis shape apa (point,polygon)

#membuat dbs dengan 2 field, berupa kolom
j.field("Bentuknya","ke") 
j.field("Bentuknya","ke") 

#membuat dbs dengan 2 field, berupa kolom
j.record("EXO1","one") 
j.record("EXO2","two")
j.record("EXO3","three")
j.record("EXO4","four") 
j.record("EXO5","five")
j.record("EXO6","six")
j.record("EXO7","seven") 
 
#membuat 7 row karena menggunakan 
#mengisi .shp dengan titik point
j.poly(parts=[[[20,-10],[26,-10], [23,-1],[20,-10]]],shapeType=shapefile.POLYLINE)
j.poly(parts=[[[-1,1],[5,1], [2,9],[-1,1]]],shapeType=shapefile.POLYLINE)
j.poly(parts=[[[-5,2],[-3,2], [-4,8],[-5,2]]],shapeType=shapefile.POLYLINE)
j.poly(parts=[[[-10,2],[-6,2], [-8,7],[-10,2]]],shapeType=shapefile.POLYLINE) 
j.poly(parts=[[[-10,-10],[-4,-10], [-7,-1],[-10,-10]]],shapeType=shapefile.POLYLINE)
j.poly(parts=[[[6,2],[10,2], [8,7],[6,2]]],shapeType=shapefile.POLYLINE)


j.save("soal10")