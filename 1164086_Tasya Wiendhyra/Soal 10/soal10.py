import shapefile #merupakan pyshp yang tadi telah diinstal
w=shapefile.Writer()  #mendeklarasikan file shapefile yang baru
w.shapeType #mengecek type dari writer yang dibuat diatas

w.field("kolom1","C") #membuat field dengan nama kolom1 dan dengan type character
w.field("kolom2","C") #membuat field dengan nama kolom2  dan dengan type character

w.record("levi","satu") #mengisi record dari field yang telah dibuatkan
w.record("eren","dua") #mengisi record dari field yang telah dibuatkan
w.record("saitama","tiga") #mengisi record dari field yang telah dibuatkan
w.record("wolfram","empat") #mengisi record dari field yang telah dibuatkan
w.record("aot","lima") #mengisi record dari field yang telah dibuatkan
w.record("onepunch","enam") #mengisi record dari field yang telah dibuatkan
w.record("kaneki","tujuh") #mengisi record dari field yang telah dibuatkan
w.record("arima","delapan") #mengisi record dari field yang telah dibuatkan


#membuat trapesium ada 8 buah
w.poly(parts=[[[2,0], [7,0], [6,3], [3,3], [2,0]]],shapeType=shapefile.POLYLINE) #menggunakan shapetype polyline yang dimana titik koordinat pertama akan bertemu dengan ujung nya membentuk trapesium.
w.poly(parts=[[[-5,4], [1,4], [0,7], [-3,7], [-5,4]]],shapeType=shapefile.POLYLINE) #menggunakan shapetype polyline yang dimana titik koordinat pertama akan bertemu dengan ujung nya membentuk trapesium.
w.poly(parts=[[[-4,-2], [6,-2], [3,1], [-2,1], [-4,-2]]],shapeType=shapefile.POLYLINE) #menggunakan shapetype polyline yang dimana titik koordinat pertama akan bertemu dengan ujung nya membentuk trapesium.
w.poly(parts=[[[8,0], [13,0], [12,6], [9,6], [8,0]]],shapeType=shapefile.POLYLINE) #menggunakan shapetype polyline yang dimana titik koordinat pertama akan bertemu dengan ujung nya membentuk trapesium.
w.poly(parts=[[[-4,-12], [6,-12], [3,-6], [-2,-6], [-4,-12]]],shapeType=shapefile.POLYLINE) #menggunakan shapetype polyline yang dimana titik koordinat pertama akan bertemu dengan membentuk trapesium.
w.poly(parts=[[[-16,-12], [-6,-12], [-9,-6], [-13,-6], [-16,-12]]],shapeType=shapefile.POLYLINE) #menggunakan shapetype polyline yang dimana titik koordinat pertama akan bertemu dengan ujung nya membentuk trapesium.
w.poly(parts=[[[7,-12], [17,-12], [15,-6], [10,-6], [7,-12]]],shapeType=shapefile.POLYLINE) #menggunakan shapetype polyline yang dimana titik koordinat pertama akan bertemu dengan ujung nya membentuk trapesium.
w.poly(parts=[[[-16,-5], [-6,-5], [-9,3],[-13,3], [-16,-5]]],shapeType=shapefile.POLYLINE) #menggunakan shapetype polyline yang dimana titik koordinat pertama akan bertemu dengan ujung nyamembentuk trapesium.


w.save("soal10") #yang berada didalam kurung merupakn nama file yang telah/akan di save