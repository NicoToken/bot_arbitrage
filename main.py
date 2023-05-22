import ccxt

import time

# Fungsi untuk mendapatkan harga dari dua pasangan mata uang

def get_price(symbol):

    ticker = exchange.fetch_ticker(symbol)

    return ticker['bid'] if ticker['bid'] else None

# Meminta pengguna memasukkan API key, secret key, dan symbol

api_key = input("Masukkan API Key Anda: ")

api_secret = input("Masukkan Secret Key Anda: ")

symbol1 = input("Masukkan Symbol 1 (contoh: BTC/USDT): ")

symbol2 = input("Masukkan Symbol 2 (contoh: ETH/USDT): ")

symbol3 = input("Masukkan Symbol 3 (contoh: BTC/ETH): ")

interval = int(input("Masukkan Interval Screening (detik): "))

# Inisialisasi Binance Spot API

exchange = ccxt.binance({

    'apiKey': api_key,

    'secret': api_secret

})

while True:

    # Mendapatkan harga untuk masing-masing pasangan mata uang

    price1 = get_price(symbol1)

    price2 = get_price(symbol2)

    price3 = get_price(symbol3)

    if price1 and price2 and price3:

        # Menghitung arbitrase triangular

        arb_opportunity = (1 / price1) * price3 * price2 - 1

        if arb_opportunity > 0:

            percent_profit = arb_opportunity * 100

            print("Peluang arbitrase triangular ditemukan!")

            print("Beli", symbol1, "di harga", price1)

            print("Jual", symbol2, "di harga", price2)

            print("Jual", symbol3, "di harga", price3)

            print("Profit estimasi: {:.2f}%".format(percent_profit))

    # Menunggu interval yang ditentukan sebelum memeriksa kembali

    time.sleep(interval)

