import time
import requests

def send_telegram_message(chat_id, bot_token, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message: {response.status_code}, {response.text}")

if __name__ == "__main__":
    bot_token = "7946011547:AAF_8ZNDZISi5SbhQNXkGXUFIGgc4JEbAvw"  # Bot token
    chat_id = "1498839589"  # Correct chat ID extracted from the updates
    message = "Please avoid talking to your brother for now."
    
    # Send the message every 10 minutes
    while True:
        send_telegram_message(chat_id, bot_token, message)
        time.sleep(600)  # Wait for 10 minutes
