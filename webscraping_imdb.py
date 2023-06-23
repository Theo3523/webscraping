from bs4 import BeautifulSoup
import requests
import openpyxl
exel=openpyxl.Workbook()
sheet=exel.active
sheet.title=' top movies'
sheet.append(['rank','name','release','rating'])

url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

try:
    result = requests.get(url)
    result.raise_for_status()
    doc = BeautifulSoup(result.text, 'html.parser')
except Exception as e:
    print(e)

movies=doc.find('tbody',class_='lister-list').find_all('tr')
for i in movies:
    names = i.find('td', class_='titleColumn').find('a').text
    rank = i.find('td', class_='titleColumn').get_text(strip=True).split('.')[0]
    year= i.find('td', class_='titleColumn').find('span').text.strip('()')
    rating= i.find('td', class_='ratingColumn imdbRating').find('strong').text
    sheet.append([names,rank ,year,rating])

exel.save('imdb_rating.xlsx')