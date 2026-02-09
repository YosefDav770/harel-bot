import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# --- Your Access Details from Green-API ---
# Replace the numbers inside the quotes with your real details
ID_INSTANCE = "7103509946"
API_TOKEN = "16176ae214c442d2b8a14fbf5ad5f1503bc7d30cb0be416e88"

def send_whatsapp_message(chat_id, text):
    url = f"https://api.green-api.com/waInstance{ID_INSTANCE}/sendMessage/{API_TOKEN}"
    payload = {
        "chatId": chat_id,
        "message": text
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

@app.route("/", methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        data = request.json
        print("Received message:", data)
        return jsonify({"status": "success"}), 200
    return "Bot is Running!", 200

if __name__ == "__main__":
    # Change '972XXXXXXXXX' to your actual phone number to test
    send_whatsapp_message("972509902568@c.us", "Bot is now Online and Ready!")
    app.run(host='0.0.0.0', port=5000)
