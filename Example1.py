#%%
import pandas as pd
import requests 
from bs4 import BeautifulSoup
#%%
# Assign a target
URL = "https://www.saudiexchange.sa/wps/portal/tadawul/markets/equities/market-watch/market-watch-today/!ut/p/z1/pZHBboJAEIafpQeuzM8CSnvbYAUETUyE4l4MNrhikDWI8vol2h5MFNt0bjP5vkzmHxKUkqiycyGzplBVVnb9UgxWMz9yfTgshM9G4IP3MBy5NoNr08cFYMx1jFcLEaKh0QEegvnUMuEZJP7ke8FsCD7nfjJOFp1v_s-H9TsfD4rjuS_6Eesb6IvoFriTQS-AnxU9V0xIyFKtrx_l1dp0JIk63-R1Xuunuhtvm-ZwfNOgoW1bXSoly1z_VHsN95StOjaU3pJ02MdxnKIIdnZ5jvjLF3fAy9o!/dz/d5/L0lDUmlTUSEhL3dHa0FKRnNBLzROV3FpQSEhL2Vu/"
# get page as html
page = requests.get(URL)

# Print HTML Page code
print(page.text)
#%%
# Assign Page to BS to to extract data
soup = BeautifulSoup(page.content, "html.parser")
#%%
# Find table tags
table = soup.find_all("table",{'id':'table13'})
df = pd.read_html(str(table))[0]

# %%
df
# %%
