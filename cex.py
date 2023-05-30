import ccxt

import time

from termcolor import colored

# Inisialisasi objek Binance dan Indodax

binance = ccxt.binance()

indodax = ccxt.indodax()

# Fungsi untuk mendapatkan harga

def get_price(exchange, symbol):

    ticker = exchange.fetch_ticker(symbol)

    return ticker['ask'] if ticker['ask'] else None

# Simpan semua pasangan yang ingin Anda arbitrase

pairs = ['BTC/USDT', 'ETH/USDT', 'BTC/USDT', 'ETH/USDT']

# Loop infinit untuk memeriksa peluang arbitrase

while True:

    for pair in pairs:

        try:

            # Dapatkan harga dari Binance dan Indodax

            binance_price = get_price(binance, pair)

            indodax_price = get_price(indodax, pair)

            # Hitung persentase arbitrase

            if binance_price and indodax_price:

                percentage_arbitrage = ((binance_price - indodax_price) / indodax_price) * 100

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

    time.sleep(5)  # Interval screning 5 detik

