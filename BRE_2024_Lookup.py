import pandas as pd
import geopandas as gpd
from shapely import wkt


### potential lookup field later if needed
# compare to counties. Need to import county data
ashe = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Counties/Ashe_County.gpkg')
avery = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Counties/Avery_County.gpkg')
alleghany = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Counties/Alleghany_County.gpkg')
caldwell = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Counties/Caldwell_County.gpkg')
watauga = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Counties/Watauga_County.gpkg')
wilkes = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Counties/Wilkes_County.gpkg')
johnson = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Counties/Johnson_County.gpkg')
carter = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Counties/Carter_County.gpkg')

# dictionary of counties and their corresponding names with salesforce id
counties = {
    'ashe': (ashe, 'a2E3u000000fSaIEAU'),
    'avery': (avery, 'a2E3u000000fSaSEAU'),
    'alleghany': (alleghany, 'a2E3u000000fSaXEAU'),
    'caldwell': (caldwell, 'a2E3u000000fSaJEAU'),
    'watauga': (watauga, 'a2E3u000000fSaYEAU'),
    'wilkes': (wilkes, 'a2E3u000000fSaTEAU'),
    'johnson': (johnson, 'a2E3u000000fSaZEAU'),
    'carter': (carter, 'a2E3u000000fSacEAE'),
}



#All custom areas filepaths
bannerelk = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Banner Elk.gpkg')
beechmountain = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Beech Mountain.gpkg')
bethel = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Bethel.gpkg')
blowingrock = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Blowing Rock.gpkg')
boone = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Boone.gpkg')
butler = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Butler.gpkg')
collettsville = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Collettsville.gpkg')
creston = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Creston.gpkg')
crossnore = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Crossnore.gpkg')
crumpler = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Crumpler.gpkg')
deepgap = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Deep Gap.gpkg')
elkpark = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Elk Park.gpkg')
fleetwood = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Fleetwood.gpkg')
foscoe = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Foscoe.gpkg')
glendalesprings = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Glendale Springs.gpkg')
grassycreek = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Grassy Creek.gpkg')
hampton = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Hampton.gpkg')
jefferson = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Jefferson.gpkg')
lansing = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Lansing.gpkg')
laurelbloomery = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Laurel Bloomery.gpkg')
laurelsprings = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Laurel Springs.gpkg')
linville = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Linville.gpkg')
matney = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Matney.gpkg')
minneapolis = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Minneapolis.gpkg')
mountaincity = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Mountain City.gpkg')
newland = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Newland.gpkg')
pineola = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Pineola.gpkg')
pineycreek = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Piney Creek.gpkg')
roanmountain = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Roan Mountain.gpkg')
scottville = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Scottville.gpkg')
sevendevils = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Seven Devils.gpkg')
shadyvalley = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Shady Valley.gpkg')
sparta = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Sparta.gpkg')
sugargrove = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Sugar Grove.gpkg')
sugarmountain = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Sugar Mountain.gpkg')
todd = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Todd.gpkg')
trade = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Trade.gpkg')
triplett = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Triplett.gpkg')
vallecrucis = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Valle Crucis.gpkg')
vilas = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Vilas.gpkg')
warrensville = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Warrensville.gpkg')
wataugalake = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Watauga Lake.gpkg')
westjefferson = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/West Jefferson.gpkg')
zionville = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Custom Areas/Zionville.gpkg')


# Dictionary of custom areas and their corresponding GeoDataFrames and id from salesforce
custom_areas = {
    'bannerelk': (bannerelk, 'a2E3u000000fPH4EAM'),
    'beechmountain': (beechmountain, 'a2E3u000000fPH5EAM'),
    'bethel': (bethel, 'a2E3u000000fPH6EAM'),
    'blowingrock': (blowingrock, 'a2E3u000000fPH7EAM'),
    'boone': (boone, 'a2E3u000000fPH8EAM'),
    'butler': (butler, 'a2E3u000000fPTxEAM'),
    'collettsville': (collettsville, 'a2E3u000000fPH9EAM'),
    'creston': (creston, 'a2E3u000000fPHAEA2'),
    'crossnore': (crossnore, 'a2E3u000000fPHBEA2'),
    'crumpler': (crumpler, 'a2E3u000000fPHCEA2'),
    'deepgap': (deepgap, 'a2E3u000000fPHDEA2'),
    'elkpark': (elkpark, 'a2E3u000000fPHEEA2'),
    'fleetwood': (fleetwood, 'a2E3u000000fPHFEA2'),
    'foscoe': (foscoe, 'a2E3u000000fPHGEA2'),
    'glendalesprings': (glendalesprings, 'a2E3u000000fPHHEA2'),
    'grassycreek': (grassycreek, 'a2E3u000000fPHIEA2'),
    'hampton': (hampton, 'a2E3u000000fPTyEAM'),
    'jefferson': (jefferson, 'a2E3u000000fPHJEA2'),
    'lansing': (lansing, 'a2E3u000000fPHKEA2'),
    'laurelbloomery': (laurelbloomery, 'a2E3u000000fPTzEAM'),
    'laurelsprings': (laurelsprings, 'a2E3u000000fPHLEA2'),
    'linville': (linville, 'a2E3u000000fPHMEA2'),
    'matney': (matney, 'a2E3u000000fPHNEA2'),
    'minneapolis': (minneapolis, 'a2E3u000000fPHOEA2'),
    'mountaincity': (mountaincity, 'a2E3u000000fPU0EAM'),
    'newland': (newland, 'a2E3u000000fPHdEAM'),
    'pineola': (pineola, 'a2E3u000000fPHPEA2'),
    'pineycreek': (pineycreek, 'a2E3u000000fPHQEA2'),
    'roanmountain': (roanmountain, 'a2E3u000000fPU1EAM'),
    'scottville': (scottville, 'a2E3u000000fPHREA2'),
    'sevendevils': (sevendevils, 'a2E3u000000fPHSEA2'),
    'shadyvalley': (shadyvalley, 'a2E3u000000fPU2EAM'),
    'sparta': (sparta, 'a2E3u000000fPHTEA2'),
    'sugargrove': (sugargrove, 'a2E3u000000fPHUEA2'),
    'sugarmountain': (sugarmountain, 'a2E3u000000fPHVEA2'),
    'todd': (todd, 'a2E3u000000fPHWEA2'),
    'trade': (trade, 'a2E3u000000fPU9EAM'),
    'triplett': (triplett, 'a2E3u000000fPHXEA2'),
    'vallecrucis': (vallecrucis, 'a2E3u000000fPHYEA2'),
    'vilas': (vilas, 'a2E3u000000fPHZEA2'),
    'warrensville': (warrensville, 'a2E3u000000fPHaEAM'),
    'wataugalake': (wataugalake, 'a2E3u000000fPU3EAM'),
    'westjefferson': (westjefferson, 'a2E3u000000fPHbEAM'),
    'zionville': (zionville, 'a2E3u000000fPHcEAM')
}


