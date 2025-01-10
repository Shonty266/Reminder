import time
import requests
import schedule

def send_telegram_message(chat_id, bot_token, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message: {response.status_code}, {response.text}")

def job():
    bot_token = "7946011547:AAF_8ZNDZISi5SbhQNXkGXUFIGgc4JEbAvw"
    chat_id = "1498839589"  # Correct chat ID
    message = "Please avoid talking to your brother for now."
    send_telegram_message(chat_id, bot_token, message)

# Schedule the job every 10 minutes
schedule.every(10).minutes.do(job)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
