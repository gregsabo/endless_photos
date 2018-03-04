import requests
from bs4 import BeautifulSoup
from pudb import set_trace
from flask import Flask
# import py_imgcat

def get_image():
    html = requests.get("https://commons.wikimedia.org/wiki/Special:Random/File")
    soup = BeautifulSoup(html.text, 'html.parser')
    images = soup.select(".fullImageLink img")
    if len(images) is 0:
        return "https://upload.wikimedia.org/wikipedia/commons/5/57/Malevich.black-square.jpg"
    return images[0]['src']


if __name__ == '__main__':
    get_image()

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <body>
            <style>
                body {
                    background-color: black;
                    text-align: center;
                    margin: 0;
                    padding: 0;

                }

                img {
                    width: 100%%;
                }
            </style>
            <img src="%s" />
            <script>
                setTimeout(function() {
                    window.location.reload();
                }, 5000)
            </script>
        </body>
    </html>
    """ % get_image()