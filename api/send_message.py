import requests
import json

def handler(request):
    # Get chat ID and message from the request body (for flexibility)
    chat_id = "1498839589"  # Example chat ID
    bot_token = "7946011547:AAF_8ZNDZISi5SbhQNXkGXUFIGgc4JEbAvw"
    message = "Please avoid talking to your brother for now."

    # Send the message via Telegram Bot API
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    response = requests.post(url, data=payload)

    if response.status_code == 200:
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Message sent successfully!"})
        }
    else:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": f"Failed to send message: {response.text}"})
        }
