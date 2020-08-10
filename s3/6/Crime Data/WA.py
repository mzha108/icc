
import pandas as pd

def convert_date(date):
    tmp = date.split('-')
    year = tmp[0]
    month = int(tmp[1])
    if month < 4:
        return year + ' Q1'
    elif month < 7:
        return year + ' Q2'
    elif month < 10:
        return year + ' Q3'
    else:
        return year + ' Q4'

def wa_data_reformat(df, current_sheet):
    
    df[('Unnamed: 0_level_0', 'Month and Year')] = df[('Unnamed: 0_level_0', 'Month and Year')].astype(str)

    list = []
    for i in range(len(df)):
        df[('Unnamed: 0_level_0', 'Month and Year')].values[i] = convert_date(df[('Unnamed: 0_level_0', 'Month and Year')][i])
        if i < len(df.columns.values):
            if 'total' in df.columns.values[i][0].lower() or 'total' in df.columns.values[i][1].lower():
                list.append(df.columns.values[i])


    df.drop(columns=list, inplace=True)

    df.set_index([('Unnamed: 0_level_0', 'Month and Year')], inplace=True)
    
    df.index.names = ['Year and Quarter']
    
    df = df.groupby('Year and Quarter').sum()

    

    df = df.stack().stack().to_frame()

    df['state_code'] = 'WA'
    df['postcode'] = ''
    df['suburb'] = ''
    df['district'] = current_sheet

    df.index.names = ['Year and Quarter', 'Subcategory', 'Category']
    df = df.rename(columns={0:'records'}).reset_index()

    df['year'] = df['Year and Quarter'].str.split(' ', 1).str[0]
    df['quarter'] = df['Year and Quarter'].str.split(' ', 1).str[1]

    df.drop(columns=['Year and Quarter'], inplace=True)

    df.to_excel('finished/WA/WA' + current_sheet + '.xlsx', index=False)

def wa():
    excel_file = pd.ExcelFile('Western Australia_data.xlsx')

    for i in range(len(excel_file.sheet_names)):
        current_sheet = excel_file.sheet_names[i]
        df = excel_file.parse(current_sheet, header=[0, 1])
        wa_data_reformat(df, current_sheet)


if __name__ == "__main__":
    excel_file = pd.ExcelFile('Western Australia_data.xlsx')

    for i in range(len(excel_file.sheet_names)):
        current_sheet = excel_file.sheet_names[i]
        print('current_sheet: {} is now started!'.format(current_sheet))
        df = excel_file.parse(current_sheet, header=[0, 1])
        wa_data_reformat(df, current_sheet)
        print('current_sheet: {} is now finished!'.format(current_sheet))

    # current_sheet = excel_file.sheet_names[0]
    # df = excel_file.parse(excel_file.sheet_names[0], header=[0, 1])
    # wa_data_reformat(df, current_sheet)
        

    # wa_data_reformat(df, current_sheet)