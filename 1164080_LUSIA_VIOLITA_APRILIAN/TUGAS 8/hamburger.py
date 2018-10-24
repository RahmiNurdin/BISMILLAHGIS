import shapefile
h=shapefile.Writer()
h.shapeType 
h.field("kolom1","C")
h.field("kolom2","C") 
h.record("ngek","satu")
h.poly(parts=[[[1,3],[5,3],[1,2],[5,2], [1,3]]],shapeType=shapefile.POLYLINE) 
h.save("hamburger") 