#All zone filepaths
Zone1a = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone1/Zone1a.gpkg")
Zone1b = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone1/Zone1b.gpkg")
Zone1c = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone1/Zone1c.gpkg")
Zone1d = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone1/Zone1d.gpkg")
Zone1e = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone1/Zone1e.gpkg")
Zone1f = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone1/Zone1f.gpkg")
Zone1g = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone1/Zone1g.gpkg")
Zone1h = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone1/Zone1h.gpkg")
Zone1i = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone1/Zone1i.gpkg")
Zone1j = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone1/Zone1j.gpkg")
Zone2a = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone2/Zone2a.gpkg")
Zone2b = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone2/Zone2b.gpkg")
Zone2c = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone2/Zone2c.gpkg")
Zone2d = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone2/Zone2d.gpkg")
Zone2e = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone2/Zone2e.gpkg")
Zone2f = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone2/Zone2f.gpkg")
Zone2g = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone2/Zone2g.gpkg")
Zone2h = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone2/Zone2h.gpkg")
Zone2i = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone2/Zone2i.gpkg")
Zone2j = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone2/Zone2j.gpkg")
Zone3a = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone3/Zone3a.gpkg")
Zone3b = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone3/Zone3b.gpkg")
Zone3c = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone3/Zone3c.gpkg")
Zone3d = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone3/Zone3d.gpkg")
Zone3e = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone3/Zone3e.gpkg")
Zone3f = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone3/Zone3f.gpkg")
Zone3g = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone3/Zone3g.gpkg")
Zone4a = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone4/Zone4a.gpkg")
Zone4b = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone4/Zone4b.gpkg")
Zone4c = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone4/Zone4c.gpkg")
Zone4d = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone4/Zone4d.gpkg")
Zone4e = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone4/Zone4e.gpkg")
Zone4f = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone4/Zone4f.gpkg")
Zone4g = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone4/Zone4g.gpkg")
Zone4h = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone4/Zone4h.gpkg")
Zone4i = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone4/Zone4i.gpkg")
Zone5a = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone5/Zone5a.gpkg")
Zone5b = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone5/Zone5b.gpkg")
Zone5c = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone5/Zone5c.gpkg")
Zone5d = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone5/Zone5d.gpkg")
Zone5e = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone5/Zone5e.gpkg")
Zone5f = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone5/Zone5f.gpkg")
Zone5g = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone5/Zone5g.gpkg")
Zone5h = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone5/Zone5h.gpkg")
Zone5i = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone5/Zone5i.gpkg")
Zone5j = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone5/Zone5j.gpkg")
Zone5k = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone5/Zone5k.gpkg")
Zone5l = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone5/Zone5l.gpkg")
Zone5m = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone5/Zone5m.gpkg")
Zone5n = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone5/Zone5n.gpkg")
Zone5o = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone5/Zone5o.gpkg")
Zone6a = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone6/Zone6a.gpkg")
Zone7a = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone7/Zone7a.gpkg")
Zone7b = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone7/Zone7b.gpkg")
Zone7c = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone7/Zone7c.gpkg")
Zone7d = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone7/Zone7d.gpkg")
Zone7e = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone7/Zone7e.gpkg")
Zone7f = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone7/Zone7f.gpkg")
Zone7g = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone7/Zone7g.gpkg")
Zone7h = gpd.read_file("/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone7/Zone7h.gpkg")


