import shapefile #merupakan pyshp yang tadi telah diinstal
w=shapefile.Writer() #mendeklarasikan file shapefile yang baru
w.shapeType #mengecek type dari writer yang dibuat diatas

w.field("kolom1","C") #membuat field dengan nama kolom1 dan dengan type character
w.field("kolom2","C") #membuat field dengan nama kolom2  dan dengan type character

w.record("ngek","satu") #mengisi record dari field yang telah dibuatkan

w.poly(parts=[[[1,3],[5,3]]], shapeType=shapefile.POLYLINE) #membuatgaris, berdasarkan titik koordinat yang telah ditentukan dengan tipe shapenya poliline/garis yang menyatu.

w.save("soal6") #yang berada didalam kurung merupakn nama file yang telah/akan di save