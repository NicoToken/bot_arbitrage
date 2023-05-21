import requests

from binance.client import Client

api_key = 'api_key_binance'

api_secret = 'api_secret_binance'

coin_price_url = 'https://api.binance.com/api/v3/ticker/price'

client = Client(api_key, api_secret)

def get_coin_arbitrage(url):

    response = requests.get(url)

    return response.json()

def collect_tradeables(json_obj):

    coin_list = []

    for coin in json_obj:

        coin_list.append(coin['symbol'])

    return coin_list


  def structure_triangular_pairs(coin_list):

    triangular_pairs_list = []

    remove_duplicates_list = []

    pairs_list = coin_list[0:]

    for pair_a in pairs_list:

        pair_a_split = pair_a.split('/')

        a_base = pair_a_split[0]

        a_quote = pair_a_split[1]

        a_pair_box = [a_base, a_quote]

        for pair_b in pairs_list:

            pair_b_split = pair_b.split('/')

            b_base = pair_b_split[0]

            b_quote = pair_b_split[1]

            if pair_b != pair_a:

                if b_base in a_pair_box or b_quote in a_pair_box:

                    for pair_c in pairs_list:

                        pair_c_split = pair_c.split('/')

                        c_base = pair_c_split[0]

                        c_quote = pair_c_split[1]

                        if pair_c != pair_a and pair_c != pair_b:

                            combine_all = [pair_a, pair_b, pair_c]

                            pair_box = [a_base, a_quote, b_base, b_quote, c_base, c_quote]

                            counts_c_base = 0

                            for i in pair_box:

                                if i == c_base:

                                    counts_c_base += 1

                            counts_c_quote = 0

                            for i in pair_box:

                                if i == c_quote:

                                    counts_c_quote += 1

                            if counts_c_base == 2 and counts_c_quote == 2 and c_base != c_quote:

                                combined = pair_a + ',' + pair_b + ',' + pair_c

                                unique_item = ''.join(sorted(combine_all))

                                if unique_item not in remove_duplicates_list:

                                    match_dict = {

                                        "a_base": a_base,

                                        "b_base": b_base,

                                        "c_base": c_base,

                                        "a_quote": a_quote,

                                        "b_quote": b_quote,

                                        "c_quote": c_quote,

                                        "pair_a": pair_a,

                                        "pair_b": pair_b,

                                        "pair_c": pair_c,

                                        "combined": combined

                                    }

                                    triangular_pairs_list.append(match_dict)

                                    remove_duplicates_list.append(unique_item)

    return triangular_pairs_list
  
 def get_price_for_t_pair(t_pair, prices_json):

    pair_a = t_pair['pair_a']

    pair_b = t_pair['pair_b']

    pair_c = t_pair['pair_c']

    for x in prices_json:

        if x['symbol'] == pair_a:

                       price_a = float(x['price'])

        elif x['symbol'] == pair_b:

            price_b = float(x['price'])

        elif x['symbol'] == pair_c:

            price_c = float(x['price'])

    return price_a, price_b, price_c
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

        price_a, price_b, price_c = get_price_for_t_pair(t_pair, coin_price_url)

        is_profitable, potential_profit, total_value = calculate_arbitrage(price_a, price_b, price_c)

        if is_profitable:

            print("Peluang Arbitrase Ditemukan:")

            print("Pasangan Koin:", t_pair['combined'])

            print("Potensi Keuntungan:", potential_profit)

            print("Total Nilai:", total_value)
            
            print("====================================")
            
            def main():

    coin_json = get_coin_arbitrage(coin_price_url)

    coin_list = collect_tradeables(coin_json)

    triangular_pairs_list = structure_triangular_pairs(coin_list)

    run_arbitrage(triangular_pairs_list)

if __name__ == "__main__":

    main()
    
    import time

while True:

    main()

    time.sleep(60)  # Menjalankan program setiap 1 menit
    
