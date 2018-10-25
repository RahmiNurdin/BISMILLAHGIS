import shapefile 
j=shapefile.Writer() 
j.shapeType 
j.field("kolom1","C") 
j.field("kolom2","C") 
j.record("shape1","satu") 
j.record("shape2","dua")
j.record("shape3","tiga")
j.record("shape4","empat") 
j.record("shape5","lima")
j.record("shape6","enam")
j.record("shape7","tujuh") 
j.record("shape8","delapan")
 
j.poly(parts=[[[-1,1],[5,1], [2,9],[-1,1]]],shapeType=shapefile.POLYLINE)
j.poly(parts=[[[6,2],[10,2], [8,7],[6,2]]],shapeType=shapefile.POLYLINE)
j.poly(parts=[[[-10,2],[-6,2], [-8,7],[-10,2]]],shapeType=shapefile.POLYLINE) 
j.poly(parts=[[[-5,2],[-3,2], [-4,8],[-5,2]]],shapeType=shapefile.POLYLINE)
j.poly(parts=[[[0,-10],[4,-10], [2,-1],[0,-10]]],shapeType=shapefile.POLYLINE)
j.poly(parts=[[[-10,-10],[-4,-10], [-7,-1],[-10,-10]]],shapeType=shapefile.POLYLINE)
j.poly(parts=[[[20,-10],[26,-10], [23,-1],[20,-10]]],shapeType=shapefile.POLYLINE)
j.poly(parts=[[[-1,-20],[5,-20], [2,-11],[-1,-20]]],shapeType=shapefile.POLYLINE)

j.save("jenang")