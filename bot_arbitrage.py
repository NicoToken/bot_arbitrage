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

def run_arbitrage(symbol, threshold, quantity, target_profit):

    while True:

        future_price = get_future_price(symbol)

        spot_price = get_spot_price(symbol)

        price_diff = future_price - spot_price

        

        print("===================================")

        print("Waktu:", time.ctime())

        print("Harga future:", future_price)

        print("Harga spot:", spot_price)

        print("Selisih harga:", price_diff)

        print("Treshold:", threshold)

        print("Kuantitas yang akan dieksekusi:", quantity)

        print("===================================")

        

        if price_diff > threshold:

            # Logika pembelian dan penjualan

            # Implementasikan strategi Anda di sini

            # Misalnya, melakukan pembelian di pasar spot dan menjual di pasar future

            

            # Membeli aset di pasar spot

            buy_order = exchange.create_market_buy_order(symbol=symbol, quantity=quantity)

            print("Order pembelian di pasar spot:", buy_order)

            

            buy_price = float(buy_order['fills'][0]['price'])

            

            # Menjual aset di pasar future

            sell_order = exchange.create_market_sell_order(symbol=symbol, quantity=quantity)

            print("Order penjualan di pasar future:", sell_order)

            

            sell_price = float(sell_order['fills'][0]['price'])

            

            profit_loss_percentage = calculate_profit_loss(buy_price, sell_price)

            

            print("Peluang arbitrase terdeteksi!")

            print("Harga future:", future_price)

            print("Harga spot:", spot_price)

            print("Selisih harga:", price_diff)

            print("Keuntungan/Kerugian (%):", profit_loss_percentage)

            

            if profit_loss_percentage >= target_profit:

                print("Target keuntungan tercapai! Menutup order.")

                # Menutup order beli di pasar spot

                close_buy_order = exchange.create_market_sell_order(symbol=symbol, quantity=quantity)

                print("Order penjualan di pasar spot:", close_buy_order)

                

                # Menutup order jual di pasar future

                close_sell_order = exchange.create_market_buy_order(symbol=symbol, quantity=quantity)

                print("Order pembelian di pasar future:", close_sell_order)

                

                break

        

        time.sleep(5)  # Tunggu 5 detik sebelum melakukan pengecekan lagi

# Meminta input dari pengguna untuk API Key dan Secret Key

api_key = input("Masukkan API Key Anda: ")

api_secret = input("Masukkan Secret Key Anda: ")

# Mengatur API Key dan Secret Key pada exchange Binance

exchange.apiKey = api_key

exchange.secret = api_secret

# Meminta input dari pengguna untuk simbol, treshold, kuantitas, dan target keuntungan

symbol = input("Masukkan simbol aset (contoh: BTC/USDT): ")

threshold = float(input("Masukkan treshold (contoh: 10): "))

quantity = float(input("Masukkan kuantitas yang akan dieksekusi (contoh: 0.001): "))

target_profit = float(input("Masukkan target keuntungan dalam persen (contoh: 5): "))

# Menjalankan strategi arbitrase

run_arbitrage(symbol, threshold, quantity, target_profit)

