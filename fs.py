import ccxt

import time

exchange = ccxt.binance()

def get_future_price(symbol):

    future_ticker = exchange.fetch_ticker(symbol)

    return float(future_ticker['bid'])

def get_spot_price(symbol):

    spot_ticker = exchange.fetch_ticker(symbol)

    return float(spot_ticker['bid'])

def calculate_profit_loss(initial_value, final_value):

    return ((final_value - initial_value) / initial_value) * 100

def find_future_symbol(spot_symbol):

    markets = exchange.load_markets()

    spot_base = spot_symbol.split('/')[0]

    for symbol in markets:

        if markets[symbol]['future'] and markets[symbol]['active']:

            future_base = symbol.split('/')[0]

            if spot_base == future_base:

                return symbol

    return None

def run_arbitrage(spot_symbol, future_symbol, threshold, quantity, target_profit, interval):

    while True:

        future_price = get_future_price(future_symbol)

        spot_price = get_spot_price(spot_symbol)

        price_diff_percentage = ((future_price - spot_price) / spot_price) * 100

        print("===================================")

        print("Waktu:", time.ctime())

        print("Harga future:", future_price)

        print("Harga spot:", spot_price)

        print("Selisih persentase: {:.2f}%".format(price_diff_percentage))

        print("Threshold: {:.2f}%".format(threshold))

        print("Kuantitas yang akan dieksekusi:", quantity)

        print("===================================")

        if price_diff_percentage >= threshold:

            buy_order = exchange.create_market_buy_order(symbol=spot_symbol, quantity=quantity)

            print("Order pembelian di pasar spot:", buy_order)

            buy_price = float(buy_order['fills'][0]['price'])

            sell_order = exchange.create_market_sell_order(symbol=future_symbol, quantity=quantity)

            print("Order penjualan di pasar future:", sell_order)

            sell_price = float(sell_order['fills'][0]['price'])

            profit_loss_percentage = calculate_profit_loss(buy_price, sell_price)

            print("Peluang arbitrase terdeteksi!")

            print("Harga future:", future_price)

            print("Harga spot:", spot_price)

            print("Selisih persentase: {:.2f}%".format(price_diff_percentage))

            print("Keuntungan/Kerugian (%): {:.2f}%".format(profit_loss_percentage))

            if profit_loss_percentage >= target_profit:

                print("Target keuntungan tercapai! Menutup order.")

                close_buy_order = exchange.create_market_sell_order(symbol=spot_symbol, quantity=quantity)

                print("Order penjualan di pasar spot:", close_buy_order)

                close_sell_order = exchange.create_market_buy_order(symbol=future_symbol, quantity=quantity)

                print("Order pembelian di pasar future:", close_sell_order)

                break

        time.sleep(interval)

api_key = input("Masukkan API Key Anda: ")

api_secret = input("Masukkan Secret Key Anda: ")

exchange.apiKey = api_key

exchange.secret = api_secret

spot_symbol = input("Masukkan simbol aset pasar spot (misalnya BTC/USDT): ")

future_symbol = find_future_symbol(spot_symbol)

if future_symbol is None:

    print("Simbol future tidak ditemukan. Pastikan simbol spot yang Anda masukkan valid.")

else:

    threshold = float(input("Masukkan threshold arbitrase (misalnya 12,23%): ").rstrip('%')) / 100

    quantity = float(input("Masukkan kuantitas yang akan dieksekusi: "))

    target_profit = float(input("Masukkan target keuntungan (%): "))

    interval = int(input("Masukkan interval screening (detik): "))

    run_arbitrage(spot_symbol, future_symbol, threshold, quantity, target_profit, interval)

