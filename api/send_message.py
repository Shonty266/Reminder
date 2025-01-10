import requests
import logging
import time

# Configure logging to capture debug information
logging.basicConfig(level=logging.DEBUG)

def send_telegram_message():
    bot_token = "7946011547:AAF_8ZNDZISi5SbhQNXkGXUFIGgc4JEbAvw"  # Your bot token
    chat_id = "1498839589"  # Your chat ID
    message = "This is a periodic reminder message."

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}

    try:
        # Send the message
        response = requests.post(url, data=payload)
        logging.debug(f"Response: {response.status_code}, {response.text}")

        if response.status_code == 200:
            logging.info("Message sent successfully!")
        else:
            logging.error(f"Failed to send message: {response.status_code}, {response.text}")
    except Exception as e:
        logging.error(f"Error sending message: {str(e)}")

if __name__ == "__main__":
    while True:
        send_telegram_message()  # Send the message
        time.sleep(600)  # Wait for 10 minutes (600 seconds) before sending the next message
