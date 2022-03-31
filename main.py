"""
Aplikasi Deteksi Gempa Terkini (Modularisasi Dengan Fungsi)
MODULARISASI DENGAN FUNCTION
"""


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
    hasil = dict()
    hasil['tanggal'] = '29 Maret 2022'
    hasil['waktu'] = '05:56:49 WIB'
    hasil['magnitudo'] = 3.7
    hasil['lokasi'] = {'ls': 3.85, 'bt': 122.83}
    hasil['pusat gempa'] = 'Pusat gempa berada di laut 20 km Timur Laut Soropia, Kab. Konawe'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): II - III Kendari, II - III Konawe'

    return hasil


def tampilkan_data(result):
    print('Gempa Terakhir Berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Lokasi LS ={result['lokasi']['ls']}, BT = {result['lokasi']['bt']}")
    print(f"Pusat gempa {result['pusat gempa']}")
    print(f"Dirasakan {result['dirasakan']}")


if __name__ == '__main__':
    print('aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)
