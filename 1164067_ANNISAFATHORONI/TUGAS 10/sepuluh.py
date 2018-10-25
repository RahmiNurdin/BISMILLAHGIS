import shapefile
w=shapefile.Writer()
w.shapeType

w.field("kolom1","C")
w.field("kolom2","C")

w.record("ngek","satu") 
w.record("crot","dua")
w.record("crit","tiga")
w.record("crut","empat")
w.record("cret","lima")
w.record("crat","enam")



w.poly(parts=[[[1,3],[5,3], [5,2],[1,2],[1,3]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[1,7],[3,7], [3,12],[1,12],[1,7]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[-10,0],[-5,0], [-5,3],[-10,3],[-10,0]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[-3,-1],[0,-1], [0,4],[-3,4],[-3,-1]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[2,4],[7,4], [7,6],[2,6],[2,4]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[20,20],[10,20], [10,15],[20,15],[20,20]]],shapeType=shapefile.POLYLINE)



w.save("soal10") 
 