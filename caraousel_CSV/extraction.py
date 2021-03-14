import bs4
import requests
import csv

url = requests.get('https://id.carousell.com/categories/health-and-beauty-11/makeup-309')

#r = requests.get(url)
#print(r.text)

soup = bs4.BeautifulSoup(url.text, 'html.parser')
#print(soup)

make_up = soup.find('div', attrs={'class':'D_mX'})
#print(cameras)

titles = make_up.findAll('div', attrs={'class':'D_mT D_S'})
#print(titles)

file = open('hasil_scrap.csv', 'w', newline'')
writer = csv.writer(file)
headers = ['Nama Toko', 'Nama Produk', 'Harga']
writer.writerow(headers)


for title in titles:
    #nama toko
    toko = (title.find('p', attrs={
        'class': 'D_aZ M_bz D_bk M_bJ D_bm M_bL D_bp M_bO D_br M_bQ D_bu M_bT D_bx M_bW D_aA'}).text)

    #judul
    nama = (title.find('p', attrs={'class':'D_aZ M_bz D_bj M_bI D_bm M_bL D_bp M_bO D_br M_bQ D_bu M_bT D_bx M_bW D_aA'}).text)

    #harga
    harga (title.find('p', attrs={'class': 'D_aZ M_bz D_bj M_bI D_bm M_bL D_bp M_bO D_br M_bQ D_bu M_bT D_bw M_bV D_a_'}).text)

    file = open('hasil_scrap.csv', 'a', newline'', encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow([toko, nama, harga])
    file.close()

