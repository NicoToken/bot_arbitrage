import datetime

import requests

from colorama import Fore, Style
def get_percentage_change(api_key, api_secret, pair, start_time, end_time):

    url = f"https://api.binance.com/api/v3/klines?symbol={pair}&interval=1h&startTime={start_time}&endTime={end_time}"

    response = requests.get(url, headers={'X-MBX-APIKEY': api_key})

    data = response.json()

    if len(data) > 0:

        open_price = float(data[0][1])

        close_price = float(data[-1][4])

        percentage_change = ((close_price - open_price) / open_price) * 100

        return percentage_change

    else:

        return None

def convert_to_timestamp(date_time):

    return int(date_time.timestamp() * 1000)

def search_percentage_change(api_key, api_secret, pair, start_date, end_date, start_hour, end_hour):

    current_date = start_date

    end_date = end_date.replace(hour=end_hour, minute=59, second=0, microsecond=0)

    total_percentage_change = 0.0  # Inisialisasi total persentase

    while current_date <= end_date:

        start_time = current_date.replace(hour=start_hour, minute=1, second=0, microsecond=0)

        end_time = current_date.replace(hour=end_hour, minute=59, second=0, microsecond=0)

        start_time = convert_to_timestamp(start_time)

        end_time = convert_to_timestamp(end_time)

        percentage_change = get_percentage_change(api_key, api_secret, pair, start_time, end_time)

        if percentage_change is not None:

            color = Fore.GREEN if percentage_change > 0 else Fore.RED

            print(color + f"Persentase kenaikan {pair} pada {current_date.strftime('%Y-%m-%d')} jam {start_hour}:01-{end_hour}:59 adalah {percentage_change:.2f}%" + Style.RESET_ALL)

            total_percentage_change += percentage_change

        else:

            print(f"Tidak ada data untuk {current_date.strftime('%Y-%m-%d')} jam {start_hour}:01-{end_hour}:59")

        current_date += datetime.timedelta(days=1)

    print("\nTotal Persentase Kenaikan:")

    print(f"{total_percentage_change:.2f}%")


    api_key = input("Masukkan API Key Binance: ")

api_secret = input("Masukkan API Secret Binance: ")

pair = input("Masukkan pasangan mata uang (pair): ")

start_date_input = input("Masukkan tanggal awal (YYYY-MM-DD): ")

end_date_input = input("Masukkan tanggal akhir (YYYY-MM-DD): ")

start_hour_input = input("Masukkan jam mulai (0-23): ")

end_hour_input = input("Masukkan jam berakhir (0-23): ")

start_date = datetime.datetime.strptime(start_date_input, "%Y-%m-%d")

end_date = datetime.datetime.strptime(end_date_input, "%Y-%m-%d")

start_hour = int(start_hour_input)

end_hour = int(end_hour_input)

search_percentage_change(api_key
