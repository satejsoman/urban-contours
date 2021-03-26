using Shapefile 
using VegaLite

path = string(homedir(), "/Documents/workspace/research/slum-mapping/DLR/Endergebnis/Mumbai_Change_Detection_1973_1990_2001_2010.shp")
gdf  = Shapefile.Table(path)

gdf |>
@vlplot(
    :geoshape,
    data = :geometry    
)