import yfinance as yf
import time

def track_stock_price(symbol, interval=60, duration=3600):
    end_time = time.time() + duration

    while time.time() < end_time:
        stock = yf.Ticker(symbol)
        try:
            current_price = stock.history(period='1d')['Close'].iloc[-1]
            print(f"Current price of {symbol}: ${current_price:.2f}")
        except:
            print(f"An error occured or Symbol {symbol} is not a valid symbol.")
        
        time.sleep(interval)

if __name__ == "__main__":
    stock_symbol = input("Enter the symbol of the stock: ")
    update_interval = int(input("Enter the update interval in seconds: "))
    tracking_duration = int(input("Enter the tracking duration in seconds: "))

    track_stock_price(stock_symbol, update_interval, tracking_duration)
