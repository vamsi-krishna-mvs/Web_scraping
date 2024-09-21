'''print('55 vamsi')

try:
    print(x)
except:
    print("print(x) is not working")'''


from bs4 import BeautifulSoup
import requests

'''
from openpyxl import Workbook

wb=Workbook()

ws=wb.active
ws.title='Top rated Movies'
ws.append(['Movie Rank','Movie Title','Year of Release','Runtime','MPAA rating','Imdb rating','Viewed by'])

'''


try:
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36','Accept-Language':'en-US, en;q=0.5'}
   
    url='https://www.imdb.com/chart/top/'

    source=requests.get(url,headers=header)
    #print(source.status_code)
    soup=BeautifulSoup(source.text,'html.parser')#source.content
    
    movies=soup.find_all('li',class_='ipc-metadata-list-summary-item sc-10233bc-0 TwzGn cli-parent')

    print(len(movies))

    for x in movies:

        a=x.find('div',class_='sc-b189961a-0 iqHBGn cli-children')
        id_title=a.find('h3',class_='ipc-title__text').text.split('.')
        id,title=id_title

        span=a.find_all('span',class_='sc-b189961a-8 hCbzGp cli-title-metadata-item')
        year=span[0].text.strip()
        duration=span[1].text.strip()
        rated=span[2].text.strip()

        rating=a.find('span',class_='ipc-rating-star--rating').text

        viewers=a.find('span',class_='ipc-rating-star--voteCount').text
        viewers=viewers.strip('(<!-- -->)').split('(')[1]#.split('<')[0]

        print(id,title,year,duration,rated,rating,viewers)
        
        #ws.append([id,title,year,duration,rated,rating,viewers])

        
except:
    print("error occured")

'''
wb.save('IMDB.xlsx')'''