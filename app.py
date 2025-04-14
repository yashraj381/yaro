from flask import Flask, request, jsonify
import openai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # ये frontend से बात करने देगा

openai.api_key = "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"

@app.route("/ask", methods=["POST"])
def ask_yaro():
    data = request.json
    user_input = data.get("message", "")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "तुम Yaro हो, एक प्यारा हिंदी बोलने वाला असिस्टेंट।"},
                {"role": "user", "content": user_input}
            ]
        )
        answer = response['choices'][0]['message']['content']
        return jsonify({"reply": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000)