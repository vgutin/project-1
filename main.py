from flask import Flask
from electricity import Electricity

# from flask_cors import CORS

app = Flask(__name__, static_folder='../react-electricity/build', static_url_path='/')
app.config['JSON_AS_ASCII'] = False  # отключаем выдачу результата в ASCII


# CORS(app)

@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/electricity/', methods=['GET'])
def get_electricity():
    elect = Electricity()
    return elect.get_all()


if __name__ == '__main__':
    app.run(debug=True)
