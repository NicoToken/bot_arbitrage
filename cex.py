import ccxt

import time

from termcolor import colored

# Inisialisasi objek Binance, Indodax, Tokocrypto, KuCoin, dan Bybit

binance = ccxt.binance()

indodax = ccxt.indodax()

tokocrypto = ccxt.tokocrypto()

kucoin = ccxt.kucoin()

bybit = ccxt.bybit()

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

                max_price = max(binance_price, indodax_price, tokocrypto_price, kucoin_price, bybit_price)

                percentage_arbitrage = ((max_price - min_price) / min_price) * 100

            else:

                percentage_arbitrage = 0.0

            # Tentukan warna teks berdasarkan persentase arbitrase

            if percentage_arbitrage < 0:

                colored_text = colored(f"{pair}: {percentage_arbitrage:.2f}%", "red")

            else:

                colored_text = colored(f"{pair}: {percentage_arbitrage:.2f}%", "green")

            # Tampilkan informasi penjual dan pembeli (CEX)

            cex_info = ""

            if binance_price and indodax_price:

                if binance_price > indodax_price:

                    cex_info = colored("Binance beli - jual Indodax", "green")

                else:

                    cex_info = colored("Indodax beli - jual Binance", "red")

            # Tampilkan hasil screning di terminal

            print(f"{colored_text}  {cex_info}")

        except Exception as e:

            print(f"Terjadi kesalahan: {e}")

    # Waktu tunggu antara setiap iterasi

    time.sleep(5)  # Interval screning 5 detik

