
from load import load
from freq import Tables
from bar import Bar
from encoding import Encode
import os
from dotenv import load_dotenv
load_dotenv()

df=os.getenv('Data')
col=os.getenv('col_name')
data=load(df).read_data()
keys,values,tbl=Tables(data,col).tables()
Bar(keys,values).bar_chart()
label=Encode(data).label_encode()


print(data.head())
print(tbl)
print(label.head())