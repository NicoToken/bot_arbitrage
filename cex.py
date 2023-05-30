import ccxt

import time

from termcolor import colored

import requests

# Inisialisasi objek Binance, Indodax, Tokocrypto, KuCoin, dan Bybit

binance = ccxt.binance()

indodax = ccxt.indodax()

tokocrypto = ccxt.tokocrypto()

kucoin = ccxt.kucoin()

bybit = ccxt.bybit()

# Jumlah dana yang akan digunakan untuk arbitrase (misalnya 1000 USDT)

funds = 1000

# Threshold persentase arbitrase untuk melakukan eksekusi (misalnya 2%)

threshold = 2

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

    # Contoh: Beli di Indodax, Jual di Binance

    indodax.create_limit_buy_order(pair, amount, min_price)

    binance.create_limit_sell_order(pair, amount, max_price)

    # Catat atau lakukan tindakan lain yang diperlukan

# Dapatkan semua pair yang tersedia di semua bursa

common_pairs = get_common_pairs([binance, indodax, tokocrypto, kucoin, bybit])

# Loop infinit untuk memeriksa peluang arbitrase

while True:

    for pair in common_pairs:

        try:

            # Dapatkan harga dari semua bursa

            binance_price = get_price(binance, pair)

            indodax_price = get_price(indodax, pair)

            tokocrypto_price = get_price(tokocrypto, pair)

            kucoin_price = get_price(kucoin, pair)

            bybit_price = get_price(bybit, pair)

            # Hitung persentase arbitrase

            if binance_price and indodax_price and tokocrypto_price and kucoin_price and bybit_price:

                min_price = min(indodax_price, tokocrypto_price, kucoin_price, bybit_price)

                max_price = max(binance_price, indodax_price, tokocrypto_price, kucoin, bybit_price)
                         # Hitung persentase arbitrase

            percentage_arbitrage = ((max_price - min_price) / min_price) * 100

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

time.sleep(5)  # Interval screning 5 detik
