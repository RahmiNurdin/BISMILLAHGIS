import shapefile
w=shapefile.Writer()
w.shapeType

w.field("kolom1","C")
w.field("kolom2","C")

w.record("ngek","satu")
w.record("crot","dua")
w.record("ngik","tiga")
w.record("crit","empat")
w.record("ngok","lima")
w.record("crat","enam")
w.record("ngak","tujuh")
w.record("crut","delapan")




w.poly(parts=[[[5,0],[10,0], [10,5],[5,5], [5,0]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[-2,-2],[-2,1], [1,1],[1,-2], [-2,-2]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[1,7],[3,7], [3,9],[1,9], [1,7]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[-1,-7],[-3,-7], [-3,-9],[-1,-9], [-1,-7]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[15,0],[20,0], [20,5],[15,5], [15,0]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[-5,-7],[-3,-7], [-3,-9],[-5,-9], [-5,-7]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[5,7],[3,7], [3,9],[5,9], [5,7]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[1,-6],[4,-6], [4,-3],[1,-3], [1,-6]]],shapeType=shapefile.POLYLINE)


w.save("soal10")