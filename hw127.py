from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
page = requests.get(url)

print(page)
headers = ['Proper name', "Distance" , 'Mass' , 'Radius']

soup = BeautifulSoup(page.text , "html.parser")

star_table = soup.find("table")

temp_list = []
table_rows = star_table.fnal_all('tr')

for tr in table_rows:
    td = tr.find_all("tr")
    row = [i.text.rstip()for i in td]
    temp_list.append(row)

star_names = []
distance = []
mass = []
radius = []
lum = []

for i in range(1,len(temp_list)):
    star_names.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])
    lum.append(temp_list[i][7])

df2 = pd.DataFrame(list(zip(star_names,distance,mass,radius,lum)),columns= [ 'Star_name' , "Distance" , 'Mass' , 'Radius' , 'Luminosity'])
print(df2)

df2.to_csv('bright_stars.csv')