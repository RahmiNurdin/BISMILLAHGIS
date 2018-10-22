import shapefile 
e=shapefile.Writer() 
e.shapeType 
e.field("kolom1","C") 
e.field("kolom2","C") 
e.record("ngek","satu") 

e.line(parts=[[[1,5],[5,5],[5,1],[3,3],[1,1]]]) 
e.save("emping") 