# dictionary of zones with their corresponding geodatafame and id from salesforce
zones = {
    'Zone1a': (Zone1a, 'a2E3u000000fSaKEAU'),
    'Zone1b': (Zone1b, 'a2E3u000000fSahEAE'),
    'Zone1c': (Zone1c, 'a2E3u000000fSaLEAU'),
    'Zone1d': (Zone1d, 'a2E3u000000fSaiEAE'),
    'Zone1e': (Zone1e, 'a2E3u000000fSajEAE'),
    'Zone1f': (Zone1f, 'a2E3u000000fSakEAE'),
    'Zone1g': (Zone1g, 'a2E3u000000fSblEAE'),
    'Zone1h': (Zone1h, 'a2E3u000000fSbmEAE'),
    'Zone1i': (Zone1i, 'a2E3u000000fSbnEAE'),
    'Zone1j': (Zone1j, 'a2E3u000000fSaMEAU'),
    'Zone2a': (Zone2a, 'a2E3u000000fSboEAE'),
    'Zone2b': (Zone2b, 'a2E3u000000fSbpEAE'),
    'Zone2c': (Zone2c, 'a2E3u000000fSaUEAU'),
    'Zone2d': (Zone2d, 'a2E3u000000fSbqEAE'),
    'Zone2e': (Zone2e, 'a2E3u000000fSbrEAE'),
    'Zone2f': (Zone2f, 'a2E3u000000fSbuEAE'),
    'Zone2g': (Zone2g, 'a2E3u000000fSbzEAE'),
    'Zone2h': (Zone2h, 'a2E3u000000fSbvEAE'),
    'Zone2i': (Zone2i, 'a2E3u000000fSdHEAU'),
    'Zone2j': (Zone2j, 'a2E3u000000fSdIEAU'),
    'Zone3a': (Zone3a, 'a2E3u000000fSbwEAE'),
    'Zone3b': (Zone3b, 'a2E3u000000fSdMEAU'),
    'Zone3c': (Zone3c, 'a2E3u000000fSdREAU'),
    'Zone3d': (Zone3d, 'a2E3u000000fSdSEAU'),
    'Zone3e': (Zone3e, 'a2E3u000000fSc0EAE'),
    'Zone3f': (Zone3f, 'a2E3u000000fSc1EAE'),
    'Zone3g': (Zone3g, 'a2E3u000000fSdNEAU'),
    'Zone4a': (Zone4a, 'a2E3u000000fSbxEAE'),
    'Zone4b': (Zone4b, 'a2E3u000000fSc2EAE'),
    'Zone4c': (Zone4c, 'a2E3u000000fSdJEAU'),
    'Zone4d': (Zone4d, 'a2E3u000000fSc3EAE'),
    'Zone4e': (Zone4e, 'a2E3u000000fSdWEAU'),
    'Zone4f': (Zone4f, 'a2E3u000000fSdKEAU'),
    'Zone4g': (Zone4g, 'a2E3u000000fSdOEAU'),
    'Zone4h': (Zone4h, 'a2E3u000000fSdPEAU'),
    'Zone4i': (Zone4i, 'a2E3u000000fWdQEAU'),
    'Zone5a': (Zone5a, 'a2E3u000000fSdLEAU'),
    'Zone5b': (Zone5b, 'a2E3u000000fSdXEAU'),
    'Zone5c': (Zone5c, 'a2E3u000000fSdTEAU'),
    'Zone5d': (Zone5d, 'a2E3u000000fSdYEAU'),
    'Zone5e': (Zone5e, 'a2E3u000000fSdbEAE'),
    'Zone5f': (Zone5f, 'a2E3u000000fSdgEAE'),
    'Zone5g': (Zone5g, 'a2E3u000000fSdUEAU'),
    'Zone5h': (Zone5h, 'a2E3u000000fSdhEAE'),
    'Zone5i': (Zone5i, 'a2E3u000000fSdVEAU'),
    'Zone5j': (Zone5j, 'a2E3u000000fSdQEAU'),
    'Zone5k': (Zone5k, 'a2E3u000000fSdiEAE'),
    'Zone5l': (Zone5l, 'a2E3u000000fSdlEAE'),
    'Zone5m': (Zone5m, 'a2E3u000000fSalEAE'),
    'Zone5n': (Zone5n, 'a2E3u000000fSdqEAE'),
    'Zone5o': (Zone5o, 'a2E3u000000fWdVEAU'),
    'Zone6a': (Zone6a, 'a2E3u000000fSdcEAE'),
    'Zone7a': (Zone7a, 'a2E3u000000fSdmEAE'),
    'Zone7b': (Zone7b, 'a2E3u000000fSddEAE'),
    'Zone7c': (Zone7c, 'a2E3u000000fSdeEAE'),
    'Zone7d': (Zone7d, 'a2E3u000000fSdvEAE'),
    'Zone7e': (Zone7e, 'a2E3u000000fSdZEAU'),
    'Zone7f': (Zone7f, 'a2E3u000000fSdaEAE'),
    'Zone7g': (Zone7g, 'a2E3u000000fSe5EAE'),
    'Zone7h': (Zone7h, 'a2E3u000000fSdwEAE')
}




# Nearest Features calculations
wataugariver = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Nearest Features/WataugaRiver.gpkg')
nforknewriver = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Nearest Features/NewRiverNorthFork.gpkg')
sforknewriver = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Nearest Features/NewRiverSouthFork.gpkg')
wataugalake = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Nearest Features/WataugaLake.gpkg')


# Creeks
minor_creeks = gpd.read_file('/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Nearest Features/MinorCreeks_HighCountryArea.gpkg')


