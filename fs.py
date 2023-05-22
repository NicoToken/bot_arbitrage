import ccxt

import time

# Inisialisasi exchange Binance

exchange = ccxt.binance()

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

# Fungsi utama untuk menjalankan strategi arbitrase

def run_arbitrage(spot_symbol, future_symbol, threshold, quantity, target_profit):

    while True:

        future_price = get_future_price(future_symbol)

        spot_price = get_spot_price(spot_symbol)

        price_diff_percentage = ((future_price - spot_price) / spot_price) * 100

        print("===================================")

        print("Waktu:", time.ctime())

        print("Harga future:", future_price)

        print("Harga spot:", spot_price)

        print("Selisih persentase:", price_diff_percentage)

        print("Threshold:", threshold)

        print("Kuantitas yang akan dieksekusi:", quantity)

        print("===================================")

        if price_diff_percentage >= threshold:

            # Logika pembelian dan penjualan

            # Implementasikan strategi Anda di sini

            # Misalnya, melakukan pembelian di pasar spot dan menjual di pasar future

            # Membeli aset di pasar spot

            buy_order = exchange.create_market_buy_order(symbol=spot_symbol, quantity=quantity)

            print("Order pembelian di pasar spot:", buy_order)

            buy_price = float(buy_order['fills'][0]['price'])

            # Menjual aset di pasar future

            sell_order = exchange.create_market_sell_order(symbol=future_symbol, quantity=quantity)

            print("Order penjualan di pasar future:", sell_order)

            sell_price = float(sell_order['fills'][0]['price'])

            profit_loss_percentage = calculate_profit_loss(buy_price, sell_price)

            print("Peluang arbitrase terdeteksi!")

            print("Harga future:", future_price)

            print("Harga spot:", spot_price)

            print("Selisih persentase:", price_diff_percentage)

            print("Keuntungan/Kerugian (%):", profit_loss_percentage)

            if profit_loss_percentage >= target_profit:

                print("Target keuntungan tercapai! Menutup order.")

                # Menutup order beli di pasar spot

                close_buy_order = exchange.create_market_sell_order(symbol=spot_symbol, quantity=quantity)

                print("Order penjualan di pasar spot:", close_buy_order)

                # Menutup order jual di pasar future

                close_sell_order = exchange.create_market_buy_order(symbol=future_symbol, quantity=quantity)

                print("Order pembelian di pasar future:", close_sell_order)

                break

        time.sleep(5)  # Tunggu 5 detik sebelum melakukan pengecekan lagi

# Meminta input dari pengguna untuk API Key dan Secret Key

api_key = input("Masukkan API Key Anda: ")

api_secret = input("Masukkan Secret Key Anda: ")

# Mengatur API Key dan Secret Key pada exchange Binance

exchange.apiKey = api_key

exchange.secret = api_secret

# Meminta input dari pengguna untuk simbol aset, threshold, kuantitas, dan target keuntungan

spot_symbol = input("Masukkan simbol aset pasar spot (misalnya BTC/USDT): ")

future_symbol = input("Masukkan simbol aset pasar future (misalnya BTC-USD-20230520): ")

threshold = float(input("Masukkan threshold arbitrase: "))

quantity = float(input("Masukkan kuantitas yang akan dieksekusi: "))

target_profit = float(input("Masukkan target keuntungan (%): "))

# Menjalankan strategi arbitrase

run_arbitrage(spot_symbol, future_symbol, threshold, quantity, target_profit)

