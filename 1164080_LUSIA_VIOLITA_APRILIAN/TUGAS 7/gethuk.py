import shapefile 
g=shapefile.Writer() 
g.shapeType 
g.field("kolom1","C") 
g.field("kolom2","C") 
g.record("ngek","satu") 

g.poly(parts=[[[1,3],[5,3],[1,2],[5,2]]],shapeType=shapefile.POLYLINE) 
g.save("gethuk")