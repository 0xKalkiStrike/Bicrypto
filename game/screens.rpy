## BiCrypto 639 Screens & Interactive UI

screen say(who, what):
    style_prefix "say"

    window:
        id "window"
        if who is not None:
            text who id "who"
        text what id "what"

screen choice(items):
    style_prefix "choice"
    vbox:
        for i in items:
            textbutton i.caption action i.action

screen crypto_dashboard():
    modal False
    
    # Background Frame
    frame:
        xfill True
        yfill True
        background "#0B0E14"
        padding (25, 20)
        
        vbox:
            spacing 15
            
            # Header Bar
            hbox:
                xfill True
                text "⚡ BiCrypto 639 Pro Trading Console" size 24 color "#00E5FF" bold True
                null width 150
                text "Balance: [usdt_balance:,.2f] USDT" size 22 color "#00FFCC" bold True
                text "  |  PnL: [total_pnl:+.2f] USD" size 20 color ("#00E676" if total_pnl >= 0 else "#FF5252")
            
            null height 10
            
            # Crypto Ticker Grid
            hbox:
                spacing 20
                
                # BTC Card
                frame:
                    xsize 280
                    padding (15, 12)
                    background "#141A24"
                    vbox:
                        text "Bitcoin (BTC)" size 18 color "#FFD700" bold True
                        text "$[btc_price:,.2f]" size 24 color "#FFFFFF" bold True
                        text "[btc_change:+.2f]%" size 16 color ("#00E676" if btc_change >= 0 else "#FF5252")
                        text "Owned: [btc_holdings:.4f] BTC" size 16 color "#8899A6"
                        null height 8
                        hbox:
                            spacing 10
                            textbutton "Buy 0.1 BTC" action Function(buy_crypto, "BTC", 0.1, btc_price)
                            textbutton "Sell 0.1 BTC" action Function(sell_crypto, "BTC", 0.1, btc_price)
                
                # ETH Card
                frame:
                    xsize 280
                    padding (15, 12)
                    background "#141A24"
                    vbox:
                        text "Ethereum (ETH)" size 18 color "#7C4DFF" bold True
                        text "$[eth_price:,.2f]" size 24 color "#FFFFFF" bold True
                        text "[eth_change:+.2f]%" size 16 color ("#00E676" if eth_change >= 0 else "#FF5252")
                        text "Owned: [eth_holdings:.2f] ETH" size 16 color "#8899A6"
                        null height 8
                        hbox:
                            spacing 10
                            textbutton "Buy 1.0 ETH" action Function(buy_crypto, "ETH", 1.0, eth_price)
                            textbutton "Sell 1.0 ETH" action Function(sell_crypto, "ETH", 1.0, eth_price)
                
                # BIC Card
                frame:
                    xsize 280
                    padding (15, 12)
                    background "#141A24"
                    vbox:
                        text "BiCrypto (BIC)" size 18 color "#00E5FF" bold True
                        text "$[bic_price:,.2f]" size 24 color "#FFFFFF" bold True
                        text "[bic_change:+.2f]%" size 16 color ("#00E676" if bic_change >= 0 else "#FF5252")
                        text "Owned: [bic_holdings:.1f] BIC" size 16 color "#8899A6"
                        null height 8
                        hbox:
                            spacing 10
                            textbutton "Buy 10 BIC" action Function(buy_crypto, "BIC", 10.0, bic_price)
                            textbutton "Sell 10 BIC" action Function(sell_crypto, "BIC", 10.0, bic_price)

                # Control Action Card
                frame:
                    xsize 280
                    padding (15, 12)
                    background "#1C2430"
                    vbox:
                        text "Market Action" size 18 color "#00E5FF" bold True
                        null height 10
                        textbutton "🔄 Simulate Market Tick" action Function(simulate_market_tick)
                        null height 8
                        textbutton "📊 Reset Portfolio" action Function(reset_portfolio)
                        null height 8
                        textbutton "💬 Talk to Analyst" action Return("analyst_talk")

            null height 15

            # Bottom Analytics Section
            hbox:
                spacing 20
                
                # Portfolio Overview Table
                frame:
                    xsize 580
                    ysize 260
                    padding (20, 15)
                    background "#141A24"
                    vbox:
                        text "💼 Portfolio Asset Allocation" size 20 color "#FFFFFF" bold True
                        null height 10
                        text "USDT Cash: $[usdt_balance:,.2f]" size 18 color "#00FFCC"
                        text "BTC Value: $[btc_holdings * btc_price:,.2f]" size 18 color "#FFD700"
                        text "ETH Value: $[eth_holdings * eth_price:,.2f]" size 18 color "#7C4DFF"
                        text "BIC Value: $[bic_holdings * bic_price:,.2f]" size 18 color "#00E5FF"
                        null height 10
                        text "Total Net Worth: $[total_net_worth:,.2f] USD" size 20 color "#FFFFFF" bold True
                
                # Live News Feed
                frame:
                    xsize 580
                    ysize 260
                    padding (20, 15)
                    background "#141A24"
                    vbox:
                        text "📰 Live Market Signals & Intelligence" size 20 color "#FFFFFF" bold True
                        null height 10
                        text "• [news_headline_1]" size 16 color "#E0E0E0"
                        null height 6
                        text "• [news_headline_2]" size 16 color "#E0E0E0"
                        null height 6
                        text "• [news_headline_3]" size 16 color "#E0E0E0"
                        null height 12
                        text "Fear & Greed Index: [fear_greed_index] / 100 ([fear_greed_label])" size 16 color ("#00E676" if fear_greed_index >= 50 else "#FF5252") bold True

style say_window:
    xalign 0.5
    yalign 0.95
    xsize 1200
    ysize 160
    background "#141A24"
    padding (25, 20)

style say_who:
    size 24
    bold True

style say_what:
    size 20
    color "#FFFFFF"

style choice_vbox:
    xalign 0.5
    yalign 0.5
    spacing 12

style choice_button:
    background "#1C2430"
    padding (20, 12)
    xsize 600

style choice_button_text:
    size 20
    color "#00E5FF"
    xalign 0.5
