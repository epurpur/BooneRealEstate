
"""
This is the first script in the series of updating the 2021 tax parcel data

Steps:
1. Imports old parcels (previous data from salesforce) and new parcels (new 2021 tax parcel data)

2. Drops Tennessee counties from both old and new data

3. Checks parcel numbers to see which parcels...
        - are new to the 2021 data. (new_parcels)
        - no longer exist in the 2021 data  (old_outdated_parcels)
        - exist in both old and new data   (existing_parcels)

(In Progress)
4. For existing_parcels, tries to compare addresses to old parcels to see if mailing addresses have been updated or not 

5. Merges existing parcels to old_parcels

6. Updates fields in old parcels with columns from new parcels. I did this because old_parcels already contains a Salesforce record ID. With the updated columns, we can just mass update the property object

7. Removes unnecessary fields from old_parcels_update (which will be used to update Salesforce)
"""





import pandas as pd
import numpy

#read in new and old parcels
old_parcels = pd.read_csv("/Users/ep9k/Desktop/old_parcels.csv")
new_parcels = pd.read_csv("/Users/ep9k/Desktop/new_parcels.csv")


#drop Tennessee counties because they will not be updated
old_parcels = old_parcels.loc[old_parcels['COUNTY__C'] != 'Carter']
old_parcels = old_parcels.loc[old_parcels['COUNTY__C'] != 'Johnson']

new_parcels = new_parcels.loc[new_parcels['cntyname'] != 'carter']
new_parcels = new_parcels.loc[new_parcels['cntyname'] != 'johnson']

#see which parcels are new from new parcels to old parcels
new_parcels['new_parcel'] = new_parcels['nparno'].isin(old_parcels['N_PARCEL_NUMBER__C'])   # 'false' in the new_parcel column means this is a new parcel
brand_new_parcels = new_parcels.loc[new_parcels['new_parcel'] == False]

#see which parcels have dissappeared from old parcels to new parcels
old_parcels['no_longer_exists'] = old_parcels['N_PARCEL_NUMBER__C'].isin(new_parcels['nparno'])   # 'false' in the comparison column means this parcel no longer exists
old_outdated_parcels = old_parcels[old_parcels['no_longer_exists'] == False]

#see which parcels exist both in old and new data
existing_parcels = new_parcels.loc[new_parcels['new_parcel'] == True]


# new_parcels are now exported and fixed up in QGIS and also Read_WKT_geometries.py
# old parcels will be deleted?????  Will ask Matt about this



#now to compare existing_parcels to old_parcels
#Matt and Benedek have verified all the existing mailing addresses in Salesforce using some address matching API. I will take the first 10 characters olf the mailadd column of existing_parcels to see if they match with 'PBA__ADDRESS_PB__C' column of old_parcels
existing_parcels['mailaddslice'] = existing_parcels['mailadd'].str[:10]
old_parcels['mailaddslice'] = old_parcels['PBA__ADDRESS_PB__C'].str[:10]

#make all text uppercase
existing_parcels['mailaddslice'] = existing_parcels['mailaddslice'].str.upper()
old_parcels['mailaddslice'] = old_parcels['mailaddslice'].str.upper()

#see if existing parcels mail address slice is in old_parcels mail address slice
existing_parcels['test_add_check'] = existing_parcels['mailaddslice'].isin(old_parcels['mailaddslice'])

# current results. IS THIS CORRECT?
# True     119535
# False    104159




#WORKFLOW TO UPDATE OLD PARCELS WITH NEW INFORMATION FROM EXISTING PARCELS
# 1. Merge existing parcels to old parcels
# all_2019_parcels = all_2019_parcels.merge(matt_parcel_update_excel, how='left', left_on='parno', right_on='parno')
old_parcels_update = old_parcels.merge(existing_parcels, how='left', left_on='N_PARCEL_NUMBER__C', right_on='nparno')


# 2. Copy data from existing parcel fields (which are merged) to already existing fields in old_parcels object
old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['altparno']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['cntyfips']
old_parcels_update['COUNTY__C'] = old_parcels_update['cntyname']
old_parcels_update['ACRES__C'] = old_parcels_update['gisacres']
old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['altparno']
old_parcels_update['IMPROVEMENT_VALUE__C'] = old_parcels_update['improvval']
old_parcels_update['LAND_VALUE__C'] = old_parcels_update['landval']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['legdecfull']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['maddpref']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['maddrno']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['maddstname']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['maddstr']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['maddstsuf']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['maddsttyp']

