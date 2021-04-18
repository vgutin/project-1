from flask import Flask
from electricity import Electricity

app = Flask(__name__, static_folder='../react-electricity/build', static_url_path='/')


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/api/electricity/', methods=['GET'])
def get_electricity():
    elect = Electricity()
    return elect.get_all()


@app.route('/api/electricity/counters/<int:counter_id>', methods=['GET'])
def get_electricity_counter(counter_id):
    elect = Electricity()
    return elect.get_counter(counter_id)


if __name__ == '__main__':
    app.run(debug=True)
