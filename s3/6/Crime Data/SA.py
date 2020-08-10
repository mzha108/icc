import pandas as pd
import numpy as np



def date_transform(datetime):
    if datetime.month < 4:
        date = str(datetime.year) + ' Q1'
    elif datetime.month < 7:
        date = str(datetime.year) + ' Q2'
    elif datetime.month < 10:
        date = str(datetime.year) + ' Q3'
    else:
        date = str(datetime.year) + ' Q4'
    return date


def sa():
    df_pivot = pd.read_excel('South Australia_data.xlsx', sheet_name='2012-2017')

    df_pivot.drop(columns=['Offence Level 1  Description'], inplace=True)

    df_pivot.rename(columns={'Offence Level 2 Description':'Category', 'Offence Level 3 Description':'Subcategory', 'Postcode - Incident':'postcode', 'Suburb - Incident':'suburb'}, inplace=True)

    df_pivot['period'] = ''

    for i in range(len(df_pivot)):
        datetime = df_pivot['Reported Date'][i]
        df_pivot['period'].values[i] = date_transform(datetime)

    df_pivot.drop(columns=['Reported Date'], inplace=True)

    df_pivot.drop(df_pivot[df_pivot['suburb'] == 'ADDRESS UNKNOWN'].index, inplace=True)

    df_pivot['postcode'] = df_pivot['postcode'].apply(str).map(lambda x:x.split('.')[0])


    df_pivot = df_pivot.groupby(['suburb', 'postcode', 'Category', 'Subcategory', 'period']).sum()


    df_pivot['year'] = ''
    df_pivot['quarter'] = ''
    df_pivot['state_code'] = 'SA'

    df_pivot = df_pivot.reset_index()


    for i in range(len(df_pivot)):
        df_pivot['year'].values[i] = df_pivot['period'].values[i].split(' ')[0]
        df_pivot['quarter'].values[i] = df_pivot['period'].values[i].split(' ')[1]

    df_pivot.drop(columns=['period'], inplace=True)

    df_pivot.to_excel('finished/SA.xlsx', index=False)



