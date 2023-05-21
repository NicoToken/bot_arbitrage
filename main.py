import requests

import json

import time

from binance.client import Client

api_key = 'api_key'

api_secret = 'api_secret'

client = Client(api_key, api_secret)

def get_coin_arbitrage():

    tickers = client.get_ticker()

    return tickers

def collect_tradeables(tickers):

    coin_list = []

    for ticker in tickers:

        coin_list.append(ticker['symbol'])

    return coin_list

def structure_triangular_pairs(coin_list):

    triangular_pairs_list = []

    for i in range(len(coin_list)):

        for j in range(i + 1, len(coin_list)):

            for k in range(j + 1, len(coin_list)):

                pair_a = coin_list[i]

                pair_b = coin_list[j]

                pair_c = coin_list[k]

                triangular_pairs_list.append([pair_a, pair_b, pair_c])

    return triangular_pairs_list

def get_price_for_t_pair(t_pair):

    prices = client.get_orderbook_tickers()

    price_dict = {}

    for price in prices:

        symbol = price['symbol']

        ask_price = float(price['askPrice'])

        bid_price = float(price['bidPrice'])

        price_dict[symbol] = {'ask': ask_price, 'bid': bid_price}

    return price_dict

def cal_triangular_arb_surface_rate(t_pair, prices_dict):

    starting_amount = 1

    min_surface_rate = 0

    surface_dict = {}

    pair_a = t_pair[0]

    pair_b = t_pair[1]

    pair_c = t_pair[2]

    a_ask = prices_dict[pair_a]['ask']

    a_bid = prices_dict[pair_a]['bid']

    b_ask = prices_dict[pair_b]['ask']

    b_bid = prices_dict[pair_b]['bid']

    c_ask = prices_dict[pair_c]['ask']

    c_bid = prices_dict[pair_c]['bid']

    direction_list = ['forward', 'reverse']

    for direction in direction_list:

        swap_1_rate = 0

        swap_2_rate = 0

        swap_3_rate = 0

        if direction == "forward":

            swap_1_rate = 1 / a_ask

        if direction == "reverse":

            swap_1_rate = a_bid

        acquired_coin_t1 = starting_amount * swap_1_rate

        for direction2 in direction_list:

            swap_2_rate = 0

            if direction2 == "forward":

                swap_2_rate = 1 / b_ask

            if direction2 == "reverse":

                swap_2_rate = b_bid

            acquired_coin_t2 = acquired_coin_t1 * swap_2_rate

            for direction3 in direction_list:

                swap_3_rate = 0

                if direction3 == "forward":

                    swap_3_rate = 1 / c_ask

                if direction3 == "reverse":

                    swap_3_rate = c_bid

                acquired_coin_t3 = acquired_coin_t2 * swap_3_rate

                profit_loss = acquired_coin_t3 - starting_amount

                profit_loss_perc = (profit_loss / starting_amount) * 100 if profit_loss != 0 else 0

                if profit_loss_perc > min_surface_rate:

                    surface_dict = {

                        "pair_a": pair_a,

                        "pair_b": pair_b,

                        "pair_c": pair_c,

                        "direction_trade_1": direction,

                        "direction_trade_2": direction2,

                        "direction_trade_3": direction3,

                        "profit_loss": profit_loss,

                        "profit_loss_percentage": profit_loss_perc

                    }

                    min_surface_rate = profit_loss_perc

    return surface_dict

def find_arbitrage_opportunities(triangular_pairs_list):

    arbitrage_opportunities = []

    for t_pair in triangular_pairs_list:

        prices_dict = get_price_for_t_pair(t_pair)

        surface_dict = cal_triangular_arb_surface_rate(t_pair, prices_dict)

        if surface_dict:

            arbitrage_opportunities.append(surface_dict)

    return arbitrage_opportunities

def execute_arbitrage(trade_opportunity):

    # Implement your arbitrage execution logic here

    # This function will execute the arbitrage trade based on the given trade_opportunity dictionary

    # Make sure to handle errors and exceptions during the trade execution process

    # Example implementation:

    pair_a = trade_opportunity['pair_a']

    pair_b = trade_opportunity['pair_b']

    pair_c = trade_opportunity['pair_c']

    direction_trade_1 = trade_opportunity['direction_trade_1']

    direction_trade_2 = trade_opportunity['direction_trade_2']

    direction_trade_3 = trade_opportunity['direction_trade_3']

    print(f"Executing arbitrage opportunity:")

    print(f"Pair A: {pair_a}, Direction: {direction_trade_1}")

    print(f"Pair B: {pair_b}, Direction: {direction_trade_2}")

    print(f"Pair C: {pair_c}, Direction: {direction_trade_3}")

    print(f"Profit/Loss: {trade_opportunity['profit_loss']}")

    print(f"Profit/Loss Percentage: {trade_opportunity['profit_loss_percentage']}")

    # Add your arbitrage execution logic here

# Main function

def main():

    tickers = get_coin_arbitrage()

    coin_list = collect_tradeables(tickers)

    triangular_pairs_list = structure_triangular_pairs(coin_list)

    arbitrage_opportunities = find_arbitrage_opportunities(triangular_pairs_list)

    print("Arbitrage Opportunities:")

    for opportunity in arbitrage_opportunities:

        print(opportunity)

    # Execute arbitrage for each opportunity

    for opportunity in arbitrage_opportunities:

        execute_arbitrage(opportunity)

        time.sleep(1)  # Pause between trades to avoid rate limits or errors

# Run the main function

if __name__ == "__main__":

    main()

