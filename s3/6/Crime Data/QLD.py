import pandas as pd
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

def qld():
    qld = pd.read_csv('Queensland_data.csv')
    qld.drop(columns=['Unnamed: 90'], inplace=True)

    for i in range(len(qld)):
        tmp = qld['Month Year'].values[i].split('-')
        qld['Month Year'].values[i] = '20' + tmp[1] + ' ' + date_convert(tmp[0])

    qld = qld.groupby(['District', 'Month Year']).sum()

    qld = qld.stack().unstack(level=1)

    qld.index.names = ['District', 'Subcategory']

    qld = qld.stack().to_frame()

    qld.rename(columns={0:'records'}, inplace=True)

    qld['postcode'] = ''
    qld['state_code'] = 'QLD'
    qld['Category'] = ''

    qld[['postcode', 'state_code', 'Category', 'records']]
    qld = qld.reset_index()

    qld.rename(columns={'Category':'category', 'District':'district', 'Subcategory':'subcategory'}, inplace=True)
    qld['year'] = qld['Month Year'].str.split(' ').str[0]
    qld['quarter'] = qld['Month Year'].str.split(' ').str[1]

    qld.drop(columns=['Month Year'], inplace=True)

    qld.to_excel('finished/QLD.xlsx', index=False)


if __name__ == "__main__":
    qld()
