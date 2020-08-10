import sys
import pandas as pd
import numpy as np

def clean_act_data(year='2017'):
    act = pd.read_excel('ACT_data.xlsx', sheet_name=year, header=[0, 1])

    check_nan(act)

    act.fillna('null', inplace=True)

    tmp_val = 'null'
    for index in range(len(act)):
        if act[('Unnamed: 0_level_0', 'district')].values[index] != 'null':
            tmp_val = act[('Unnamed: 0_level_0', 'district')].values[index]
        else:
            act[('Unnamed: 0_level_0', 'district')].values[index] = tmp_val

    act = act.drop(act[act[('Quarter', 'suburb')] == 'null'].index)
    act.set_index([('Unnamed: 0_level_0', 'district'), ('Quarter', 'suburb')], inplace=True)
    act.index.names = ['district', 'suburb']
    act = act.stack().stack().to_frame()
    act.index.names = ['district', 'suburb', 'category', 'quarter']
    act.rename(columns={0:'records'}, inplace=True)
    act['year'] = year
    act['state_code'] = 'ACT'
    act['postcode'] = ''
    act['subcategory'] = ''
    act = act[['year', 'postcode', 'state_code', 'subcategory', 'records']]
    path = 'finished/ACT/ACT' + str(year) + '.xlsx'
    act = act.reset_index()
    act.to_excel(path, index=False)

def check_nan(act):
    for quarter in range(1, 5):
        df_num = 'Q' + str(quarter)
        count = 0
        for i in range(len(act[df_num].isna().all())):
            if act[df_num].isna().all()[i] == True:
                count = count + 1
        if count == len(act[df_num].isna().all()):
            act.drop(columns=[df_num], inplace=True)
        
def act():
    act_file = pd.ExcelFile('ACT_data.xlsx')
    for i in range(len(act_file.sheet_names)):
        clean_act_data(act_file.sheet_names[i])


if __name__ == "__main__":
    # try:
    #     year = sys.argv[1:]
    #     for i in range(len(year)):
    #         clean_act_data(year[i])
    # except Exception as e:
    #     print(e)
    act()
