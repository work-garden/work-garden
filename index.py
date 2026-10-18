from flask import Flask, request
import requests

app = Flask(__name__)

# --- SETTINGS ---
ACCESS_TOKEN = "EAAJ..._YOUR_TOKEN_HERE" # << ഇവിടെ നിങ്ങളുടെ Token ഇടുക
PHONE_NUMBER_ID = "1652004821944123"
VERIFY_TOKEN = "Sneha_garden_123"
OWNER_NUMBER = "919605525083" # << നിങ്ങളുടെ നമ്പർ
# ----------------

def send_whatsapp_message(to, text):
    url = f"https://graph.facebook.com/v20.0/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": text}
    }
    requests.post(url, headers=headers, json=payload)

@app.route('/webhook', methods=['GET'])
def verify_webhook():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge, 200
    else:
        return "Verification Failed", 403

@app.route('/webhook', methods=['POST'])
def handle_message():
    data = request.get_json()
    try:
        entry = data['entry'][0]['changes'][0]['value']
        if 'messages' in entry:
            message_data = entry['messages'][0]
            from_number = message_data['from']
            msg_body = message_data['text']['body'].lower()
            
            # --- BOT LOGIC WITH YOUR NUMBER ---
            if "hi" in msg_body or "hello" in msg_body or "hai" in msg_body:
                reply_text = "🌿 *Sneha Garden-ലേക്ക് സ്വാഗതം!* 🙏\n\nഞങ്ങളുടെ കളക്ഷൻ കാണാൻ:\n1️⃣ പൂച്ചെടികൾ കാണാൻ\n2️⃣ Indoor Plants\n3️⃣ Location & Contact\n\nഒരു നമ്പർ അയക്കൂ!"
            elif msg_body == "1":
                reply_text = "🌹 *പൂച്ചെടികൾ* 🌹\n\n• റോസ് - 150rs\n• ജമന്തി - 100rs\n• മുല്ല - 120rs\n• ചെമ്പരത്തി - 130rs\n\nOrder ചെയ്യാൻ 'ORDER' എന്ന് അയക്കൂ!"
            elif msg_body == "2":
                reply_text = "🏡 *Indoor Plants* 🏡\n\n• Money Plant - 200rs\n• Snake Plant - 250rs\n• Aloe Vera - 180rs\n\nOrder ചെയ്യാൻ 'ORDER' എന്ന് അയക്കൂ!"
            elif msg_body == "3":
                reply_text = f"📍 *Sneha Garden*\nKochi, Kerala\n\n📞 Contact: +91 {OWNER_NUMBER[2:]}\n👉 WhatsApp: https://wa.me/{OWNER_NUMBER}\n🗺️ Map: https://maps.google.com/?q=Sneha+Garden"
            elif "order" in msg_body:
                reply_text = f"✅ Order എടുക്കാൻ റെഡിയാണ്! 🌿\n\nനിങ്ങൾക്ക് വേണ്ട ചെടിയുടെ പേര് അയക്കൂ!\nഅല്ലെങ്കിൽ നേരിട്ട് വിളിക്കൂ: +91 {OWNER_NUMBER[2:]}\nhttps://wa.me/{OWNER_NUMBER}"
            else:
                reply_text = "ക്ഷമിക്കണം, മനസ്സിലായില്ല 😅\n\n1, 2, 3 എന്നതിൽ ഒരു നമ്പർ അയക്കൂ!"
            
            send_whatsapp_message(from_number, reply_text)
    except Exception as e:
        print(f"Error: {e}")
    return "ok", 200
