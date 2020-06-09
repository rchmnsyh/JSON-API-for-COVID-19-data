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
                    "image_url": "https://kawalcorona.com/uploads/sad-u6e.png",
                    "title": "Kasus Positif",
                    "text": data.json()[0]["positif"] + " orang"
                    },
                    {
                    "image_url": "https://kawalcorona.com/uploads/happy-ipM.png",
                    "title": "Pasien Sembuh",
                    "text": data.json()[0]["sembuh"] + " orang"
                    },
                    {
                    "image_url": "https://kawalcorona.com/uploads/emoji-LWx.png",
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