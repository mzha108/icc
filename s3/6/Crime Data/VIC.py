
import pandas as pd

def vic():
    vic = pd.ExcelFile('Victoria_BySuburb_data.xlsx')

    sheet_name = vic.sheet_names[0]
    vic = vic.parse(sheet_name=sheet_name)

    vic['quarter'] = ''
    vic['district'] = ''
    vic['state_code'] = 'VIC'

    vic.rename(columns={'Year ending December':'year', 'Postcode':'postcode', 'Suburb/Town Name':'suburb', 
                        'Offence Subdivision':'category', 'Offence Subgroup':'subcategory', 'Incidents Recorded':'records'}, inplace=True)

    vic.drop(columns=['Offence Division'], inplace=True)

    vic = vic[['district', 'suburb', 'postcode', 'state_code', 'year', 'quarter', 'category', 'subcategory', 'records']]

    vic['category'] = vic['category'].str.split(' ', 1).str[1]
    vic['subcategory'] = vic['subcategory'].str.split(' ', 1).str[1]

    vic.to_excel('finished/VIC.xlsx', index=False)



