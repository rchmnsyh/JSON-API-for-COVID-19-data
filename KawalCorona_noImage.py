from flask import Flask
import requests

data = requests.get("https://api.kawalcorona.com/indonesia")
# print(data.json()[0]['name'])

app = Flask(__name__)

@app.route('/')
def post():
    data = requests.get("https://api.kawalcorona.com/indonesia")
    return {
        "chats": [
            {
                "columns": [
                    {
                    "title": "Kasus Positif",
                    "text": data.json()[0]["positif"] + " orang"
                    },
                    {
                    "title": "Pasien Sembuh",
                    "text": data.json()[0]["sembuh"] + " orang"
                    },
                    {
                    "title": "Pasien Meninggal",
                    "text": data.json()[0]["meninggal"] + " orang"
                    }
                ],
                "type": "carousel"
            }
        ]
    }

if __name__ == "__main__":
    app.run()