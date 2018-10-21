import shapefile #merupakan pyshp yang tadi telah diinstal
w=shapefile.Writer(shapeType=1) #mendeklarasikan file shapefile yang baru
w.shapeType  #mengecek type dari writer yang dibuat diatas
w.shapeType=3  #mengatur jenis bentuk
w.shapeType  #mengecek type dari writer yang dibuat diatas
 

w.field("kolom1","C") #membuat field dengan nama kolom1 dan dengan type character
w.field("kolom2","C") #membuat field dengan nama kolom2  dan dengan type character

w.record("ngek","satu") #mengisi record dari field yang telah dibuatkan (untuk kolom 1)
w.record("ngok","dua") #mengisi record dari field yang telah dibuatkan (untuk kolom 2)

w.point(1,1) #menggunakan titik/point sebagai penanda dengan titik koordinat 1,1
w.point(2,2) #menggunakan titik/point sebagai penanda dengan titik koordinat 2,2

w.save("soal3") #yang berada didalam kurung merupakn nama file yang telah/akan di save