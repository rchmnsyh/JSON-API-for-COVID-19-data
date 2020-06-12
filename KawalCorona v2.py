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
                    "image_url": "https://media.istockphoto.com/vectors/hospitalization-of-the-patient-a-sick-person-vector-id639973454?b=1&k=6&m=639973454&s=612x612&h=R0Qfj4NhJQO7FO37WG4tNNc8C6uwECHPO8Ep2UbjtRs=",
                    "title": "Kasus Positif",
                    "text": data.json()[0]["positif"] + " orang"
                    },
                    {
                    "image_url": "https://img.freepik.com/free-vector/old-man-hospital-room_82574-2898.jpg",
                    "title": "Pasien Sembuh",
                    "text": data.json()[0]["sembuh"] + " orang"
                    },
                    {
                    "image_url": "https://image.freepik.com/free-vector/funeral-composition-with-flat-design_23-2147996208.jpg",
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