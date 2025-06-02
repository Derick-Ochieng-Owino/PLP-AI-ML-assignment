class CryptoBot:
    def __init__(self):
        self.name = "CryproBot"
        self.greeting = "Welcome to CryptoCurrency World"
        self.crypto_db = {
            "Bitcoin": {
                "price_trend": "rising",
                "market_cap": "high",
                "energy_use": "high",
                "sustainability_score": 3 / 10
            },
            "Ethereum": {
                "price_trend": "stable",
                "market_cap": "high",
                "energy_use": "medium",
                "sustainability_score": 6 / 10
            },
            "Cardano": {
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 8 / 10
            }
        }
    
    def response(self, user_input):
        self.user_input = user_input.lower()

        print(self.greeting)
        if "sustainable" in user_input or "eco" in user_input:
            recommend = max(
                (c for c in self.crypto_db if self.crypto_db[c]["energy_use"] == "low" and self.crypto_db[c]["sustainability_score"] > 0.7),
                key=lambda c: self.crypto_db[c]["sustainability_score"],
                default=None
            )
            if recommend:
                print(f"Invest in {recommend}! 🌱 It’s eco-friendly and has long-term potential!")
            else:
                print("No highly sustainable options found. Try again later!")

        elif "trending" in user_input or "growth" in user_input:
            # Filter coins that are rising and have high market cap
            candidates = [c for c in self.crypto_db if self.crypto_db[c]["price_trend"] == "rising" and self.crypto_db[c]["market_cap"] == "high"]
            if candidates:
                print(f"{candidates[0]} is trending up with a strong market cap! 🚀")
            else:
                print("No trending high market cap cryptos found right now.")

        else:
            print("Sorry, I only understand queries about sustainability or trending crypto for now.")

# Sample run
bot = CryptoBot()
while True:
    query = input("\nYou: ")
    if query.lower() in ["exit", "quit", "bye"]:
        print("CryptoBuddy: See you later! Stay savvy! 👋")
        break
    bot.response(query)