#HERE we want to do somethinglike if ['test_add_check'] == true, then update mailing address with mailadd
#In this case, if the test_add_check is false, this means the mail address in exisiting parcels was not found in old parcels and should be updated
#however, I don't trust these results!
# old_parcels_update['MAILING_ADDRESS__C'] = old_parcels_update['mailadd']                       #???????????
old_parcels_update.loc[(old_parcels_update['test_add_check'] == False), 'MAILING_ADDRESS__C'] = old_parcels_update['mailadd']  #???????????????????

# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['mapref']
old_parcels_update['MAILING_CITY__C'] = old_parcels_update['mcity']
old_parcels_update['MAILING_STATE__C'] = old_parcels_update['mstate']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['multistruc']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['munit']
old_parcels_update['MAILING_POSTAL_CODE__C'] = old_parcels_update['mzip']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['nparno']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['ownfrst']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['ownlast']
# old_parcels_update['TRIMMED_MAILING_NAME__C'] = old_parcels_update['ownname']                 #???????????
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['ownname2']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['owntype']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['parno']
old_parcels_update['PARCEL_USE_CODE_2__C'] = old_parcels_update['parusecd2']
old_parcels_update['PARCEL_VALUE__C'] = old_parcels_update['parval']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['parvaltype']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['presentval']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['recareano']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['recareatx']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['revdatetx']
old_parcels_update['REVISE_DATE__C'] = old_parcels_update['revisedate']
old_parcels_update['REVISE_YEAR__C'] = old_parcels_update['reviseyear']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['saddno']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['saddpref']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['saddstname']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['saddstr']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['saddstsuf']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['saddsttyp']
# old_parcels_update['SALE_DATE__C'] = old_parcels_update['saledate']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['saledatetx']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['scity']
old_parcels_update['PBA__ADDRESS_PB__C'] = old_parcels_update['siteadd']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['sourceagnt']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['sourcedate']
old_parcels_update['SOURCE_DATE__C'] = old_parcels_update['sourcedatx']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['sourceref']
old_parcels_update['PBA__STATE_PB__C'] = old_parcels_update['sstate']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['stcntyfips']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['stfips']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['stname']
# old_parcels_update['STRUCTURE__C'] = old_parcels_update['struct']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['structyear']
old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['altparno']
# old_parcels_update['SUBDIVISION__C'] = old_parcels_update['subdivisio']                    #?????????????
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['subowntype']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['subsurfown']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['sunit']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['szip']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['transfdate']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['id_0']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['sourceagen']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['owner2']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['gisacre']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['new_parcel']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['mailaddslice_y']
# old_parcels_update['ALTERNATIVE_PARCEL_NUMBER__C'] = old_parcels_update['test_add_check']




#Final Step, remove unneccesary columns
columns_to_drop = ['no_longer_exists','mailaddslice_x','Unnamed: 0','altparno','cntyfips','cntyname','gisacres','gnisid','improvval','landval',
 'legdecfull','maddpref','maddrno','maddstname','maddstr','maddstsuf','maddsttyp','mailadd','mapref','mcity','mstate','multistruc','munit',
 'mzip','nparno','ownfrst','ownlast','ownname','ownname2','owntype','parno','parusecd2','parusecode','parusedesc','parusedsc2','parval','parvaltype','presentval',
 'recareano','recareatx','revdatetx','revisedate','reviseyear','saddno','saddpref','saddstname','saddstr','saddstsuf','saddsttyp','saledate','saledatetx',
 'scity','siteadd','sourceagnt','sourcedate','sourcedatx','sourceref','sstate','stcntyfips','stfips','stname','struct','structno','structyear','subdivisio',
 'subowntype','subsurfown','sunit','szip','transfdate','id_0','sourceagen','owner2','gisacre','new_parcel','mailaddslice_y','test_add_check']

#drop columns
old_parcels_update.drop(columns_to_drop, inplace=True, axis=1)

