from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Your API token (keep it secret!)
API_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiI3OTQ1MTIyMjA2IiwianRpIjoiZWNmZTVlZmQtMDE2Yy00YmQyLTkyOTEtMDRlMzM5NzFkYjQ4IiwiZXhwIjoxNzkyMjQ1NjU3fQ.CohYSUJMLYthpk--yQKf4SrjyFs7OUVuFd8bIT6yNlmU4TNWvVqsuTHgcKGUdKdHLlK8dUDOvtjOl_hv00jvYwT58-Aaa-pJmSD7Jm58z34AZiVMyAVK99N0X7RHYKEofeoiali0TN6hoplvQwqKF3QjMsZcaSv0d7pWwSIwm4E"

# Copyright-style username
USERNAME = "© @ig_banz"

# Root URL - fun Hinglish message
@app.route("/")
def home():
    return jsonify({
        "message": "Oye, kya dekh raha hai? 😏 Ye API chori karne ka nahi hai!",
        "warning": "© @ig_banz ka data hai, respect dena zaroori hai 🤚",
        "note": "Stats dekhna hai toh /user/user_id use karo. Chill maro 😎",
        "example_user_id": 8457829943
    })

# User stats route
@app.route("/user/<int:user_id>")
def get_user_stats(user_id):
    url = f"https://funstat.info/api/v1/users/{user_id}/stats_min"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {API_TOKEN}"
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        # Inject your copyright username in fun style
        data["DEVLOPER 👉🏻"] = USERNAME
        return jsonify(data)
    else:
        return jsonify({
            "error": f"Request failed with status code {response.status_code}",
            "DEVLOPER 👉🏻": USERNAME
        }), response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)