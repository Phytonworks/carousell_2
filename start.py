import bs4
import requests

url = 'https://id.carousell.com/categories/photography-6'

r = requests.get(url)
#print(r.text)

soup = bs4.BeautifulSoup(r.text, 'html.parser')
#print(soup)

cameras = soup.find('div', attrs={'class':'D_eJ M_um D_S'})
#print(cameras)

titles = soup.findAll('div', attrs={'class':'D_iJ M_wN D_iG D_eG'})

for title in titles:
    #print(title.text)
    print(title.find('p', attrs={'class':'D_be M_bF D_bn M_bO D_bq M_bR D_bt M_bU D_bv M_bW D_by M_bZ D_bA M_cc D_ba'}).text)

    #gambar
    print(title.find('div', attrs={'class':'D_iV'}).find('img')['src'])

    #harga
    print(title.find('p', attrs={
        'class': 'D_be M_bF D_bn M_bO D_bq M_bR D_bt M_bU D_bv M_bW D_by M_bZ D_b_ M_cb D_aZ'}).text)


