import pandas as pd
import datetime
import numpy as np

def date_convert(data):
    if data == 'Jan' or data == 'Feb' or data == 'Mar':
        return 'Q1'
    elif data == 'Apr' or data == 'May' or data == 'Jun':
        return 'Q2'
    elif data == 'Jul' or data == 'Aug' or data == 'Sep':
        return 'Q3'
    else:
        return 'Q4'


def nt():
    file = pd.ExcelFile('ori/Northern Territory_data.xlsx')
    nt = file.parse(sheet_name='2011-2018', header=None)

    for i in range(len(nt.columns)):
        for j in range(len(nt)):
            if type(nt[nt.columns[i]].values[j]) == datetime.datetime:
                if nt[nt.columns[i]].values[j].month < 4:
                    nt[nt.columns[i]].values[j] = str(nt[nt.columns[i]].values[j]).split(' ')[0].split('-', 1)[0] + ' Q1'
                elif nt[nt.columns[i]].values[j].month < 7:
                    nt[nt.columns[i]].values[j] = str(nt[nt.columns[i]].values[j]).split(' ')[0].split('-', 1)[0] + ' Q2'
                elif nt[nt.columns[i]].values[j].month < 10:
                    nt[nt.columns[i]].values[j] = str(nt[nt.columns[i]].values[j]).split(' ')[0].split('-', 1)[0] + ' Q3'
                else:
                    nt[nt.columns[i]].values[j] = str(nt[nt.columns[i]].values[j]).split(' ')[0].split('-', 1)[0] + ' Q4'
            elif type(nt[nt.columns[i]].values[j]) == str:
                if len(nt[nt.columns[i]].values[j]) == 6 and len(nt[nt.columns[i]].values[j].split('-')) == 2:
                    nt[nt.columns[i]].values[j] = '20' + nt[nt.columns[i]].values[j].split('-')[1] + ' ' + date_convert(nt[nt.columns[i]].values[j].split('-')[0])


    column_name_list = list(nt.loc[0,:])
    nt = pd.DataFrame(
        np.row_stack([nt.columns, nt.values]),
        columns=column_name_list
    )

    nt = nt.drop(index=[0, 1]).reset_index().drop(columns=['index'])

    nt.fillna('null', inplace=True)
    nt.drop(nt[nt['Number of offences'] == 'null'].index, inplace=True)
    nt.drop(nt[nt['Number of offences'] == 'null'].index, inplace=True)
    nt.rename(columns={'Number of offences':'subcategory'}, inplace=True)

    nt['category'] = nt['category'].apply(lambda x:x.split(' ', 1)[1])
    nt['subcategory'] = nt['subcategory'].apply(lambda x:x.strip().split(' ', 1)[1] if ',' not in x else x.strip())

    nt.set_index(['district', 'category', 'subcategory'], inplace=True)
    nt = nt.stack().to_frame()
    nt.index.names = ['district', 'category', 'subcategory', 'year and quarter']

    nt = nt.groupby(['district', 'category', 'subcategory', 'year and quarter']).sum()
    nt.rename(columns={0:'records'}, inplace=True)

    nt['suburb'] = ''
    nt['postcode'] = ''
    nt['state_code'] = 'NT'

    nt = nt.reset_index()
    nt['year and quarter']
    nt['year'] = nt['year and quarter'].str.split(' ').str[0]
    nt['quarter'] = nt['year and quarter'].str.split(' ').str[1]

    nt = nt.drop(columns=['year and quarter'])
    nt.to_excel('finished/NT.xlsx', index=False)


