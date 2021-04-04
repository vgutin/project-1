from flask import Flask, jsonify
# from flask_cors import CORS

# app = Flask(__name__)
app = Flask(__name__, static_folder='../build', static_url_path='/')
app.config['JSON_AS_ASCII'] = False  # отключаем выдачу результата в ASCII
# CORS(app)

db_electricity = [
    {
        'id': 1,
        'legal_entity': 'ООО "ОКЕЙ"',
        'brand': 'ОКЕЙ',
        'room_number': '0-01',
        'energy_meter_number': '07927265',
        'KTR': 240,
        'initial_readings': 1267433,
        'final_readings': 1267800
    },
    {
        'id': 2,
        'legal_entity': 'ООО "ОКЕЙ"',
        'brand': 'ОКЕЙ',
        'room_number': '0-01',
        'energy_meter_number': '07926824',
        'KTR': 240,
        'initial_readings': 20115,
        'final_readings': 20318
    }
]

@app.route('/')
def index():
    return app.send_static_file('index.html')

# @app.route('/')
# def hello():
#     return '<a href="/electricity">to electricity</a>'


@app.route('/electricity/', methods=['GET'])
def get_electricity():
    return jsonify({'electricity': db_electricity})


if __name__ == '__main__':
    app.run(debug=True)
