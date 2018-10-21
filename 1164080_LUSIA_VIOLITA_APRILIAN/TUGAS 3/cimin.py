import shapefile 
c=shapefile.Writer(shapeType=1) 
c.shapeType 
c.shapeType=3 
c.shapeType 
c.field("kolom1","C") 
c.field("kolom2","C") 
c.record("ngek","satu") 
c.record("ngok","dua") 
c.point(1,1) 
c.point(2,2) 
c.save("cimin") 