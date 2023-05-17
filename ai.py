import ccxt

import time

# Inisialisasi exchange Binance

exchange = ccxt.binance()

# Meminta input dari pengguna untuk API Key dan Secret Key

api_key = input("Masukkan API Key Anda: ")

api_secret = input("Masukkan Secret Key Anda: ")

# Mengatur API Key dan Secret Key pada exchange Binance

exchange.apiKey = api_key

exchange.secret = api_secret

# Fungsi untuk mendapatkan harga aset di pasar future

def get_future_price(symbol):

    future_ticker = exchange.fetch_ticker(symbol)

    return float(future_ticker['bid'])

# Fungsi untuk mendapatkan harga aset di pasar spot

def get_spot_price(symbol):

    spot_ticker = exchange.fetch_ticker(symbol)

    return float(spot_ticker['bid'])

# Fungsi untuk menghitung persentase keuntungan/kerugian

def calculate_profit_loss(initial_value, final_value):

    return ((final_value - initial_value) / initial_value) * 100

# Fungsi untuk mencari peluang arbitrase triangular

def find_triangular_arbitrage_opportunities():

    # Implementasikan logika pencarian peluang arbitrase triangular di sini

    # Mengembalikan daftar peluang arbitrase yang ditemukan

    opportunities = []

    # ...

    return opportunities

# Fungsi untuk mengeksekusi order arbitrase triangular

def execute_triangular_arbitrage(opportunity, initial_funds):

    # Implementasikan logika eksekusi order arbitrase triangular di sini

    # ...

    pass

# Fungsi utama untuk menjalankan strategi arbitrase triangular

def run_triangular_arbitrage(target_profit, initial_funds, stop_profit_percentage):

    while True:

        # Melakukan screening peluang arbitrase triangular

        opportunities = find_triangular_arbitrage_opportunities()

        # Jika ditemukan peluang arbitrase

        if opportunities:

            best_opportunity = max(opportunities, key=lambda x: x['profit_percentage'])

            best_profit = best_opportunity['profit_percentage']

            # Jika profit melebihi persentase yang diinginkan, stop eksekusi

            if best_profit >= target_profit:

                print(f"Profit mencapai target ({best_profit}%). Berhenti eksekusi.")

                break

            # Eksekusi order arbitrase

            execute_triangular_arbitrage(best_opportunity, initial_funds)

        

        # Tunggu beberapa waktu sebelum melakukan pengecekan kembali

        time.sleep(1)

# Meminta input dari pengguna untuk target keuntungan, dana awal, dan persentase profit untuk berhenti

target_profit = float(input("Masukkan target keuntungan (%): "))

initial_funds = float(input("Masukkan jumlah dana awal: "))

stop_profit_percentage = float(input("Masukkan persentase profit untuk berhenti: "))

# Menjalankan strategi arbitrase triangular

run_triangular_arbitrage(target_profit, initial_funds, stop_profit_percentage)

