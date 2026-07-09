from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "project": "WhatsApp AI Assistant",
        "version": "0.1.0",
        "status": "running"
    }

if __name__ == "__main__":
    app.run()
