import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
import requests

load_dotenv()
EURON_API_KEY = os.getenv("EURON_API_TOKEN")

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static"

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        language = request.form["language"]
        file = request.files["file"]

        if file:
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # ✅ Transcribe to English using Euron (Whisper)
            with open(filepath, "rb") as audio_file:
                whisper_response = requests.post(
                    url="https://api.euron.one/api/v1/euri/alpha/audio/translations",  # ✅ THIS IS THE CORRECT ROUTE
                    headers={
                        "Authorization": f"Bearer {EURON_API_KEY}"
                    },
                    files={"file": (filename, audio_file, "audio/mp3")},
                    data={"model": "whisper-1"}
                )

            try:
                whisper_data = whisper_response.json()
                print("Whisper Response:", whisper_data)
                transcript_text = whisper_data.get("text", "")
            except Exception as e:
                return jsonify({"error": f"Failed to parse transcription response: {str(e)}"})

            if not transcript_text:
                return jsonify({
                    "error": "Transcription failed.",
                    "euron_response": whisper_data
                })

            # ✅ Translate English transcript to target language
            chat_response = requests.post(
                url="https://api.euron.one/api/v1/euri/alpha/chat/completions",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {EURON_API_KEY}",
                },
                json={
                    "model": "gpt-4.1-nano",
                    "messages": [
                        {
                            "role": "system",
                            "content": f"You will be provided with a sentence in English, and your task is to translate it into {language}."
                        },
                        {
                            "role": "user",
                            "content": transcript_text
                        }
                    ],
                    "temperature": 0,
                    "max_tokens": 256
                }
            )

            chat_data = chat_response.json()
            print("Chat Response:", chat_data)

            translation = chat_data.get("choices", [{}])[0].get("message", {}).get("content", "No translation received.")

            return jsonify({
                "original": transcript_text,
                "translated": translation
            })

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8080)
