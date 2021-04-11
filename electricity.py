from flask import jsonify
from database import Database


class Electricity:
    def __init__(self):
        pass

    def get_all(self):
        db = Database()
        db.connect()
        db.cursor.execute(
            "SELECT r.legal_enity, r.brand_name, r.room, ec.factory_number, ec.ktr, (SELECT lead(value) OVER (ORDER BY date desc) AS prev_value FROM electricity_readings WHERE electricity_counter_id=ec.id LIMIT 1), (SELECT value AS current_value FROM electricity_readings WHERE electricity_counter_id=ec.id ORDER BY date desc LIMIT 1) FROM electricity_counters ec LEFT JOIN renters r ON ec.renters_id=r.id;")
        result = list()
        for row in db.cursor:
            result.append(
                {
                    'legal_entity': row[0],
                    'brand': row[1],
                    'room_number': row[2],
                    'energy_meter_number': row[3],
                    'KTR': row[4],
                    'initial_readings': row[5],
                    'final_readings': row[6]
                }
            )
        db.close()
        return jsonify({'electricity': result})
