import shapefile
b=shapefile.Writer(shapeType=1)
b.shapeType 
b.field("kolom1","C")
b.field("kolom2","C") 
b.record("ngek","satu")
b.record("ngok","dua") 
b.point(1,1)
b.point(2,2) 
b.save("bakpao")