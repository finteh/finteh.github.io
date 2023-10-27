import psycopg2

import config

from datetime import datetime
from waitress import serve
from flask import Flask
from flask import jsonify


app = Flask(__name__)


@app.route('/ibc_voting_data', methods=['GET'])
def get_ibc_data():
    res = select_const()
    response = {
        'CWD': {},
        'BTS': {},
        'VIZ': {},
        'EOS': {},
        'WAX': {},
        'HIVE': {},
        'ATOM': {},
        'STEEM': {}
    }
    for item in res:
        if 'cwd_tlg' in item:
            response['CWD']['tlg'] = item[1]
        elif 'cwd_worker' in item:
            response['CWD']['worker'] = item[1]
        elif 'cwd_worker_percent' in item:
            response['CWD']['worker_percent'] = item[1]
        elif 'cwd_tlg_percent' in item:
            response['CWD']['tlg_percent'] = item[1]
        elif 'cwd_worker_link' in item:
            response['CWD']['worker_link'] = item[1]
        elif 'cwd_tlg_link' in item:
            response['CWD']['tlg_link'] = item[1]

        elif 'bts_tlg' in item:
            response['BTS']['tlg'] = item[1]
        elif 'bts_worker' in item:
            response['BTS']['worker'] = item[1]
        elif 'bts_worker_percent' in item:
            response['BTS']['worker_percent'] = item[1]
        elif 'bts_tlg_percent' in item:
            response['BTS']['tlg_percent'] = item[1]
        elif 'bts_worker_link' in item:
            response['BTS']['worker_link'] = item[1]
        elif 'bts_tlg_link' in item:
            response['BTS']['tlg_link'] = item[1]

        elif 'viz_tlg' in item:
            response['VIZ']['tlg'] = item[1]
        elif 'viz_worker' in item:
            response['VIZ']['worker'] = item[1]
        elif 'viz_worker_percent' in item:
            response['VIZ']['worker_percent'] = item[1]
        elif 'viz_tlg_percent' in item:
            response['VIZ']['tlg_percent'] = item[1]
        elif 'viz_worker_link' in item:
            response['VIZ']['worker_link'] = item[1]
        elif 'viz_tlg_link' in item:
            response['VIZ']['tlg_link'] = item[1]

        elif 'eos_tlg' in item:
            response['EOS']['tlg'] = item[1]
        elif 'eos_worker' in item:
            response['EOS']['worker'] = item[1]
        elif 'eos_worker_percent' in item:
            response['EOS']['worker_percent'] = item[1]
        elif 'eos_tlg_percent' in item:
            response['EOS']['tlg_percent'] = item[1]
        elif 'eos_worker_link' in item:
            response['EOS']['worker_link'] = item[1]
        elif 'eos_tlg_link' in item:
            response['EOS']['tlg_link'] = item[1]

        elif 'wax_tlg' in item:
            response['WAX']['tlg'] = item[1]
        elif 'wax_worker' in item:
            response['WAX']['worker'] = item[1]
        elif 'wax_worker_percent' in item:
            response['WAX']['worker_percent'] = item[1]
        elif 'wax_tlg_percent' in item:
            response['WAX']['tlg_percent'] = item[1]
        elif 'wax_worker_link' in item:
            response['WAX']['worker_link'] = item[1]
        elif 'wax_tlg_link' in item:
            response['WAX']['tlg_link'] = item[1]

        elif 'hive_tlg' in item:
            response['HIVE']['tlg'] = item[1]
        elif 'hive_worker' in item:
            response['HIVE']['worker'] = item[1]
        elif 'hive_worker_percent' in item:
            response['HIVE']['worker_percent'] = item[1]
        elif 'hive_tlg_percent' in item:
            response['HIVE']['tlg_percent'] = item[1]
        elif 'hive_worker_link' in item:
            response['HIVE']['worker_link'] = item[1]
        elif 'hive_tlg_link' in item:
            response['HIVE']['tlg_link'] = item[1]

        elif 'atom_tlg' in item:
            response['ATOM']['tlg'] = item[1]
        elif 'atom_worker' in item:
            response['ATOM']['worker'] = item[1]
        elif 'atom_worker_percent' in item:
            response['ATOM']['worker_percent'] = item[1]
        elif 'atom_tlg_percent' in item:
            response['ATOM']['tlg_percent'] = item[1]
        elif 'atom_worker_link' in item:
            response['ATOM']['worker_link'] = item[1]
        elif 'atom_tlg_link' in item:
            response['ATOM']['tlg_link'] = item[1]

        elif 'steem_tlg' in item:
            response['STEEM']['tlg'] = item[1]
        elif 'steem_worker' in item:
            response['STEEM']['worker'] = item[1]
        elif 'steem_worker_percent' in item:
            response['STEEM']['worker_percent'] = item[1]
        elif 'steem_tlg_percent' in item:
            response['STEEM']['tlg_percent'] = item[1]
        elif 'steem_worker_link' in item:
            response['STEEM']['worker_link'] = item[1]
        elif 'steem_tlg_link' in item:
            response['STEEM']['tlg_link'] = item[1]
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


def select_const():
    connection = None
    try:
        connection = psycopg2.connect(
            host=config.GENERAL['psql_host'], 
            database=config.GENERAL['psql_database'], 
            user=config.GENERAL['psql_user'], 
            password=config.GENERAL['psql_password']
        )
        cursor = connection.cursor()
        sql = "SELECT c_name, c_value FROM const ORDER BY c_id ASC;"
        cur.execute(sql)
        result = cursor.fetchall()
        return result
    except (Exception, psycopg2.DatabaseError) as e:
        str_log = f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} select_const(): {e}"
        print(str_log)
    finally:
        if connection is not None:
            connection.close()


if __name__ == '__main__':
    serve(app, host=config.GENERAL['ip'], port=config.GENERAL['port'])
