from flask import Flask, abort, Response
import sys
import os

PORT = 8080
MESSAGE = "Hello World"
MESSAGE_MARS = "Hello Mars\n"

app = Flask(__name__)

counter = 0
@app.route("/")
def hello_world():
    global counter
    global MESSAGE

    return MESSAGE.encode("utf-8")

    # if divmod(int(time.time()), 10)[1] <= 3:
    #     abort(500)
    # else:
    #     return MESSAGE.encode("utf-8")
    # return MESSAGE.encode("utf-8")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
