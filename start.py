import bs4
import requests

url = 'https://id.carousell.com/categories/photography-6'

r = requests.get(url)
#print(r.text)

soup = bs4.BeautifulSoup(r.text, 'html.parser')
#print(soup)

cameras = soup.find('div', attrs={'class':'D_gG M_cf'})
#print(camera)

titles = soup.findAll('div', attrs={'class':'D_kE M_ez D_kx D_gz'})

for title in titles:
    #print(title.text)
    #print(title.find('p', attrs={'class':'D_bN M_bt D_bW M_bB D_bZ M_bF D_cc M_bI D_cf M_bK D_ci M_bN D_cl M_bQ D_bK'}).text)

    #gambar
    #print(title.find('div', attrs={'class':'D_kQ'}).find('img')['src'])

    #harga
    print(title.find('p', attrs={
        'class': 'D_bN M_bt D_bW M_bB D_bZ M_bF D_cc M_bI D_cf M_bK D_ci M_bN D_ck M_bP D_bJ'}).text)


