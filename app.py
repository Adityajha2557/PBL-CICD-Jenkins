from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>PBL CI/CD Application</title>
        </head>
        <body>
            <h1>CI/CD Pipeline Successfully Deployed!</h1>
            <p>Docker + Jenkins + Kubernetes</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)