import vonage
client = vonage.Client(key="222ce96c", secret="11bYzrXnbKOi2fb7")
sms = vonage.Sms(client)
responseData = sms.send_message(
    {
        "from": "Vonage APIs",
        "to": "917488160265",
        "text": "Please hurry \n Patient is alert",
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")