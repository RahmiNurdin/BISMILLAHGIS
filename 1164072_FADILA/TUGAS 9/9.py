import shapefile #merupakan pyshp yang tadi telah diinstal

w=shapefile.Writer()  #mendeklarasikan file shapefile yang baru

w.shapeType #mengecek type dari writer yang dibuat diatas



w.field("kolom1","C") #membuat field dengan nama kolom1 dan dengan type character

w.field("kolom2","C") #membuat field dengan nama kolom2  dan dengan type character



w.record("ngek","satu") #mengisi record dari field yang telah dibuatkan

w.record("crot","dua") #mengisi record dari field yang telah dibuatkan







w.poly(parts=[[[1,3],[5,3], [5,2],[1,2], [1,3]]],shapeType=shapefile.POLYLINE) #menggunakan shapetype polyline yang dimana titik koordinat pertama akan bertemu dengan ujung nya.

w.poly(parts=[[[1,6],[5,6], [5,9],[1,9], [1,6]]],shapeType=shapefile.POLYLINE) #menggunakan shapetype polyline yang dimana titik koordinat pertama akan bertemu dengan ujung nya.

 



w.save("soal9") #yang berada didalam kurung merupakn nama file yang telah/akan di save