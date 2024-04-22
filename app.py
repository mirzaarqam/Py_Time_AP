from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/get_time', methods=['GET'])
def get_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {'time': current_time}

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='10.22.202.81', port=5000, debug=True)
