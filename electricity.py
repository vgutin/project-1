from flask import jsonify
from database import Database


class Electricity:
    def __init__(self):
        pass

    def get_all(self):
        db = Database()
        db.connect()
        # TODO сделать вывод показаний за последний 2 календарные месяца (текущий и предыдущий) исключив из списка неактивных арендаторов
        db.cursor.execute("SELECT r.legal_enity, r.brand_name, r.room, ec.factory_number, ec.ktr, " 
                          "(SELECT lead(value) OVER (ORDER BY date desc) AS prev_value FROM electricity_readings WHERE electricity_counter_id=ec.id LIMIT 1), "
                          "(SELECT value AS current_value FROM electricity_readings WHERE electricity_counter_id=ec.id ORDER BY date desc LIMIT 1), "
                          "r.id AS renter_id, ec.id AS counter_id "
                          "FROM electricity_counters ec LEFT JOIN renters r ON ec.renters_id=r.id;")
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
                    'final_readings': row[6],
                    'renter_id': row[7],
                    'counter_id': row[8]
                }
            )
        db.close()
        return jsonify(result)

    def get_counter(self, counter_id):
        db = Database()
        db.connect()
        db.cursor.execute(f"SELECT factory_number, ktr, r.legal_enity, r.brand_name, r.room "
                          f"FROM electricity_counters ec "
                          f"LEFT JOIN renters r ON ec.renters_id=r.id "
                          f"WHERE ec.id={counter_id} LIMIT 1;")
        responce = dict()
        counter = list()
        # TODO сделать прямой вывод единственного значения не через цикл
        for row in db.cursor:
            counter.append(
                {
                    'factory_number': row[0],
                    'KTR': row[1],
                    'legal_enity': row[2],
                    'brand_name': row[3],
                    'room': row[4]
                }
            )
        db.cursor.execute(f"SELECT value, date FROM electricity_readings er "
                          f"WHERE er.electricity_counter_id={counter_id} "
                          f"ORDER BY DATE DESC LIMIT 36")
        readings = list()
        for row in db.cursor:
            readings.append(
                {
                    'value': row[0],
                    'date': row[1]

                }
            )
        db.close()
        responce = {'counter': counter, 'readings': readings}
        return jsonify(responce)
