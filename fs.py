import ccxt

import time

# Fungsi untuk mendapatkan daftar pasangan mata uang yang tersedia di Binance

def get_available_pairs(exchange):

    markets = exchange.fetch_markets()

    pairs = []

    for market in markets:

        if market['spot']:

            pairs.append(market['symbol'])

    return pairs

# Fungsi untuk menampilkan daftar pasangan mata uang di terminal

def print_pairs(pairs):

    print("Pair yang tersedia:")

    for pair in pairs:

        print(pair)

# Fungsi untuk menampilkan hasil screening pasangan mata uang di terminal

def print_screened_pairs(pairs, threshold):

    print("Pair yang memenuhi threshold:")

    for pair in pairs:

        # Mendapatkan harga spot

        spot_ticker = exchange.fetch_ticker(pair)

        spot_price = spot_ticker['last']

        # Mendapatkan harga future

        future_pair = pair.replace('/', '_')

        future_ticker = exchange.fetch_ticker(f'{pair}_PERP')

        future_price = future_ticker['last']

        # Menghitung selisih persentase antara harga spot dan future

        spread = (future_price - spot_price) / spot_price * 100

        # Menampilkan pasangan mata uang jika selisih persentase melebihi threshold

        if spread > threshold:

            print(f"Pair: {pair}, Spread: {spread}%")

# Mengambil input dari pengguna

api_key = input("Masukkan API Key: ")

secret_key = input("Masukkan Secret Key: ")

threshold = float(input("Masukkan Threshold: "))

interval = int(input("Masukkan Interval (detik): "))

# Membuat objek exchange menggunakan CCXT

exchange = ccxt.binance({

    'apiKey': api_key,

    'secret': secret_key,

    'enableRateLimit': True,

})

# Mendapatkan daftar pasangan mata uang yang tersedia

pairs = get_available_pairs(exchange)

# Menampilkan daftar pasangan mata uang di terminal

print_pairs(pairs)

# Melakukan screening pasangan mata uang dan arbitrase jika memenuhi threshold

while True:

    screened_pairs = []

    for pair in pairs:

        # Mendapatkan harga spot

        spot_ticker = exchange.fetch_ticker(pair)

        spot_price = spot_ticker['last']

        # Mendapatkan harga future

        future_pair = pair.replace('/', '_')

        future_ticker = exchange.fetch_ticker(f'{pair}_PERP')

        future_price = future_ticker['last']

        # Menghitung selisih persentase antara harga spot dan future

        spread = (future_price - spot_price) / spot_price * 100

        # Menambahkan pasangan mata uang ke daftar screened_pairs jika selisih persentase melebihi threshold

        if spread > threshold:

            screened_pairs.append(pair)

        # Menampilkan pasangan mata uang hasil screening di terminal

    print_screened_pairs(screened_pairs, threshold)

    time.sleep(interval)
