import bs4
import requests

url = requests.get('https://id.carousell.com/categories/photography-6')

#r = requests.get(url)
#print(r.text)

soup = bs4.BeautifulSoup(url.text, 'html.parser')
#print(soup)

cameras = soup.find('div', attrs={'class':'D_R'})
#print(cameras)

titles = cameras.findAll('div', attrs={'class':'D_pU'})
#print(titles)

for title in titles:
    #nama toko
    print(title.find('p', attrs={'class': 'D_aZ M_bz D_bk M_bJ D_bm M_bL D_bp M_bO D_br M_bQ D_bu M_bT D_bx M_bW D_aA'}).text)

    #deskripsi barang
    #print(title.find('p', attrs={'class': 'D_aZ M_bz D_bj M_bI D_bm M_bL D_bp M_bO D_br M_bQ D_bu M_bT D_bw M_bV D_aA'}).text)

    #judul
    #print(title.find('p', attrs={'class':'D_aZ M_bz D_bj M_bI D_bm M_bL D_bp M_bO D_br M_bQ D_bu M_bT D_bx M_bW D_aA'}).text)

    #gambar
    #print(title.find('div', attrs={'class':'D_qe'}).find('img')['src'])

    #harga
    #print(title.find('p', attrs={'class': 'D_aZ M_bz D_bj M_bI D_bm M_bL D_bp M_bO D_br M_bQ D_bu M_bT D_bw M_bV D_a_'}).text)


