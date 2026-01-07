#/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Boone.gpkg


# from pathlib import Path
# import geopandas as gpd
# import fiona

# input_dir = Path("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Nearest Features")
# output_dir = Path("/Users/ep9k/Desktop/BRE_Data_Exports/Nearest Features")
# output_dir.mkdir(parents=True, exist_ok=True)

# for gpkg in input_dir.glob("*.gpkg"):
#     layers = fiona.listlayers(gpkg)

#     for layer in layers:
#         gdf = gpd.read_file(gpkg, layer=layer)
#         out_file = output_dir / f"{gpkg.stem}.geojson"
#         gdf.to_file(out_file, driver="GeoJSON")
        
        
        
        
        

from pathlib import Path
import shutil

src = Path("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone7")
dst = Path("/Users/ep9k/Desktop/BRE_Data_Exports/Zones/Zone7")

dst.mkdir(parents=True, exist_ok=True)

for gpkg in src.glob("*.gpkg"):
    shutil.copy2(gpkg, dst)


