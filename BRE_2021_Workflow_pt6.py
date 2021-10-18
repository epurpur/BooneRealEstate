
import pandas as pd
import numpy as np


df = pd.read_csv('/Users/ep9k/Desktop/forks_extract.csv')


columns_to_drop = ['ACRES__C','ADDRESS_ERROR__C','ALTERNATIVE_PARCEL_NUMBER__C','CONDO_BUILDING__C','COUNTY__C','CREATEDBYID','CREATEDDATE','CURRENCYISOCODE','CUSTOM_AREA_LOOKUP__C','CUSTOM_AREA__C',
 'DELIVERABILITY__C','DELIVERY_POINT__C','DISTANCE_TO_FEATURE__C','DO_NOT_MAIL__C','EXTERNAL_PROPERTY_ID__C','GEOLOCATION__LATITUDE__S','GEOLOCATION__LONGITUDE__S','GEOLOCATION__C','GEOMETRY_SHAPE__C',
 'IMPROVEMENT_VALUE__C','ISDELETED','LAND_VALUE__C','LASTACTIVITYDATE','LASTMODIFIEDBYID','LASTMODIFIEDDATE','LASTREFERENCEDDATE','LASTVIEWEDDATE','LOB_CONFIDENCE_LEVEL__C','LOB_CONFIDENCE_SCORE__C',
 'MAILING_ADDRESS__C','MAILING_CITY__C','MAILING_GEOLOCATION__LATITUDE__S','MAILING_GEOLOCATION__LONGITUDE__S','MAILING_GEOLOCATION__C','MAILING_NAME_2__C','MAILING_NAME__C','MAILING_POSTAL_CODE__C',
 'MAILING_STATE__C','MULTIPLESHAPES__C','N_PARCEL_NUMBER__C','NEAREST_FEATURE__C','OWNERID','PIN__C',
 'PARCEL_USE_CODE_2__C','PARCEL_USE_CODE__C','PARCEL_USE_DESCRIPTION__C','PARCEL_VALUE__C','PARENT_PROJECT__C','POSTCARD_FRONT_GENERAL_IMAGE__C','PROPERTY_LOCATION_MERGE_VARIABLE__C','PROPERTY_OWNER__C',
 'RECORDTYPEID','REVISE_DATE__C','REVISE_YEAR__C','SALE_DATE__C','SOURCE_DATE__C','SOURCE_REFERENCE__C','SQ_FT_HLA__C','STRUCTURE__C','SUBDIVISION_LOOKUP__C','SUBDIVISION__C','SYSTEMEXTERNALID__C','SYSTEMMODSTAMP',
 'TOWNHOME__C','TRIMMED_MAILING_NAME__C','UNIT__C','VERIFICATION_ID__C','VERIFICATION_RESPONSE_PAYLOAD__C','VERIFIED_AT__C','VERIFIED__C','VERIFY__C',
 'ZONE__C','PBA__ADDRESS_PB__C','PBA__AREA_PB__C','PBA__BEDROOMS_PB__C','PBA__CITY_PB__C','PBA__COMPLETIONDATE_PB__C','PBA__COMPLETIONSTATUS_PB__C','PBA__COUNTRYCODE_PB__C','PBA__COUNTRY_PB__C','PBA__DESCRIPTION_PB__C',
 'PBA__FLOOR__C','PBA__FULLBATHROOMS_PB__C','PBA__GEOCODEACCURACY_PB__C','PBA__HALFBATHROOMS_PB__C','PBA__LATITUDE_PB__C','PBA__LONGITUDE_PB__C','PBA__LOTSIZE_PB__C','PBA__MAIN_WEBSITE_IMAGE__C','PBA__MASTER_PROPERTY__C',
 'PBA__MEASUREMENT_PB__C','PBA__NUMBEROFPARKINGSPACES_PB__C','PBA__POSTALCODE_PB__C','PBA__PROPERTYOWNERCONTACT_PB__C','PBA__PROPERTYTYPE__C','PBA__STATECODE_PB__C','PBA__STATE_PB__C','PBA__STREET_PB__C',
 'PBA__SYSTEMWEBSITEEXTERNALID__C','PBA__TOTALAREA_PB__C','PBA__VIEW_PB__C','PBA__YEARBUILT_PB__C']

df.drop(columns_to_drop, inplace=True, axis=1)


#convert columns to numeric data types
df["NForkNewRiverDist_HubDist"] = pd.to_numeric(df["NForkNewRiverDist_HubDist"])
df["SForkNewRiverDist_HubDist"] = pd.to_numeric(df["SForkNewRiverDist_HubDist"])
df["WatRiverDist_HubDist"] = pd.to_numeric(df["WatRiverDist_HubDist"])


# if parcels < .15mi from river, artificially change that distance to 0
df.loc[df['NForkNewRiverDist_HubDist'] <= .15, 'NForkNewRiverDist_HubDist'] = 0
df.loc[df['SForkNewRiverDist_HubDist'] <= .15, 'SForkNewRiverDist_HubDist'] = 0
df.loc[df['WatRiverDist_HubDist'] <= .15, 'WatRiverDist_HubDist'] = 0


#determine nearest river

#find shortest distance
df['DISTANCE_TO_FEATURE__C'] = df[['NForkNewRiverDist_HubDist', 'SForkNewRiverDist_HubDist', 'WatRiverDist_HubDist']].min(axis=1)

#compare shortest distance to other columns to get nearest feature and label it as such
df.loc[df['NForkNewRiverDist_HubDist'] == df['DISTANCE_TO_FEATURE__C'], 'NEAREST_FEATURE__C'] = 'New River North Fork'
df.loc[df['SForkNewRiverDist_HubDist'] == df['DISTANCE_TO_FEATURE__C'], 'NEAREST_FEATURE__C'] = 'New River South Fork'
df.loc[df['WatRiverDist_HubDist'] == df['DISTANCE_TO_FEATURE__C'], 'NEAREST_FEATURE__C'] = 'Watauga River'
  
#populate NEAREST_FEATURE_LOOKUP field with salesforce IDs of river objects
df.loc[df['NEAREST_FEATURE__C'] == 'New River North Fork', 'NEAREST_FEATURE_LOOKUP__C'] = 'a2E3u000000fPsfEAE'
df.loc[df['NEAREST_FEATURE__C'] == 'New River South Fork', 'NEAREST_FEATURE_LOOKUP__C'] = 'a2E3u000000fPskEAE'
df.loc[df['NEAREST_FEATURE__C'] == 'Watauga River', 'NEAREST_FEATURE_LOOKUP__C'] = 'a2E3u000000fPmwEAE'


#export results
# df.to_csv('/Users/ep9k/Desktop/rivers_update.csv')