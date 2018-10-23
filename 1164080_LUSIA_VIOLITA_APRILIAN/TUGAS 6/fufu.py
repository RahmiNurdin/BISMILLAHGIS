import shapefile 
f=shapefile.Writer() 
f.shapeType 
f.field("kolom1","C") 
f.field("kolom2","C") 
f.record("ngek","satu") 

f.poly(parts=[[[1,3],[5,3]]], shapeType=shapefile.POLYLINE) 
f.save("fufu")