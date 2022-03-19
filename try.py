
from bs4 import BeautifulSoup
import lxml
import requests
import pandas as pd

cities = ['pathankot', 'patiala', 'amritsar', 'chandigarh', 'ludhiana', 'dehradun', 'delhi', 'gurgaon', 'noida', 'noida-1',
'agra', 'Allahabad', 'kanpur', 'lucknow', 'bareilly', 'rampur', 'varanasi', 'aligarh', 'jaipur', 'ajmer', 'jodhpur', 'udaipur', 
'jabalpur', 'indore', 'bhopal', 'gwalior', 'patna', 'kolkata', 'ahmedabad', 'rajkot', 'surat', 'baroda', 'vapi', 'bhuj', 
'mumbai', 'pune', 'nashik', 'Aurangabad', 'vizag', 'hyderabad', 'bangalore', 'kochi', 'kozhikode', 'chennai', 'vadodara', 'pondicherry',
'port-blair', 'darjeeling', 'daman', 'diu']

city = []
Name = []
Cuisine = []
Rating = []
cf2 = []
swiggy_offer = []
link = []
restaurant_code = []

def rest():
    for i in l:
        Rating.append(i.text.split('•')[0][-3:])
        cf2.append(i.text.split('TWO')[0].split('₹')[1] + 'TWO')
        swiggy_offer.append(i.text.split('TWO')[1].split('Quick')[0])
        link.append('www.swiggy.com'+i.a['href'])
        city.append(i.a['href'].split('-')[-2])
        restaurant_code.append(i.a['href'].split('-')[-1])

    for i in soup_1.find_all('div', class_='nA6kb'):
        Name.append(i.text)

    for i in soup_1.find_all('div', class_='_1gURR'):
        Cuisine.append(i.text)



for i in cities:
    for j in range(1,110):
        url_1 = f'https://www.swiggy.com/{i}?page={j}'
        html_1 = requests.get(url_1)

        soup_1 = BeautifulSoup(html_1.text , 'html.parser')

        l = soup_1.find_all('div', class_='_3XX_A')
        rest()
        

data = []
for i in range(len(Name)):
    my_data = {
        'City' : city[i],
        'Name' : Name[i],
        'Cuisine' : Cuisine[i],
        'Rating' : Rating[i],
        'Cost for 2' : cf2[i],
        'Swiggy Offers' : swiggy_offer[i],
        'Url' : link[i],
        'Restaurant code' : restaurant_code[i]
    }
    data.append(my_data)
df = pd.DataFrame(data)
df.to_excel('Rest.xlsx', index=False, encoding='UTF-8')
print('01')