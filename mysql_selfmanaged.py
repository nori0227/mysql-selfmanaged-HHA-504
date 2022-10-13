# -*- coding: utf-8 -*-
"""mysql-selfmanaged

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZBjd-D3HgRjxhaB5Np-GxMXOJg10BVoq
"""

import pandas as pd
from sqlalchemy import create_engine

!sudo apt-get install python3-dev default-libmysqlclient-dev
!pip install pymysql

from sqlalchemy import create_engine

MYSQL_HOSTNAME = '34.136.63.186' # you probably don't need to change this
MYSQL_USER = 'dba'
MYSQL_PASSWORD = 'ahi2020'
MYSQL_DATABASE = 'tempdata'

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
connection_string

db1 = create_engine(connection_string)

db1

collected_data = pd.read_csv('/State_Taxes_and_Fees_Collected__Beginning_Fiscal_Year_Ending_March_31__1995.csv')
collected_data

collected_data.to_sql('/Taxes_and_Fees_Collected_Fiscal_Year__1995', con= db1)
