import ccxt

import time

# Fungsi untuk mendapatkan harga dari dua pasangan mata uang

def get_price(symbol):

    ticker = exchange.fetch_ticker(symbol)

    return ticker['bid'] if ticker['bid'] else None

# Meminta pengguna memasukkan API key dan secret key

api_key = input("Masukkan API Key Anda: ")

api_secret = input("Masukkan Secret Key Anda: ")

interval = int(input("Masukkan Interval Screening (detik): "))

# Inisialisasi Binance Spot API

exchange = ccxt.binance({

    'apiKey': api_key,

    'secret': api_secret

})

# Mendapatkan daftar pasangan yang tersedia

markets = exchange.load_markets()

while True:

    for symbol in markets:

        # Memeriksa apakah pasangan mata uang valid

        if '/' in symbol:

            base_currency, quote_currency = symbol.split('/')

            # Memeriksa apakah ada tiga simbol yang dibutuhkan untuk arbitrase triangular

            if base_currency + '/' + quote_currency in markets and quote_currency + '/' + base_currency in markets:

                price1 = get_price(base_currency + '/' + quote_currency)

                price2 = get_price(quote_currency + '/' + base_currency)

                price3 = get_price(symbol)

                if price1 and price2 and price3:

                    # Menghitung arbitrase triangular

                    arb_opportunity = (1 / price1) * price3 * price2 - 1

                    if arb_opportunity > 0:

                        percent_profit = arb_opportunity * 100

                        print("Peluang arbitrase triangular ditemukan pada pasangan", symbol)

                        print("Beli", base_currency, "di harga", price1)

                        print("Jual", quote_currency, "di harga", price2)

                        print("Jual", symbol, "di harga", price3)

                        print("Profit estimasi: {:.2f}%".format(percent_profit))

                        print("-" * 40)

    # Menunggu interval yang ditentukan sebelum memeriksa kembali

    time.sleep(interval)

