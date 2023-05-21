import requests

import datetime

from colorama import Fore, Style

# Fungsi untuk mendapatkan kenaikan harga BTC/USD pada jam tertentu

def get_percentage_change(api_key, api_secret, start_time, end_time):

    url = f"https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1h&startTime={start_time}&endTime={end_time}"

    response = requests.get(url, headers={'X-MBX-APIKEY': api_key})

    data = response.json()

    if len(data) > 1:

        open_price = float(data[0][1])

        close_price = float(data[-1][4])

        percentage_change = ((close_price - open_price) / open_price) * 100

        return percentage_change

    else:

        return None

# Fungsi untuk mengubah waktu menjadi format timestamp Binance

def convert_to_timestamp(date_time):

    return int(date_time.timestamp() * 1000)

# Fungsi utama untuk mencari data kenaikan BTC/USD pada jam tertentu dalam rentang waktu yang ditentukan

def search_percentage_change(api_key, api_secret, start_date, end_date, target_hour):

    current_date = start_date

    end_date = end_date.replace(hour=target_hour, minute=0, second=0, microsecond=0)

    total_percentage_change = 0.0  # Inisialisasi total persentase

    while current_date <= end_date:

        start_time = convert_to_timestamp(current_date)

        end_time = start_time + 3600000  # Satu jam dalam milidetik

        percentage_change = get_percentage_change(api_key, api_secret, start_time, end_time)

        if percentage_change is not None:

            color = Fore.GREEN if percentage_change > 0 else Fore.RED

            print(color + f"Persentase kenaikan BTC/USD pada {current_date.strftime('%Y-%m-%d')} jam {target_hour} adalah {percentage_change:.2f}%" + Style.RESET_ALL)

            total_percentage_change += percentage_change

        else:

            print(f"Tidak ada data untuk {current_date.strftime('%Y-%m-%d')} jam {target_hour}")

        current_date += datetime.timedelta(days=1)

    print("\nTotal Persentase Kenaikan:")

    print(f"{total_percentage_change:.2f}%")

# Mendapatkan input API key dan secret dari pengguna melalui terminal

api_key = input("Masukkan API Key Binance: ")

api_secret = input("Masukkan API Secret Binance: ")

# Mendapatkan input tanggal awal, tanggal akhir, dan jam dari pengguna melalui terminal

start_date_input = input("Masukkan tanggal awal (YYYY-MM-DD): ")

end_date_input = input("Masukkan tanggal akhir (YYYY-MM-DD): ")

target_hour_input = input("Masukkan jam (0-23): ")

# Mengubah input tanggal dan jam menjadi objek datetime

start_date = datetime.datetime.strptime(start_date_input, "%Y-%m-%d")

end_date = datetime.datetime.strptime(end_date_input, "%Y-%m-%d")

target_hour = int(target_hour_input)

# Menjalankan pencarian persentase kenaikan

search_percentage_change(api_key, api_secret, start_date, end_date, target_hour)
