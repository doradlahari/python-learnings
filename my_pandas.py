# pandas -- pip install pandas


# filteration
# analysis of data

import pandas

# data=['ramesh','suresh','mahesh','subhash','vignesh','rajesh']

# info=pandas.DataFrame(data)

# print(info)

# print(type(info))

# dict1={
#     'teams':['csk','rcb','mi','lsg'],
#     'players':['dhoni','kohili','rohit','rahul']
# }

# info=pandas.DataFrame(dict1)

# print(info)

# print(type(info))

#read_csv
# read_excel
#read_json
csv_data= pandas.read_csv('sample_data.csv')

# print(csv_data)

# print(csv_data.loc[0:2]) # row based


# print(csv_data.loc[[0,1,3]])

# print(csv_data['Name'])  # column based

# print(csv_data)

# info = csv_data[csv_data['Location']=='Los Angeles']


print(csv_data)
# info.to_csv('filtered_data.csv',index=False)

csv_data.to_excel('sample.xlsx',index=False)

csv_data.to_json('sample_info.json',index=False,indent=4,orient='records')