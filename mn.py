import time

from termcolor import colored

import ccxt

# Inisialisasi objek Binance dan Indodax

binance = ccxt.binance()

indodax = ccxt.indodax()

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

# Dapatkan semua pair yang tersedia di semua bursa

common_pairs = get_common_pairs([binance, indodax])

# Loop infinit untuk memeriksa peluang arbitrase

while True:

    for pair in common_pairs:

        try:

            # Dapatkan harga dari semua bursa

            binance_price = get_price(binance, pair)

            indodax_price = get_price(indodax, pair)

            # Hitung persentase arbitrase

            if binance_price and indodax_price:

                min_price = min(indodax_price)

                max_price = max(binance_price)

                percentage_arbitrage = ((max_price - min_price) / min_price) * 100

            else:

                percentage_arbitrage = 0.0

            # Tentukan warna teks berdasarkan persentase arbitrase

            if percentage_arbitrage < 0:

                colored_text = colored(f"{pair}: {percentage_arbitrage:.2f}%", "red")

            else:

                colored_text = colored(f"{pair}: {percentage_arbitrage:.2f}%", "green")

            # Tampilkan hasil screning di terminal

            print(colored_text)

        except Exception as e:

            print(f"Terjadi kesalahan: {e}")

    # Waktu tunggu antara setiap iterasi

    time.sleep(1)  # Interval screning 5 detik

