import requests
from bs4 import BeautifulSoup


def ekstraksi_data():
    """
    Tanggal: 29 Maret 2022,
    Waktu: 05:56:49 WIB
    Magnitudo: 3.7
    Kedalaman: 1 km
    Lokasi: LS=3.85  - BT=122.83
Pusat Gempa: Pusat gempa berada di laut 20 km Timur Laut Soropia, Kab. Konawe
Dirasakan: Dirasakan (Skala MMI): II - III Kendari, II - III Konawe
    :return:
    """

    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        result = soup.find('span', {'class': 'waktu'})
        result = result.text.split(', ')
        tanggal = result[0]
        waktu = result[1]

        hasil = dict()
        hasil['tanggal'] = tanggal  # '29 Maret 2022'
        hasil['waktu'] = waktu  # '05:56:49 WIB'
        hasil['magnitudo'] = 3.7
        hasil['lokasi'] = {'ls': 3.85, 'bt': 122.83}
        hasil['pusat gempa'] = 'Pusat gempa berada di laut 20 km Timur Laut Soropia, Kab. Konawe'
        hasil['dirasakan'] = 'Dirasakan (Skala MMI): II - III Kendari, II - III Konawe'
        return hasil
    else:
        return None


def tampilkan_data(result):
    if result is None:
        print("tidak bisa menampilkan data terkini")
        return
    print('Gempa Terakhir Berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Lokasi LS ={result['lokasi']['ls']}, BT = {result['lokasi']['bt']}")
    print(f"Pusat gempa {result['pusat gempa']}")
    print(f"Dirasakan {result['dirasakan']}")


# if __name__ == '__main__':
   # print('ini adalah package gempa terkini')
   # print('hai')