creeks = {
    'Adams Branch': 'a2E3u000000fg2tEAA',
    'Aho Branch': 'a2E3u000000fg2uEAA',
    'Andy Branch': 'a2E3u000000fg2vEAA',
    'Arnold Branch': 'a2E3u000000fg2wEAA',
    'Asher Branch': 'a2E3u000000fg2xEAA',
    'Ashley Branch': 'a2E3u000000fg2yEAA',
    'Atchison Branch': 'a2E3u000000fg2zEAA',
    'Avery Branch': 'a2E3u000000fg30EAA',
    'Bailey Camp Creek': 'a2E3u000000fg31EAA',
    'Baird\'s Creek': 'a2E3u000000fg32EAA',
    'Baker Branch': 'a2E3u000000fg33EAA',
    'Ballew Creek': 'a2E3u000000fg34EAA',
    'Banjo Branch': 'a2E3u000000fg35EAA',
    'Barry Branch': 'a2E3u000000fg36EAA',
    'Bear Branch': 'a2E3u000000fg37EAA',
    'Bear Creek': 'a2E3u000000fg38EAA',
    'Bear Den Branch': 'a2E3u000000fg39EAA',
    'Beaver Branch': 'a2E3u000000fg3AEAQ',
    'Beaver Creek': 'a2E3u000000fg3BEAQ',
    'Beaverdam Creek': 'a2E3u000000fg3CEAQ',
    'Bee Branch': 'a2E3u000000fg3DEAQ',
    'Bee Cove Branch': 'a2E3u000000fg3EEAQ',
    'Bee Tree Creek': 'a2E3u000000fg3FEAQ',
    'Beech Creek': 'a2E3u000000fg3GEAQ',
    'Ben Bolen Creek': 'a2E3u000000fg3HEAQ',
    'Berry Branch': 'a2E3u000000fg3IEAQ',
    'Big Branch': 'a2E3u000000fg3JEAQ',
    'Big Dry Run': 'a2E3u000000fg3KEAQ',
    'Big Horse Creek': 'a2E3u000000fg3LEAQ',
    'Big Laurel Creek': 'a2E3u000000fg3MEAQ',
    'Big Sandy Creek': 'a2E3u000000fg3NEAQ',
    'Big Windfall Branch': 'a2E3u000000fg3OEAQ',
    'Bill White Creek': 'a2E3u000000fg3PEAQ',
    'Birchfield Creek': 'a2E3u000000fg3QEAQ',
    'Black Branch': 'a2E3u000000fg3REAQ',
    'Black Mountain Branch': 'a2E3u000000fg3SEAQ',
    'Blackman Branch': 'a2E3u000000fg3TEAQ',
    'Bledsoe Creek': 'a2E3u000000fg3UEAQ',
    'Blevins Creek': 'a2E3u000000fg3VEAQ',
    'Blood Camp Branch': 'a2E3u000000fg3WEAQ',
    'Boomer Branch': 'a2E3u000000fg3XEAQ',
    'Boone Branch': 'a2E3u000000fg3YEAQ',
    'Boone Camp Branch': 'a2E3u000000fg3ZEAQ',
    'Boone Creek': 'a2E3u000000fg3aEAA',
    'Boone Fork': 'a2E3u000000fg3bEAA',
    'Bowlin Creek': 'a2E3u000000fg3cEAA',
    'Bowling Branch': 'a2E3u000000fg3dEAA',
    'Brickyard Branch': 'a2E3u000000fg3eEAA',
    'Brown Branch': 'a2E3u000000fg3fEAA',
    'Browns Branch': 'a2E3u000000fg3gEAA',
    'Brush Creek': 'a2E3u000000fg3hEAA',
    'Brush Fork': 'a2E3u000000fg3iEAA',
    'Brushy Fork': 'a2E3u000000fg3jEAA',
    'Buck Creek': 'a2E3u000000fg3kEAA',
    'Buck Ridge Branch': 'a2E3u000000fg3lEAA',
    'Buckeye Creek': 'a2E3u000000fg3mEAA',
    'Buffalo Creek': 'a2E3u000000fg3nEAA',
    'Bulldog Creek': 'a2E3u000000fg3oEAA',
    'Bullhead Creek': 'a2E3u000000fg3pEAA',
    'Bunton Branch': 'a2E3u000000fg3qEAA',
    'Bunton Creek': 'a2E3u000000fg3rEAA',
    'Buttermilk Branch': 'a2E3u000000fg3sEAA',
    'Cabbage Creek': 'a2E3u000000fg3tEAA',
    'Call Creek': 'a2E3u000000fg3uEAA',
    'Camp Branch': 'a2E3u000000fg3vEAA',
    'Campbell Creek': 'a2E3u000000fg3wEAA',
    'Cannon Branch': 'a2E3u000000fg3xEAA',
    'Capley Branch': 'a2E3u000000fg3yEAA',
    'Carriger Spring Branch': 'a2E3u000000fg3zEAA',
    'Carroll Branch': 'a2E3u000000fg40EAA',
    'Cheek Branch': 'a2E3u000000fg41EAA',
    'Chestnut Branch': 'a2E3u000000fg42EAA',
    'China Creek': 'a2E3u000000fg43EAA',
    'Christian Branch': 'a2E3u000000fg44EAA',
    'Clark Branch': 'a2E3u000000fg45EAA',
    'Clark Creek': 'a2E3u000000fg46EAA',
    'Clarke Creek': 'a2E3u000000fg47EAA',
    'Claybank Creek': 'a2E3u000000fg48EAA',
    'Clear Branch': 'a2E3u000000fg49EAA',
    'Clear Creek': 'a2E3u000000fg4AEAQ',
    'Clingman Mine Branch': 'a2E3u000000fg4BEAQ',
    'Cobb Creek': 'a2E3u000000fg4CEAQ',
    'Cold Branch': 'a2E3u000000fg4DEAQ',
    'Cole Branch': 'a2E3u000000fg4EEAQ',
    'Cook Branch': 'a2E3u000000fg4FEAQ',
    'Copeland Creek': 'a2E3u000000fg4GEAQ',
    'Copley Branch': 'a2E3u000000fg4HEAQ',
    'Corn Creek': 'a2E3u000000fg4IEAQ',
    'Cornett Branch': 'a2E3u000000fg4JEAQ',
    'Corum Branch': 'a2E3u000000fg4KEAQ',
    'Couches Creek': 'a2E3u000000fg4LEAQ',
    'Cove Creek': 'a2E3u000000fg4MEAQ',
    'Cow Camp Creek': 'a2E3u000000fg4NEAQ',
    'Crab Fork': 'a2E3u000000fg4OEAQ',
    'Craborchard Creek': 'a2E3u000000fg4PEAQ',
    'Cranberry Creek': 'a2E3u000000fg4QEAQ',
    'Creasey Branch': 'a2E3u000000fg4REAQ',
    'Cress Branch': 'a2E3u000000fg4SEAQ',
    'Crooked Branch': 'a2E3u000000fg4TEAQ',
    'Crossnore Creek': 'a2E3u000000fg4UEAQ',
    'Curtis Creek': 'a2E3u000000fg4VEAQ',
    'Cut Laurel Creek': 'a2E3u000000fg4WEAQ',
    'Dale Neely Branch': 'a2E3u000000fg4XEAQ',
    'David Blevins Branch': 'a2E3u000000fg4YEAQ',
    'Days Creek': 'a2E3u000000fg4ZEAQ',
    'Dennis Creek': 'a2E3u000000fg4aEAA',
    'Dixon Creek': 'a2E3u000000fg4bEAA',
    'Doe Branch': 'a2E3u000000fg4cEAA',
    'Doe Creek': 'a2E3u000000fg4dEAA',
    'Doe Fork': 'a2E3u000000fg4eEAA',
    'Dog Creek': 'a2E3u000000fg4fEAA',
    'Doll Branch': 'a2E3u000000fg4gEAA',
    'Doubles Branch': 'a2E3u000000fg4hEAA',
    'Drake Branch': 'a2E3u000000fg4iEAA',
    'Draught Creek': 'a2E3u000000fg4jEAA',
    'Dry Branch': 'a2E3u000000fg4kEAA',
    'Drystone Branch': 'a2E3u000000fg4lEAA',
    'Duck Branch': 'a2E3u000000fg4mEAA',
    'Dugger Branch': 'a2E3u000000fg4nEAA',
    'Dutch Creek': 'a2E3u000000fg4oEAA',
    'Dye Leaf Branch': 'a2E3u000000fg4pEAA',
    'E H Phillippi Branch': 'a2E3u000000fg4qEAA',
    'Eager Branch': 'a2E3u000000fg4rEAA',
    'Elk Creek': 'a2E3u000000fg4zEAA',
    'Ellison Branch': 'a2E3u000000fg50EAA',
    'Evans Branch': 'a2E3u000000fg51EAA',
    'Ezra Fork': 'a2E3u000000fg52EAA',
    'Fall Branch': 'a2E3u000000fg53EAA',
    'Fall Creek': 'a2E3u000000fg54EAA',
    'Fees Branch': 'a2E3u000000fg55EAA',
    'Fenner Branch': 'a2E3u000000fg56EAA',
    'Fiddlers Branch': 'a2E3u000000fg57EAA',
    'Five Poplar Branch': 'a2E3u000000fg58EAA',
    'Flannery Fork': 'a2E3u000000fg59EAA',
    'Flat Spring Branch': 'a2E3u000000fg5AEAQ',
    'Flat Springs Branch': 'a2E3u000000fg5BEAQ',
    'Flat Top Branch': 'a2E3u000000fg5CEAQ',
    'Flattop Creek': 'a2E3u000000fg5DEAQ',
    'Flowers Branch': 'a2E3u000000fg5EEAQ',
    'Forest Grove Creek': 'a2E3u000000fg5FEAQ',
    'Forge Creek': 'a2E3u000000fg5GEAQ',
    'Fork Branch': 'a2E3u000000fg5HEAQ',
    'Fork Creek': 'a2E3u000000fg5IEAQ',
    'Foster Springs Branch': 'a2E3u000000fg5JEAQ',
    'Furnace Creek': 'a2E3u000000fg5KEAQ',
    'Gap Creek': 'a2E3u000000fg5LEAQ',
    'Gap Run': 'a2E3u000000fg5MEAQ',
    'Gentry Branch': 'a2E3u000000fg5NEAQ',
    'Gentry Creek': 'a2E3u000000fg5OEAQ',
    'George Creek': 'a2E3u000000fg5PEAQ',
    'George Gap Branch': 'a2E3u000000fg5QEAQ',
    'Glade Creek': 'a2E3u000000fg5REAQ',
    'Goldmine Branch': 'a2E3u000000fg5SEAQ',
    'Goose Creek': 'a2E3u000000fg5TEAQ',
    'Gouge Branch': 'a2E3u000000fg5UEAQ',
    'Grassy Creek': 'a2E3u000000fg5VEAQ',
    'Grassy Gap Creek': 'a2E3u000000fg5WEAQ',
    'Graybeal Branch': 'a2E3u000000fg5XEAQ',
    'Green Branch': 'a2E3u000000fg5YEAQ',
    'Green Mountain Branch': 'a2E3u000000fg5ZEAQ',
    'Green Mountain Creek': 'a2E3u000000fg5aEAA',
    'Green Ridge Branch': 'a2E3u000000fg5bEAA',
    'Greer Branch': 'a2E3u000000fg5cEAA',
    'Gregg Branch': 'a2E3u000000fg5dEAA',
    'Grindstone Branch': 'a2E3u000000fg5eEAA',
    'Groundhop Branch': 'a2E3u000000fg5fEAA',
    'Hall Branch': 'a2E3u000000fg5gEAA',
    'Hamby Branch': 'a2E3u000000fg5hEAA',
    'Hampton Creek': 'a2E3u000000fg5iEAA',
    'Handpole Branch': 'a2E3u000000fg5jEAA',
    'Hanging Rock Creek': 'a2E3u000000fg5kEAA',
    'Harbin Branch': 'a2E3u000000fg5lEAA',
    'Harrison Branch': 'a2E3u000000fg5mEAA',
    'Haw Branch': 'a2E3u000000fg5nEAA',
    'Hayes Branch': 'a2E3u000000fg5oEAA',
    'Heaberlin Branch': 'a2E3u000000fg5pEAA',
    'Heaton Branch': 'a2E3u000000fg5qEAA',
    'Heaton Creek': 'a2E3u000000fg5rEAA',
    'Helton Creek': 'a2E3u000000fg5sEAA',
    'Henson Creek': 'a2E3u000000fg5tEAA',
    'Hickorynut Branch': 'a2E3u000000fg5uEAA',
    'High Trestle Branch': 'a2E3u000000fg5vEAA',
    'Hignite Branch': 'a2E3u000000fg5wEAA',
    'Hillside Branch': 'a2E3u000000fg5xEAA',
    'Hodges Creek': 'a2E3u000000fg5yEAA',
    'Hog Camp Branch': 'a2E3u000000fg5zEAA',
    'Holloway Branch': 'a2E3u000000fg60EAA',
    'Holly Branch': 'a2E3u000000fg61EAA',
    'Horn Branch': 'a2E3u000000fg62EAA',
    'Horney Branch': 'a2E3u000000fg63EAA',
    'Horse Bottom Creek': 'a2E3u000000fg64EAA',
    'Horse Branch': 'a2E3u000000fg65EAA',
    'Horse Cove Branch': 'a2E3u000000fg66EAA',
    'Horse Creek': 'a2E3u000000fgCZEAY',
    'Hoskin Fork': 'a2E3u000000fgCaEAI',
    'Howard Branch': 'a2E3u000000fgCbEAI',
    'Howard\'s Creek': 'a2E3u000000fgCcEAI',
    'Ingram Branch': 'a2E3u000000fgCdEAI',
    'Isaae Branch': 'a2E3u000000fgCeEAI',
    'James Branch': 'a2E3u000000fgCfEAI',
    'Jenkins Creek': 'a2E3u000000fgCgEAI',
    'Jenny Branch': 'a2E3u000000fgChEAI',
    'Jerd Branch': 'a2E3u000000fgCiEAI',
    'Jerry Creek': 'a2E3u000000fgCjEAI',
    'Jewel Creek': 'a2E3u000000fgCkEAI',
    'Jim Wright Branch': 'a2E3u000000fgClEAI',
    'Joes Creek': 'a2E3u000000fgCmEAI',
    'Johnson Blevins Branch': 'a2E3u000000fgCnEAI',
    'Jones Branch': 'a2E3u000000fgCoEAI',
    'Jones Creek': 'a2E3u000000fgCpEAI',
    'Justice Creek': 'a2E3u000000fgCqEAI',
    'Katy Branch': 'a2E3u000000fgCrEAI',
    'Keller Branch': 'a2E3u000000fgCsEAI',
    'Kentucky Creek': 'a2E3u000000fgCtEAI',
    'Kilby Creek': 'a2E3u000000fgCuEAI',
    'Kirby Branch': 'a2E3u000000fgCvEAI',
    'Lance Creek': 'a2E3u000000fgCwEAI',
    'Laurel Branch': 'a2E3u000000fgCxEAI',
    'Laurel Creek': 'a2E3u000000fgCyEAI',
    'Laurel Fork': 'a2E3u000000fgCzEAI',
    'Laxon Creek': 'a2E3u000000fgD0EAI',
    'Lee Branch': 'a2E3u000000fgD1EAI',
    'Mulberry Creek': 'a2E3u000000fgD2EAI',
    'Left Prong Hampton Creek': 'a2E3u000000fgD3EAI',
    'Leroy Creek': 'a2E3u000000fgD5EAI',
    'Linville Creek': 'a2E3u000000fgD6EAI',
    'Lipford Branch': 'a2E3u000000fgD7EAI',
    'Little Beaverdam Creek': 'a2E3u000000fgD8EAI',
    'Little Buffalo Creek': 'a2E3u000000fgD9EAI',
    'Little Cove Creek': 'a2E3u000000fgDAEAY',
    'Little Creek': 'a2E3u000000fgDBEAY',
    'Little Dry Run': 'a2E3u000000fgDCEAY',
    'Little Elk Creek': 'a2E3u000000fgDDEAY',
    'Little Gap Creek': 'a2E3u000000fgDEEAY',
    'Little Glade Creek': 'a2E3u000000fgDFEAY',
    'Little Helton Creek': 'a2E3u000000fgDGEAY',
    'Little Henson Creek': 'a2E3u000000fgDHEAY',
    'Little Horse Creek': 'a2E3u000000fgDIEAY',
    'Little Laurel Branch': 'a2E3u000000fgDJEAY',
    'Little Laurel Creek': 'a2E3u000000fgDKEAY',
    'Little Naked Creek': 'a2E3u000000fgDLEAY',
    'Little Peak Creek': 'a2E3u000000fgDMEAY',
    'Little Phoenix Creek': 'a2E3u000000fgDNEAY',
    'Little Piney Creek': 'a2E3u000000fgDOEAY',
    'Little Plumtree Creek': 'a2E3u000000fgDPEAY',
    'Little Whiteoak Creek': 'a2E3u000000fgDQEAY',
    'Little Windfall Branch': 'a2E3u000000fgDREAY',
    'Locust Knob Branch': 'a2E3u000000fgDSEAY',
    'Long Branch': 'a2E3u000000fgDTEAY',
    'Long Hope Creek': 'a2E3u000000fgDUEAY',
    'Long Shoals Creek': 'a2E3u000000fgDVEAY',
    'Lost Branch': 'a2E3u000000fgDWEAY',
    'Lumpkin Branch': 'a2E3u000000fgDXEAY',
    'Lunt Branch': 'a2E3u000000fgDYEAY',
    'Mack Branch': 'a2E3u000000fgDZEAY',
    'Maine Branch': 'a2E3u000000fgDaEAI',
    'Mains Branch': 'a2E3u000000fgDbEAI',
    'Maple Branch': 'a2E3u000000fgDcEAI',
    'Martin Branch': 'a2E3u000000fgDdEAI',
    'Martin Creek': 'a2E3u000000fgDeEAI',
    'McCann Branch': 'a2E3u000000fgDfEAI',
    'McEwen Branch': 'a2E3u000000fgDgEAI',
    'McKinney Branch': 'a2E3u000000fgDhEAI',
    'McQueen Branch': 'a2E3u000000fgDiEAI',
    'Meadow Creek': 'a2E3u000000fgDjEAI',
    'Meadow Fork': 'a2E3u000000fgDkEAI',
    'Meat Camp Creek': 'a2E3u000000fgDlEAI',
    'Middle Branch': 'a2E3u000000fgDmEAI',
    'Milam Branch': 'a2E3u000000fgDqEAI',
    'Mill Creek': 'a2E3u000000fgDrEAI',
    'Mill Timber Creek': 'a2E3u000000fgDsEAI',
    'Milligan Branch': 'a2E3u000000fgDtEAI',
    'Millpond Branch': 'a2E3u000000fgDuEAI',
    'Mine Branch': 'a2E3u000000fgDvEAI',
    'Moccasin Creek': 'a2E3u000000fgDwEAI',
    'Mollie Branch': 'a2E3u000000fgDxEAI',
    'Monkey Branch': 'a2E3u000000fgDyEAI',
    'Moody Mill Creek': 'a2E3u000000fgDzEAI',
    'Moreland Branch': 'a2E3u000000fgE0EAI',
    'Morgan Branch': 'a2E3u000000fgE1EAI',
    'Morton Branch': 'a2E3u000000fgE2EAI',
    'Mud Creek': 'a2E3u000000fgE3EAI',
    'Muddy Branch': 'a2E3u000000fgE4EAI',
    'Mutton Creek': 'a2E3u000000fgE5EAI',
    'Naked Creek': 'a2E3u000000fgE6EAI',
    'Nathans Creek': 'a2E3u000000fgE7EAI',
    'New Years Creek': 'a2E3u000000fgE8EAI',
    'No Head Branch': 'a2E3u000000fgE9EAI',
    'Norris Branch': 'a2E3u000000fgEAEAY',
    'Norris Fork': 'a2E3u000000fgEBEAY',
    'Nowhere Branch': 'a2E3u000000fgEJEAY',
    'Obids Creek': 'a2E3u000000fgEKEAY',
    'Old Field Branch': 'a2E3u000000fgELEAY',
    'Old Field Creek': 'a2E3u000000fgEMEAY',
    'Old Fields Creek': 'a2E3u000000fgENEAY',
    'Owens Branch': 'a2E3u000000fgEOEAY',
    'Owl Branch': 'a2E3u000000fgEPEAY',
    'Palmer Branch': 'a2E3u000000fgEQEAY',
    'Parks Branch': 'a2E3u000000fgEREAY',
    'Patrick Branch': 'a2E3u000000fgESEAY',
    'Payne Branch': 'a2E3u000000fgETEAY',
    'Peak Creek': 'a2E3u000000fgEUEAY',
    'Peavine Branch': 'a2E3u000000fgEVEAY',
    'Penley Branch': 'a2E3u000000fgEWEAY',
    'Phillips Branch': 'a2E3u000000fgEXEAY',
    'Phillips Creek': 'a2E3u000000fgEYEAY',
    'Pierce Branch': 'a2E3u000000fgEZEAY',
    'Pigeonroost Creek': 'a2E3u000000fgEaEAI',
    'Pine Branch': 'a2E3u000000fgEbEAI',
    'Pine Mountain Branch': 'a2E3u000000fgEcEAI',
    'Pine Orchard Creek': 'a2E3u000000fgEdEAI',
    'Pine Run': 'a2E3u000000fgEeEAI',
    'Pine Swamp Creek': 'a2E3u000000fgEfEAI',
    'Piney Branch': 'a2E3u000000fgEgEAI',
    'Piney Creek': 'a2E3u000000fgEhEAI',
    'Piney Fork': 'a2E3u000000fgEiEAI',
    'Plumtree Creek': 'a2E3u000000fgEjEAI',
    'Poga Creek': 'a2E3u000000fgEkEAI',
    'Pond Creek': 'a2E3u000000fgElEAI',
    'Potato Creek': 'a2E3u000000fgEmEAI',
    'Potter Branch': 'a2E3u000000fgEnEAI',
    'Pounding Mill Branch': 'a2E3u000000fgEoEAI',
    'Powdermill Creek': 'a2E3u000000fgEpEAI',
    'Prathers Creek': 'a2E3u000000fgEqEAI',
    'Puckett Branch': 'a2E3u000000fgErEAI',
    'Puncheon Camp Branch': 'a2E3u000000fgEsEAI',
    'Pyatt Creek': 'a2E3u000000fgEtEAI',
    'Raccoon Branch': 'a2E3u000000fgEuEAI',
    'Race Path Branch': 'a2E3u000000fgEvEAI',
    'Reece Branch': 'a2E3u000000fgEwEAI',
    'Reese Branch': 'a2E3u000000fgExEAI',
    'Reeves Branch': 'a2E3u000000fgEyEAI',
    'Reservoir Branch': 'a2E3u000000fgEzEAI',
    'Rhinestone Branch': 'a2E3u000000fgF0EAI',
    'Rich Gap Branch': 'a2E3u000000fgF1EAI',
    'Rich Hill Creek': 'a2E3u000000fgF2EAI',
    'Rich Mountain Creek': 'a2E3u000000fgF3EAI',
    'Ripshin Branch': 'a2E3u000000fgF4EAI',
    'Rittle Fork': 'a2E3u000000fgF5EAI',
    'Roan Creek': 'a2E3u000000fgF6EAI',
    'Roaring Branch': 'a2E3u000000fgF7EAI',
    'Roaring Creek': 'a2E3u000000fgF8EAI',
    'Roaring Fork': 'a2E3u000000fgF9EAI',
    'Rock Branch': 'a2E3u000000fgFAEAY',
    'Rock Creek': 'a2E3u000000fgFBEAY',
    'Rockhouse Creek': 'a2E3u000000fgFCEAY',
    'Rocky Branch': 'a2E3u000000fgFDEAY',
    'Roten Creek': 'a2E3u000000fgFEEAY',
    'Roundabout Creek': 'a2E3u000000fgFFEAY',
    'Row Branch': 'a2E3u000000fgFGEAY',
    'Rube Creek': 'a2E3u000000fgFHEAY',
    'Rush Branch': 'a2E3u000000fgFIEAY',
    'Sally Cove Creek': 'a2E3u000000fgFJEAY',
    'Sandbank Creek': 'a2E3u000000fgFKEAY',
    'Sandpit Branch': 'a2E3u000000fgFLEAY',
    'Sawmill Branch': 'a2E3u000000fgFMEAY',
    'Sawyer Creek': 'a2E3u000000fgFNEAY',
    'Scott Branch': 'a2E3u000000fgFOEAY',
    'Seng Cove Branch': 'a2E3u000000fgFPEAY',
    'Shanty Spring Branch': 'a2E3u000000fgFQEAY',
    'Sharp Creek': 'a2E3u000000fgFREAY',
    'Shaw Branch': 'a2E3u000000fgFSEAY',
    'Shawneehaw Creek': 'a2E3u000000fgFTEAY',
    'Shell Creek': 'a2E3u000000fgFUEAY',
    'Shingletown Branch': 'a2E3u000000fgFVEAY',
    'Shippy Branch': 'a2E3u000000fgFWEAY',
    'Shoemaker Branch': 'a2E3u000000fgFXEAY',
    'Shook Branch': 'a2E3u000000fgFYEAY',
    'Shoun Branch': 'a2E3u000000fgFZEAY',
    'Sidney Branch': 'a2E3u000000fgFaEAI',
    'Silas Branch': 'a2E3u000000fgFbEAI',
    'Silas Creek': 'a2E3u000000fgFcEAI',
    'Simcox Branch': 'a2E3u000000fgFdEAI',
    'Simerly Creek': 'a2E3u000000fgFeEAI',
    'Sims Creek': 'a2E3u000000fgFfEAI',
    'Sink Branch': 'a2E3u000000fgFgEAI',
    'Skalley Branch': 'a2E3u000000fgFhEAI',
    'Slabtown Branch': 'a2E3u000000fgFiEAI',
    'Slimp Branch': 'a2E3u000000fgFjEAI',
    'Smith Branch': 'a2E3u000000fgFkEAI',
    'Smitty Branch': 'a2E3u000000fgFlEAI',
    'Snyder Branch': 'a2E3u000000fgFmEAI',
    'Soup Bean Branch': 'a2E3u000000fgFnEAI',
    'South Beaver Creek': 'a2E3u000000fgFoEAI',
    'Lewis Fork': 'a2E3u000000fgFuEAI',
    'Spanish Oak Branch': 'a2E3u000000fgFvEAI',
    'Spear Branch': 'a2E3u000000fgFwEAI',
    'Spice Bottom Creek': 'a2E3u000000fgFxEAI',
    'Spice Branch': 'a2E3u000000fgFyEAI',
    'Spruce Branch': 'a2E3u000000fgFzEAI',
    'Squirrel Creek': 'a2E3u000000fgG0EAI',
    'Stacey Creek': 'a2E3u000000fgG1EAI',
    'Stagg Creek': 'a2E3u000000fgG2EAI',
    'Stalcup Branch': 'a2E3u000000fgG3EAI',
    'Stamey Branch': 'a2E3u000000fgG4EAI',
    'Stanley Branch': 'a2E3u000000fgG5EAI',
    'State Line Branch': 'a2E3u000000fgG6EAI',
    'Steve Phillippi Branch': 'a2E3u000000fgG7EAI',
    'Stone Branch': 'a2E3u000000fgG8EAI',
    'Stone Mountain Branch': 'a2E3u000000fgG9EAI',
    'Stone Mountain Creek': 'a2E3u000000fgGAEAY',
    'Stony Fork': 'a2E3u000000fgGBEAY',
    'Storey Branch': 'a2E3u000000fgGCEAY',
    'Stout Branch': 'a2E3u000000fgGDEAY',
    'Sugar Creek': 'a2E3u000000fgGEEAY',
    'Sugar Hollow Creek': 'a2E3u000000fgGFEAY',
    'Sugar Tree Branch': 'a2E3u000000fgGGEAY',
    'Sumpter Cabin Creek': 'a2E3u000000fgGHEAY',
    'Swift Branch': 'a2E3u000000fgGIEAY',
    'Thaxon Creek': 'a2E3u000000fgGJEAY',
    'Thomas Branch': 'a2E3u000000fgGKEAY',
    'Three Top Creek': 'a2E3u000000fgGLEAY',
    'Threemile Creek': 'a2E3u000000fgGMEAY',
    'Thunderhole Creek': 'a2E3u000000fgGNEAY',
    'Tiger Creek': 'a2E3u000000fgGOEAY',
    'Timothy Branch': 'a2E3u000000fgGPEAY',
    'Tom Baker Branch': 'a2E3u000000fgGQEAY',
    'Toms Branch': 'a2E3u000000fgGREAY',
    'Town Creek': 'a2E3u000000fgGSEAY',
    'Trigger Branch': 'a2E3u000000fgGTEAY',
    'Trim Branch': 'a2E3u000000fgGUEAY',
    'Trivett Branch': 'a2E3u000000fgGVEAY',
    'Trout Creek': 'a2E3u000000fgGWEAY',
    'Turkeypen Branch': 'a2E3u000000fgGXEAY',
    'Valley Creek': 'a2E3u000000fgGZEAY',
    'Vanderpool Creek': 'a2E3u000000fgGaEAI',
    'Vaught Branch': 'a2E3u000000fgGbEAI',
    'Vaught Creek': 'a2E3u000000fgGcEAI',
    'Vile Creek': 'a2E3u000000fgGdEAI',
    'Wallace Branch': 'a2E3u000000fgGeEAI',
    'Ward Branch': 'a2E3u000000fgGfEAI',
    'Waterfalls Creek': 'a2E3u000000fgGgEAI',
    'Waters Branch': 'a2E3u000000fgGhEAI',
    'Watson Branch': 'a2E3u000000fgGiEAI',
    'Webb Creek': 'a2E3u000000fgGjEAI',
    'Whitaker Branch': 'a2E3u000000fgGqEAI',
    'White Pine Creek': 'a2E3u000000fgGrEAI',
    'White Spring Branch': 'a2E3u000000fgGsEAI',
    'Whitehead Branch': 'a2E3u000000fgGtEAI',
    'Whitehead Creek': 'a2E3u000000fgGuEAI',
    'Whiteoak Creek': 'a2E3u000000fgGvEAI',
    'Wildcat Creek': 'a2E3u000000fgGwEAI',
    'Wilson Branch': 'a2E3u000000fgGxEAI',
    'Winkler\'s Creek': 'a2E3u000000fgGyEAI',
    'Wolf Branch': 'a2E3u000000fgGzEAI',
    'Wolfden Branch': 'a2E3u000000fgH0EAI',
    'Wolfpen Creek': 'a2E3u000000fgH1EAI',
    'Woodard Branch': 'a2E3u000000fgH2EAI',
    'Woodward Branch': 'a2E3u000000fgH3EAI',
    'Worley Creek': 'a2E3u000000fgH4EAI',
    'Scrawls Branch': 'a2E3u000000fqXgEAI',
    'East Fork Beaverdam Creek': 'a2E3u000000fqXhEAI',
    'East Fork Fall Branch': 'a2E3u000000fqXiEAI',
    'East Fork Dugger Branch': 'a2E3u000000fqXjEAI',
    'West Fork Buttermilk Branch': 'a2E3u000000fqXkEAI',
    'Lunsford Branch': 'a2E3u000000fqXlEAI',
    'Yokum Branch': 'a2E3u000000fqXmEAI',
    'South Fork McCann Branch': 'a2E3u000000fqXnEAI',
    'Lick Branch': 'a2E3u000000fqXoEAI',
    'West Fork Beaverdam Creek': 'a2E3u000000fqXpEAI',
    'North Fork McCann Branch': 'a2E3u000000fqXqEAI',
    'Low Gap Branch': 'a2E3u000000fqXrEAI',
    'North Fork Gentry Creek': 'a2E3u000000fqXvEAI',
    'West Fork Dugger Branch': 'a2E3u000000fqXwEAI',
    'East Fork Cove Creek': 'a2E3u000000fqXxEAI',
    'North Fork Sawyer Creek': 'a2E3u000000fqXyEAI',
    'Middle Fork South Fork New River': 'a2E3u000000fqXzEAI',
    'Middle Fork Beaverdam Creek': 'a2E3u000000fqY5EAI',
    'E H Phillippi Branch': 'a2E3u000000fqYAEAY',
    'Crooked Branch': 'a2E3u000000fqYBEAY',
    'East Fork Slabtown Branch': 'a2E3u000000fqYCEAY',
    'Howard Creek': 'a2E3u000000fqYDEAY',
    'Middle Fork Drake Branch': 'a2E3u000000fqYFEAY',
    'West Fork Pine Swamp Creek': 'a2E3u000000fqYGEAY',
    'Baird Creek': 'a2E3u000000fqYKEAY',
    'South Fork Ellison Branch': 'a2E3u000000fqYLEAY',
    'Upper Laurel Fork': 'a2E3u000000fqYPEAY',
    'East Fork South Fork New River': 'a2E3u000000fqYUEAY',
    'Blevins Branch': 'a2E3u000000fqYVEAY',
    'South Fork Laurel Creek': 'a2E3u000000fqYZEAY',
    'North Pierce Branch': 'a2E3u000000fqYyEAI',
    'Flat Branch': 'a2E3u000000fqZ3EAI'
}


