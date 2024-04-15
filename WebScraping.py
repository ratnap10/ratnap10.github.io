import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

link = 'https://republika.co.id/'
req = requests.get(link)
ini = BeautifulSoup(req.text, 'html.parser')

# Simpan data
berita = []

# Mengambil waktu
ambil = datetime.now().strftime('%d %B %Y %H:%M:%S')

# Menemukan elemen
repu = ini.find_all('div', 'caption')

for idx, i in enumerate(repu, start=1):
    ktgr = i.find('span', 'kanal-info').text if i.find('span', 'kanal-info') else ""
    jdl = i.find('div', 'title').text if i.find('div', 'title') else ""
    tgl_pub = i.find('div', 'date').text if i.find('div', 'date') else ""

    # Memeriksa apakah elemen ditemukan atau tidak
    if jdl:
        pub_clean = tgl_pub.split(', ')[-1]
        print("Nomor: ", idx)
        print("Judul: ", jdl)
        print("Kategori: ", ktgr)
        print("Waktu Publish: ", pub_clean)
        print("Waktu Pengambilan: ", ambil)
        berita.append({
            'no': idx,
            'judul': jdl,
            'kategori': ktgr,
            'waktu_publish': pub_clean,
            'waktu_pengambilan': ambil,
        })

# Menyimpan berita ke dalam file JSON
with open('Repu.json', 'w') as fjson:
     json.dump(berita, fjson, indent=4)
