"""
Прочитать данные из  csv файла и записать её в базу данных SQL

"""

import pandas as pd
data = pd.read_csv("application_record.csv")
len(data["NAME_INCOME_TYPE"].unique())
ar_ = data["NAME_INCOME_TYPE"].unique()
for item in ar_:
    print (str(item),":",data[data.NAME_INCOME_TYPE == str(item)].shape[0])

from sqlalchemy import create_engine
engine = create_engine('sqlite+pysqlite:///file_path.db', echo=True)

data.loc[:,data.columns != 'index'].drop(data[data.NAME_INCOME_TYPE !='Working'].index).to_sql("Table",con=engine, if_exists='replace')
