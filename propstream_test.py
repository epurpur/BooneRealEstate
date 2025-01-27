
import pandas as pd
from geopy.geocoders import Nominatim

propstream_df = pd.read_excel("Property Export Echota+on+the+Ridge (PropStream).xlsx")
salesforce_df = pd.read_csv("EchotaontheRidgeextract(fromSALESFORCE).csv")


#make unique column in propstream data
#combo of APN + FIPS column.
# also removes '-' from APN
propstream_df['unique_id'] = propstream_df['APN'].astype(str).str.replace("-", "", regex=True) + "|" + propstream_df['FIPS'].astype(str)

#example of propstream unique ID: 1839-00-98-9299-00000_37011


#Unique field in salesforce data already exists: 'VZ__APN_FIPS__C'
#example of salesforce unique ID: '00100200|47091'


#join fields from salesforce data to propstream
# Merge the dataframes on 'unique_id' and 'VZ__APN_FIPS__C'
merged_df = propstream_df.merge(
    salesforce_df[['VZ__APN_FIPS__C', 
                   'ID', 
                   'VZ__BOUNDARY_WKT__C', 
                   'VZ__GEOLOCATION_MEASURED__LATITUDE__S', 
                   'VZ__GEOLOCATION_MEASURED__LONGITUDE__S', 
                   'VZ__GEOLOCATION__LATITUDE__S', 
                   'VZ__GEOLOCATION__LONGITUDE__S']],
    left_on='unique_id',
    right_on='VZ__APN_FIPS__C',
    how='left'
)


#####
# Of the 233 rows in propstream data, 184 have a match in the Salesforce data based on the APN+FIPS unique ID
# 49 do not have a match. Why? I don't know


# Check to see if there is spatial data in the merged_df
# Assuming merged_df is your dataframe
columns_to_check = [
    'VZ__BOUNDARY_WKT__C', 
    'VZ__GEOLOCATION_MEASURED__LATITUDE__S', 
    'VZ__GEOLOCATION_MEASURED__LONGITUDE__S', 
    'VZ__GEOLOCATION__LATITUDE__S', 
    'VZ__GEOLOCATION__LONGITUDE__S'
]

# Create the 'has_spatial_info' column
merged_df['has_spatial_info'] = merged_df[columns_to_check].notna().any(axis=1)

# If you want the column to explicitly contain TRUE or FALSE as strings:
merged_df['has_spatial_info'] = merged_df['has_spatial_info'].map({True: 'TRUE', False: 'FALSE'})



#attempt to geocode
# Create a geolocator object
geolocator = Nominatim(user_agent="geoapi", timeout=10)

# Address to geocode
# address = "267 Morgans Ridge Dr, Banner Elk, NC 28604"
#address = "114, Ridge Point Drive, Heath, Rockwall County, Texas, 75126, United States  #this works!
address = "114, Ridge Point Drive, Boone, Watauga County, North Carolina, 28607"

# Geocode the address
location = geolocator.geocode(address)

# Check if the geocoding was successful
if location:
    print(f"Address: {location.address}")
    print(f"Latitude: {location.latitude}")
    print(f"Longitude: {location.longitude}")
else:
    print("Geocoding failed: Unable to find the location.")


"""
Workflow

There will be two scenarios with the data:
    1. The propstream parcel will match with a salesforce parcel based on the unique column which is APN+FIPS number
            -I expect this to be the vast majority of the parcels
        -I have merged the salesforce ID for each property so that is what will be used to update the fields in salesforce
        -We will match the fields in the propstreamdata to the salesforce fields when uploading in dataloader
    2. There will be some new parcels that do not match. 
        -for those, they will have an address field
            -however those records will not have a point, line, polygon on the map
        -Can I georeference these points?
            -they need a value in the 'GEOMETRY' field
        -will also have to create the custom boone real estate fields for use in salesforce

            -files to do that include (from github):
                BRE_2024.py
                BRE_2024_Lookup
                BRE_Data_map (maybe)
"""
