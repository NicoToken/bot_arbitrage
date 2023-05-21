import requests

coin_price_url = "https://api.binance.com/api/v3/ticker/price"

def get_coin_arbitrage(url):

    response = requests.get(url)

    coin_json = response.json()

    return coin_json

def collect_tradeables(coin_json):

    coin_list = []

    for coin in coin_json:

        if coin['symbol'].endswith('USDT'):

            coin_list.append(coin)

    return coin_list
    def get_price_for_t_pair(t_pair, url):

    symbol_a = t_pair['pair_a'] + "USDT"

    symbol_b = t_pair['pair_b'] + "USDT"

    symbol_c = t_pair['pair_c'] + "USDT"

    response = requests.get(url, params={'symbol': symbol_a})

    price_a = float(response.json()['price'])

    response = requests.get(url, params={'symbol': symbol_b})

    price_b = float(response.json()['price'])

    response = requests.get(url, params={'symbol': symbol_c})

    price_c = float(response.json()['price'])

    return price_a, price_b, price_c
  def structure_triangular_pairs(coin_list):

    triangular_pairs_list = []

    for i in range(len(coin_list)):

        for j in range(len(coin_list)):

            for k in range(len(coin_list)):

                if i != j and j != k and i != k:

                    t_pair = {

                        'pair_a': coin_list[i]['symbol'],

                        'pair_b': coin_list[j]['symbol'],

                        'pair_c': coin_list[k]['symbol'],

                        'combined': f"{coin_list[i]['symbol']} - {coin_list[j]['symbol']} - {coin_list[k]['symbol']}"

                    }

                    triangular_pairs_list.append(t_pair)

    return triangular_pairs_list
  def calculate_arbitrage(price_a, price_b, price_c):

    total_investment = 1000  # Jumlah investasi dalam USDT

    fee_percentage = 0.1  # Persentase biaya perdagangan

    profit_percentage = 0.5  # Persentase keuntungan yang diinginkan

    # Hitung jumlah koin yang bisa dibeli dengan total investasi

    volume_a = (total_investment / price_a) * (1 - fee_percentage / 100)

    volume_b = (volume_a / price_b) * (1 - fee_percentage / 100)

    volume_c = (volume_b / price_c) * (1 - fee_percentage / 100)

    # Hitung total nilai akhir

    total_value = volume_c * price_c * (1 - fee_percentage / 100)

    # Hitung potensi keuntungan

    potential_profit = total_value - total_investment

    # Verifikasi apakah potensi arbitrase menguntungkan

    if potential_profit > 0 and (potential_profit / total_investment) >= (profit_percentage / 100):

        return True, potential_profit, total_value

    else:

        return False, 0, 0
      def run_arbitrage(triangular_pairs_list):

    for t_pair in triangular_pairs_list:

        price_a, price_b, price_c = get_price_for_t_pair(t_pair, coin_price,success, potential_profit, total_value = calculate_arbitrage(price_a, price_b, price_c)

    if success:

        print("Potensi Arbitrase yang Menguntungkan Ditemukan!")

        print("Kombinasi: ", t_pair['combined'])

        print("Potensi Keuntungan: ", potential_profit)

        print("Total Nilai Akhir: ", total_value)

        print("-----------------------------------------")
                             if __name__ == '__main__':

    coin_json = get_coin_arbitrage(coin_price_url)

    coin_list = collect_tradeables(coin_json)

    triangular_pairs_list = structure_triangular_pairs(coin_list)

    run_arbitrage(triangular_pairs_list)
             # Menjalankan program secara otomatis

if __name__ == '__main__':

    coin_json = get_coin_arbitrage(coin_price_url)

    coin_list = collect_tradeables(coin_json)

    triangular_pairs_list = structure_triangular_pairs(coin_list)

    run_arbitrage(triangular_pairs_list)

 # Menjalankan program secara otomatis

if __name__ == '__main__':

    coin_json = get_coin_arbitrage(coin_price_url)

    coin_list = collect_tradeables(coin_json)

    triangular_pairs_list = structure_triangular_pairs(coin_list)

    run_arbitrage(triangular_pairs_list)

                                          
