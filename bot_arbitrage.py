import ccxt

import time

import statistics
# Inisialisasi exchange Binance

exchange = ccxt.binance()
# Fungsi untuk mendapatkan harga aset di pasar future
def calculate_threshold(price_history):

    mean_price = statistics.mean(price_history)

    std_dev = statistics.stdev(price_history)

    if mean_price == 0:

        print("Mean price is zero. Cannot calculate threshold.")

        return None

    threshold = (std_dev / mean_price) * 100

    return threshold

# ...

def run_arbitrage(symbol, quantity, target_profit):

    price_history = []

    while True:

        future_price = get_future_price(symbol)

        spot_price = get_spot_price(symbol)

        price_diff = future_price - spot_price

        price_history.append(spot_price)

        if len(price_history) > 10:

            price_history.pop(0)

        print("===================================")

        print("Waktu:", time.ctime())

        print("Harga future:", future_price)

        print("Harga spot:", spot_price)

        print("Selisih harga:", price_diff)

        # Menghitung threshold secara dinamis

        threshold = calculate_threshold(price_history)

        if threshold is None:

            threshold = 10  # Nilai default jika terjadi kesalahan

        print("Threshold:", threshold)

        print("Kuantitas yang akan dieksekusi:", quantity)

        print("===================================")

        # Melakukan pembelian dan penjualan jika terpenuhi kondisi arbitrase

        time.sleep(5)  # Tunggu 5 detik sebelum melakukan pengecekan lagi

# Meminta input dari pengguna untuk API Key dan Secret Key

api_key = input("Masukkan API Key Anda: ")

api_secret = input("Masukkan Secret Key Anda: ")

# Mengatur API Key dan Secret Key pada exchange Binance

exchange.apiKey = api_key

exchange.secret = api_secret

# Meminta input dari pengguna untuk simbol, kuantitas, dan target keuntungan

symbol = input("Masukkan simbol aset (contoh: BTC/USDT): ")

quantity = float(input("Masukkan kuantitas yang akan dieksekusi (contoh: 0.001): "))

target_profit = float(input("Masukkan target keuntungan dalam persen (contoh: 5): "))

# Menjalankan strategi arbitrase

run_arbitrage(symbol, quantity, target_profit)

