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
Zone1a = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone1/Zone1a.gpkg"
Zone1b = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone1/Zone1b.gpkg"
Zone1c = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone1/Zone1c.gpkg"
Zone1d = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone1/Zone1d.gpkg"
Zone1e = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone1/Zone1e.gpkg"
Zone1f = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone1/Zone1f.gpkg"
Zone1g = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone1/Zone1g.gpkg"
Zone1h = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone1/Zone1h.gpkg"
Zone1i = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone1/Zone1i.gpkg"
Zone1j = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone1/Zone1j.gpkg"
Zone2a = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone2/Zone2a.gpkg"
Zone2b = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone2/Zone2b.gpkg"
Zone2c = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone2/Zone2c.gpkg"
Zone2d = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone2/Zone2d.gpkg"
Zone2e = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone2/Zone2e.gpkg"
Zone2f = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone2/Zone2f.gpkg"
Zone2g = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone2/Zone2g.gpkg"
Zone2h = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone2/Zone2h.gpkg"
Zone2i = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone2/Zone2i.gpkg"
Zone2j = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone2/Zone2j.gpkg"
Zone3a = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone3/Zone3a.gpkg"
Zone3b = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone3/Zone3b.gpkg"
Zone3c = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone3/Zone3c.gpkg"
Zone3d = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone3/Zone3d.gpkg"
Zone3e = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone3/Zone3e.gpkg"
Zone3f = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone3/Zone3f.gpkg"
Zone3g = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone3/Zone3g.gpkg"
Zone4a = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone4/Zone4a.gpkg"
Zone4b = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone4/Zone4b.gpkg"
Zone4c = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone4/Zone4c.gpkg"
Zone4d = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone4/Zone4d.gpkg"
Zone4e = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone4/Zone4e.gpkg"
Zone4f = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone4/Zone4f.gpkg"
Zone4g = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone4/Zone4g.gpkg"
Zone4h = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone4/Zone4h.gpkg"
Zone4i = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone4/Zone4i.gpkg"
Zone5a = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone5/Zone5a.gpkg"
Zone5b = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone5/Zone5b.gpkg"
Zone5c = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone5/Zone5c.gpkg"
Zone5d = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone5/Zone5d.gpkg"
Zone5e = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone5/Zone5e.gpkg"
Zone5f = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone5/Zone5f.gpkg"
Zone5g = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone5/Zone5g.gpkg"
Zone5h = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone5/Zone5h.gpkg"
Zone5i = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone5/Zone5i.gpkg"
Zone5j = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone5/Zone5j.gpkg"
Zone5k = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone5/Zone5k.gpkg"
Zone5l = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone5/Zone5l.gpkg"
Zone5m = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone5/Zone5m.gpkg"
Zone5n = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone5/Zone5n.gpkg"
Zone5o = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone5/Zone5o.gpkg"
Zone6a = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone6/Zone6a.gpkg"
Zone7a = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone7/Zone7a.gpkg"
Zone7b = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone7/Zone7b.gpkg"
Zone7c = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone7/Zone7c.gpkg"
Zone7d = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone7/Zone7d.gpkg"
Zone7e = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone7/Zone7e.gpkg"
Zone7f = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone7/Zone7f.gpkg"
Zone7g = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone7/Zone7g.gpkg"
Zone7h = "/Users/ep9k/Library/CloudStorage/OneDrive-UniversityofVirginia/BRE/BRE_GIS_Data/Zones/Zone7/Zone7h.gpkg"


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

