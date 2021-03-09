from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
@app.route('/')

def home():
    return render_template('input.html')

@app.route('/kamera-populer')
def kamera_populer():
    url = 'https://id.carousell.com/categories/photography-6'

    r = requests.get(url)
    # print(r.text)

    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    #print(soup)

    cameras = soup.find('div', attrs={'class': 'D_eJ M_um D_S'})
    titles = soup.findAll('div', attrs={'class': 'D_iJ M_wN D_iG D_eG'})

    return render_template('input.html', title=titles)












if __name__ =='__main__':
    app.run(debug=True)

