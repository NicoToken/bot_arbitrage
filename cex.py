import ccxt

import time

from termcolor import colored

# Inisialisasi objek Binance, Indodax, KuCoin, dan Bybit

binance = ccxt.binance({

    'apiKey': 'BINANCE_API_KEY',

    'secret': 'BINANCE_SECRET_KEY',

    'options': {

        'defaultType': 'spot',  # Akun spot untuk Binance

        'createMarketBuyOrderRequiresPrice': False

    }

})

indodax = ccxt.indodax({

    'apiKey': 'INDODAX_API_KEY',

    'secret': 'INDODAX_SECRET_KEY'

})

kucoin = ccxt.kucoin({

    'apiKey': 'KUCOIN_API_KEY',

    'secret': 'KUCOIN_SECRET_KEY'

})

bybit = ccxt.bybit({

    'apiKey': 'BYBIT_API_KEY',

    'secret': 'BYBIT_SECRET_KEY'

})

# Bursa utama untuk deposit pertama

main_exchange = tokocrypto

# Jumlah dana yang akan digunakan untuk arbitrase (misalnya 1000 USDT)

funds = 1000

# Threshold persentase arbitrase untuk melakukan eksekusi (misalnya 2%)

threshold = 2

# Pilih akun demo atau akun real

account_type = input("Pilih akun demo atau akun real (demo/real): ")

# Fungsi untuk mendapatkan pair yang tersedia di semua bursa

def get_common_pairs(exchanges):

    pairs = [exchange.fetch_markets() for exchange in exchanges]

    symbols = [set(pair['symbol'] for pair in exchange) for exchange in pairs]

    common_symbols = set.intersection(*symbols)

    return list(common_symbols)

# Fungsi untuk mendapatkan harga

def get_price(exchange, symbol):

    ticker = exchange.fetch_ticker(symbol)

    return ticker['ask'] if ticker['ask'] else None

# Fungsi untuk mengeksekusi tindakan arbitrase

def execute_arbitrage(pair, min_price, max_price):

    # Hitung jumlah aset yang dapat dibeli berdasarkan dana yang tersedia

    amount = funds / min_price

    # Eksekusi tindakan arbitrase

    # Contoh: Beli di Bursa Utama, Jual di Binance

    main_exchange.create_limit_buy_order(pair, amount, min_price)

    binance.create_limit_sell_order(pair, amount, max_price)

    # Catat atau lakukan tindakan lain yang diperlukan

# Dapatkan semua pair yang tersedia di semua bursa

common_pairs = get_common_pairs([main_exchange, binance, indodax, kucoin, bybit])

# Loop infinit untuk memeriksa peluang arbitrase

while True:

    for pair in common_pairs:

        try:

            # Dapatkan harga dari semua bursa

            main_price = get_price(main_exchange, pair)

            binance_price = get_price(binance, pair)

            indodax_price = get_price(indodax, pair)

            kucoin_price = get_price(kucoin, pair)

            bybit_price = get_price(bybit, pair)

            # Hitung persentase arbitrase

            if main_price and binance_price and indodax_price and kucoin_price and bybit_price:

                min_price = min(binance_price, indodax_price, kucoin_price, bybit_price)

                max_price = max(binance_price, indodax_price, kucoin_price, bybit_price)

                # Hitung persentase arbitrase

                if min_price != 0:

                    percentage_arbitrage = ((max_price - min_price) / min_price) * 100

                else:

                    percentage_arbitrage = 0.0

            else:

                percentage_arbitrage = 0.0

            # Tentukan warna teks berdasarkan persentase arbitrase

            if percentage_arbitrage < 0:

                colored_text = colored(f"{pair}: {percentage_arbitrage:.2f}%", "red")

            else:

                colored_text = colored(f"{pair}: {percentage_arbitrage:.2f}%", "green")

            # Tampilkan hasil screening di terminal

            print(colored_text)

            # Eksekusi tindakan arbitrase jika persentase arbitrase melebihi threshold

            if percentage_arbitrage > threshold:

                print(f"Terjadi peluang arbitrase yang layak untuk dieksekusi pada pair {pair}!")

                # Eksekusi tindakan arbitrase

                execute_arbitrage(pair, min_price, max_price)

                # Catat atau lakukan tindakan lain yang diperlukan setelah eksekusi

        except Exception as e:

            print(f"Terjadi kesalahan: {e}")

    # Waktu tunggu antara setiap iterasi

    time.sleep(5)  # Interval screening 5 detik

