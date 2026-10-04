# BiCrypto 639 - Interactive Cryptocurrency Trading Engine

define analyst = Character("Lead Analyst Vance", color="#00E5FF")
define trader = Character("You (Trader)", color="#00FFCC")

init python:
    import random

    # Financial State Variables
    initial_capital = 50000.0
    usdt_balance = 50000.0

    btc_price = 95000.0
    eth_price = 3500.0
    bic_price = 639.0

    btc_change = 4.25
    eth_change = 2.80
    bic_change = 15.40

    btc_holdings = 0.25
    eth_holdings = 3.0
    bic_holdings = 100.0

    news_pool = [
        "Federal Reserve signals liquidity injection; Risk assets rally.",
        "BiCrypto 639 Protocol V2 upgrade deployed successfully on mainnet.",
        "Institutional inflow into Bitcoin ETFs reaches $1.2B in single session.",
        "Ethereum gas fees hit 6-month lows as L2 transaction volumes surge.",
        "Global crypto market capitalization crosses $3.5 Trillion benchmark."
    ]

    news_headline_1 = news_pool[0]
    news_headline_2 = news_pool[1]
    news_headline_3 = news_pool[2]

    fear_greed_index = 78
    fear_greed_label = "Extreme Greed"

    btc_val = 0.25 * 95000.0
    eth_val = 3.0 * 3500.0
    bic_val = 100.0 * 639.0
    total_net_worth = usdt_balance + btc_val + eth_val + bic_val
    total_pnl = 0.0

    def calculate_metrics():
        global total_net_worth, total_pnl, btc_val, eth_val, bic_val
        btc_val = btc_holdings * btc_price
        eth_val = eth_holdings * eth_price
        bic_val = bic_holdings * bic_price
        net = usdt_balance + btc_val + eth_val + bic_val
        total_net_worth = net
        total_pnl = net - (initial_capital + (0.25 * 95000.0) + (3.0 * 3500.0) + (100.0 * 639.0))

    def buy_crypto(symbol, amount, price):
        global usdt_balance, btc_holdings, eth_holdings, bic_holdings
        cost = amount * price
        if usdt_balance >= cost:
            usdt_balance -= cost
            if symbol == "BTC":
                btc_holdings += amount
            elif symbol == "ETH":
                eth_holdings += amount
            elif symbol == "BIC":
                bic_holdings += amount
            calculate_metrics()
            renpy.notify(f"Bought {amount} {symbol} for ${cost:,.2f} USDT")
        else:
            renpy.notify("Insufficient USDT balance for this order!")

    def sell_crypto(symbol, amount, price):
        global usdt_balance, btc_holdings, eth_holdings, bic_holdings
        if symbol == "BTC" and btc_holdings >= amount:
            btc_holdings -= amount
            usdt_balance += amount * price
        elif symbol == "ETH" and eth_holdings >= amount:
            eth_holdings -= amount
            usdt_balance += amount * price
        elif symbol == "BIC" and bic_holdings >= amount:
            bic_holdings -= amount
            usdt_balance += amount * price
        else:
            renpy.notify(f"Insufficient {symbol} holdings to sell!")
            return
        calculate_metrics()
        renpy.notify(f"Sold {amount} {symbol} for ${amount * price:,.2f} USDT")

    def simulate_market_tick():
        global btc_price, eth_price, bic_price, btc_change, eth_change, bic_change
        global news_headline_1, news_headline_2, news_headline_3, fear_greed_index, fear_greed_label

        b_delta = random.uniform(-0.03, 0.04)
        e_delta = random.uniform(-0.04, 0.05)
        bic_delta = random.uniform(-0.05, 0.08)

        btc_price = max(1000.0, btc_price * (1.0 + b_delta))
        eth_price = max(100.0, eth_price * (1.0 + e_delta))
        bic_price = max(1.0, bic_price * (1.0 + bic_delta))

        btc_change = b_delta * 100.0
        eth_change = e_delta * 100.0
        bic_change = bic_delta * 100.0

        shuffled = list(news_pool)
        random.shuffle(shuffled)
        news_headline_1, news_headline_2, news_headline_3 = shuffled[:3]

        fear_greed_index = random.randint(35, 92)
        if fear_greed_index >= 75:
            fear_greed_label = "Extreme Greed"
        elif fear_greed_index >= 55:
            fear_greed_label = "Greed"
        elif fear_greed_index >= 45:
            fear_greed_label = "Neutral"
        else:
            fear_greed_label = "Fear"

        calculate_metrics()
        renpy.notify("Market prices and signals updated!")

    def reset_portfolio():
        global usdt_balance, btc_holdings, eth_holdings, bic_holdings
        global btc_price, eth_price, bic_price
        usdt_balance = 50000.0
        btc_holdings = 0.25
        eth_holdings = 3.0
        bic_holdings = 100.0
        btc_price = 95000.0
        eth_price = 3500.0
        bic_price = 639.0
        calculate_metrics()
        renpy.notify("Portfolio reset to initial default state.")

    calculate_metrics()

label start:
    scene black
    with dissolve

    analyst "Welcome to the BiCrypto 639 High-Frequency Trading Terminal."
    analyst "You have $50,000 USDT in starting capital alongside initial crypto holdings."
    
    jump dashboard_loop

label dashboard_loop:
    call screen crypto_dashboard

    if _return == "analyst_talk":
        analyst "Market sentiment is currently [fear_greed_label] ([fear_greed_index]/100)."
        analyst "BiCrypto (BIC) is currently trading at $[bic_price:,.2f]."
        jump dashboard_loop

    jump dashboard_loop
