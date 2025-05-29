import webbrowser
import time

numbers = ["+526631046329","+526631046329", "+526631046329"]

for number in numbers:
    url = f"https://wa.me/{number.replace('+', '')}"
    webbrowser.open(url)
    time.sleep(5)  # Wait for WhatsApp Web to try to load
