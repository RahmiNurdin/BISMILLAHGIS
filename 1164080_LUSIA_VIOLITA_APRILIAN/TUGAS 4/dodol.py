import shapefile 
d=shapefile.Writer(shapefile.POINTM) 
d.shapeType 
d.field("kolom1","C") 
d.field("kolom2","C") 
d.record("ngek","satu") 
d.record("ngok","dua") 
d.point(1,1) 
d.point(2,2) 
d.save("dodol") 