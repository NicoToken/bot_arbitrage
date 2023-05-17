import requests

import time

# Fungsi untuk mendapatkan harga aset di DEX Terra menggunakan API Coingecko

def get_asset_price(asset):

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={asset}&vs_currencies=usd"

    response = requests.get(url)

    data = response.json()

    price = data[asset]["usd"]

    return price

# Fungsi untuk menjalankan strategi arbitrase triangular

def run_triangular_arbitrage(base_asset, quote_asset, target_profit, initial_funds, stop_profit_percentage):

    while True:

        # Mendapatkan harga aset di DEX Terra

        base_price = get_asset_price(base_asset)

        quote_price = get_asset_price(quote_asset)

        # Menghitung harga tukar antara aset dasar dan kutipan

        exchange_rate = base_price / quote_price

        # Menghitung harga arbitrase untuk setiap langkah

        buy_price = exchange_rate

        sell_price = 1 / exchange_rate

        # Menghitung potensi keuntungan

        potential_profit = (sell_price - buy_price) / buy_price * 100

        # Menampilkan informasi harga dan potensi keuntungan

        print("===================================")

        print("Waktu:", time.ctime())

        print(f"Harga {base_asset}: {base_price}")

        print(f"Harga {quote_asset}: {quote_price}")

        print("Exchange Rate:", exchange_rate)

        print("Buy Price:", buy_price)

        print("Sell Price:", sell_price)

        print("Potensi Keuntungan:", potential_profit)

        print("===================================")

        if potential_profit >= target_profit:

            # Memeriksa apakah keuntungan telah mencapai persentase berhenti

            if potential_profit >= stop_profit_percentage:

                print("Target keuntungan tercapai! Berhenti eksekusi.")

                break

            # Menjalankan langkah-langkah arbitrase

            print("Eksekusi arbitrase...")

            print("Langkah 1: Beli", base_asset)

            print("Langkah 2: Jual", quote_asset)

            print("Langkah 3: Beli", quote_asset, "dengan", base_asset)

            # Simulasi eksekusi dengan mengurangi dana awal dan menambahkan keuntungan

            executed_profit = initial_funds * (potential_profit / 100)

            final_funds = initial_funds + executed_profit

            print("Hasil Eksekusi:")

            print("Dana Awal:", initial_funds)

            print("Keuntungan:", executed_profit)

            print("Dana Akhir:", final_funds)

            initial_funds = final_funds  # Mengupdate dana awal dengan dana akhir setelah eksekusi

        time.sleep(5)  # Tunggu 5 detik sebelum melakukan pengecekan lagi

# Meminta input dari pengguna

base_asset = input("Masukkan simbol aset dasar: ")

quote_asset = input("Masukkan simbol aset kutipan: ")

target_profit = float(input("Masukkan target keuntungan (%): "))

initial_funds = float(input("Masukkan jumlah dana awal: "))

stop_profit_percentage = float(input("Masukkan persentase keuntungan untuk berhenti: "))

# Menjalankan strategi arbitrase triangular

run_triangular_arbitrage(base_asset, quote_asset

