import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
r = requests.get(url)
data = r.content
soap = BeautifulSoup(data, 'html.parser')

name_lst = []
clean_name_lst = []
rate_lst = []
year_lst = []

anchors = soap.select('a')
x = anchors[56:555]
for i in x:
    name_lst.append(i.text.strip())
    clean_name_lst = list(filter("".__ne__,name_lst))

strong = soap.find_all("strong")
for i in strong:
    rate_lst.append(i.get_text())

span = soap.find_all("span",class_="secondaryInfo")
for i in span:
    year_lst.append(i.get_text()[1:5])



dict = {"Name": clean_name_lst,
        "Rating": rate_lst,
        "Year": year_lst
        }

df = pd.DataFrame(dict)
# print(df.head(10))
df.to_csv("imdb_data.csv",index=False)