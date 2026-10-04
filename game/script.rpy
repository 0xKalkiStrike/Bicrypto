# BiCrypto 639 - Clean Ren'Py Game Script

define config.name = "BiCrypto 639"
define config.version = "1.0.0"
define config.screen_width = 1280
define config.screen_height = 720

define player = Character("Trader", color="#00ffcc")
define analyst = Character("Crypto Analyst", color="#ffaa00")

label start:
    scene black
    with dissolve

    "Welcome to BiCrypto 639 - Crypto Trading Simulator."
    
    analyst "Market analysis initialized. Welcome to the BiCrypto trading platform."

    menu:
        "Check Crypto Market Overview":
            jump market_overview
        "View Portfolio":
            jump view_portfolio
        "Exit Application":
            jump end_game

label market_overview:
    analyst "Bitcoin (BTC): $95,000 (+4.2%)"
    analyst "Ethereum (ETH): $3,500 (+2.8%)"
    analyst "BiCrypto Token (BIC): $639.00 (+15.4%)"
    
    jump start

label view_portfolio:
    player "Current Portfolio Value: $10,000 USD."
    player "Holdings: 10 BIC, 0.05 BTC, 1.2 ETH."
    
    jump start

label end_game:
    "Thank you for using BiCrypto 639."
    return
