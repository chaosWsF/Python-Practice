import pandas as pd

data_path = './data/'

aqr_ci = pd.read_excel(
    data_path + 'Commodities for the Long Run Updated Monthly Data.xlsx', sheet_name='Data', 
    usecols=list(range(10)), skiprows=10, 
    names=['Date', 'CI_1', 'CI_2', 'CI_3', 'CI_4', 'CI_5', 'CI_6', 'CI_7', 'CI_8', 'CI_9']
)
tmp = pd.to_datetime(aqr_ci.iloc[0:275, 0], format='%Y-%m-%d %H:%M:%S')
tmp1 = pd.to_datetime(aqr_ci.iloc[275:, 0], format='%m/%d/%Y')
aqr_ci.Date = tmp.append(tmp1)
aqr_ci = aqr_ci.groupby(pd.Grouper(key='Date', freq='M'))
aqr_ci = aqr_ci.last()

date_list = set()
variables = []

commodity_indices = pd.read_excel(data_path + 'GSCI_SP_TR.xlsx')
tmp = commodity_indices.Date.to_list()
date_list = date_list.union(tmp)
ci = dict(zip(tmp, commodity_indices.GSCI.to_list()))
variables.append(ci)

oil_prices = pd.read_excel(data_path + 'oil_commodity_futures.xlsx', sheet_name=None)
for oil_price in oil_prices.values():
    tmp = oil_price.date.to_list()
    date_list = date_list.union(tmp)
    cur = dict(zip(tmp, oil_price.close.to_list()))
    variables.append(cur)

date_list = list(date_list)
date_list.sort()
data = []
for date_index in date_list:
    row = [date_index]
    for variable in variables:
        if date_index in variable:
            row.append(variable[date_index])
        else:
            row.append(None)

    data.append(row)

colum_names = ['Date', 'CI_10', 'CI_11', 'CI_12', 'CI_13', 'CI_14', 'CI_15', 'CI_16', 'CI_17']
data = pd.DataFrame(data, columns=colum_names)
data.Date = pd.to_datetime(data.Date, format='%Y%m%d')

monthly_data = data.groupby(pd.Grouper(key='Date', freq='M'))
monthly_data = monthly_data.last()
tmp = monthly_data[1:] / monthly_data[0:-1]
print()