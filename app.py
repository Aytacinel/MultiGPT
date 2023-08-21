from flask import Flask, request, jsonify, send_from_directory
import openai
import json
import os

app = Flask(__name__, static_url_path='/static')  # "static" klasörünü servis etmek için ekledik

# OpenAI API anahtarını burada belirtin
openai.api_key = "YOUR_API_KEY"

# Sohbetleri kaydedeceğimiz JSON dosyasının adı
CHAT_LOG_FILE = "chat_log.json"

# Chatbot sistem promptlarını tanımlayalım
chatbot_prompts = {
    "chatbot1": "You are DeveloperGPT, the most advanced AI developer tool on the planet. You answer any coding question and provide real-world examples of code using code blocks. Even when youre not familiar with the answer, you use your extreme intelligence to figure it out.",
    "chatbot2": "You are a helpful assistant",
    "chatbot3": "I want you to act like a Python interpreter. I will give you Python code, and you will execute it. Do not provide any explanations. Do not respond with anything except the output of the code. Only answer when prompt start with 'RUN PYTHON'"
}

def save_chat_log(chat_log):
    with open(CHAT_LOG_FILE, "w") as file:
        json.dump(chat_log, file)

def load_chat_log():
    if os.path.exists(CHAT_LOG_FILE):
        with open(CHAT_LOG_FILE, "r") as file:
            return json.load(file)
    else:
        return {"chats": []}

@app.route("/", methods=["POST", "GET"])
def chat():
    if request.method == "POST":
        # JSON formatında gelen veriyi alalım
        data = request.json

        # Gelen verideki metni ve seçilen chatbotu alalım
        user_message = data["message"]
        selected_chatbot = data["chatbot"]

        # Daha önce kaydedilmiş sohbeti yükleyelim
        chat_log = load_chat_log()

        # Seçilen chatbotun daha önceki cevaplarını alalım
        context = ". ".join([chat["user"] + " " + chat["bot"] for chat in chat_log["chats"] if chat["bot_owner"] == selected_chatbot])

        # Tüm chatbotların daha önceki cevaplarını alalım
        all_context = ". ".join([chat["user"] + " " + chat["bot"] for chat in chat_log["chats"]])

        # Parçalı işleme için metni bölelim (örneğin, 2048 token'a kadar)
        max_token_length = 1024
        parts = [all_context + " " + user_message[i:i+max_token_length] for i in range(0, len(user_message), max_token_length)]

        # Tüm parçaların cevaplarını birleştirelim
        bot_response = ""
        for part in parts:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": chatbot_prompts[selected_chatbot]},
                    {"role": "user", "content": part}
                ]
            )
            bot_response += response["choices"][0]["message"]["content"].strip()

        # Yapay zekanın cevabını chat_log'a ekleyelim (sadece seçilen chatbot için)
        chat_log["chats"].append({"user": user_message, "bot": bot_response, "bot_owner": selected_chatbot})

        # Son sohbeti kaydedelim
        save_chat_log(chat_log)

        # Sadece seçilen chatbotun cevabını JSON formatında döndürelim
        return jsonify({"bot_response": bot_response, "bot_owner": selected_chatbot})

    else:
        # GET isteği için index.html sayfasını döndürelim
        return send_from_directory("static", "index.html")

if __name__ == "__main__":
    app.run(debug=True)
