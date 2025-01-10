import requests
import logging

logging.basicConfig(level=logging.DEBUG)

def send_telegram_message():
    bot_token = "your-bot-token"
    chat_id = "your-chat-id"
    message = "This is a periodic reminder message."

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}

    try:
        response = requests.post(url, data=payload)
        logging.debug(f"Response: {response.status_code}, {response.text}")

        if response.status_code == 200:
            logging.info("Message sent successfully!")
        else:
            logging.error(f"Failed to send message: {response.status_code}, {response.text}")
    except Exception as e:
        logging.error(f"Error sending message: {str(e)}")

if __name__ == "__main__":
    send_telegram_message()
