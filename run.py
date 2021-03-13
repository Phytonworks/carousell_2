from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
@app.route('/')

def home():
    return render_template('input.html')

@app.route("/kamera_populer")
def cameras():
    url = requests.get('https://id.carousell.com/categories/photography-6')

    soup = BeautifulSoup(url.text, 'html.parser')
    #print(soup)

    cameras = soup.find('div', attrs={'class': 'D_mT M_bX D_S'})
    titles = cameras.findAll('div', attrs={'class': 'D_pR M_eE D_pO D_mQ'})

    return render_template('input.html', title=titles)












if __name__ =='__main__':
    app.run(debug=True)

