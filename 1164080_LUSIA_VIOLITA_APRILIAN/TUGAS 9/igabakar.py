import shapefile 
i=shapefile.Writer() 
i.shapeType 
i.field("kolom1","C") 
i.field("kolom2","C") 
i.record("ngek","satu") 
i.record("crot","dua") 
 
i.poly(parts=[[[1,3],[5,3], [5,2],[1,2], [1,3]]],shapeType=shapefile.POLYLINE)
i.poly(parts=[[[1,6],[5,6], [5,9],[1,9], [1,6]]],shapeType=shapefile.POLYLINE) 
 
i.save("igabakar")