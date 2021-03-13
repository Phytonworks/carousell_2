import bs4
import requests

url = requests.get('https://id.carousell.com/categories/photography-6')

#r = requests.get(url)
#print(r.text)

soup = bs4.BeautifulSoup(url.text, 'html.parser')
#print(soup)

cameras = soup.find('div', attrs={'class':'D_mT M_bX D_S'})
#print(cameras)

titles = cameras.findAll('div', attrs={'class':'D_pR M_eE D_pO D_mQ'})
#print(titles)

for title in titles:
    #print(title.text)
    print(title.find('p', attrs={'class':'D_aZ M_bz D_bj M_bI D_bm M_bL D_bp M_bO D_br M_bQ D_bu M_bT D_bx M_bW D_aA'}).text)

    #gambar
    print(title.find('div', attrs={'class':'D_qe'}).find('img')['src'])

    #harga
    print(title.find('p', attrs={
        'class': 'D_aZ M_bz D_bj M_bI D_bm M_bL D_bp M_bO D_br M_bQ D_bu M_bT D_bw M_bV D_a_'}).text)


