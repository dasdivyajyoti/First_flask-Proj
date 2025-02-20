
from app_one.app_models import DataModel
from flask import request,jsonify
from flask import Flask

app = Flask(__name__)

@app.route('/info',methods=['POST'])

def post_data():

    # This method ensures csv file exist inside DataModel and receive information using post request

    try:
        DataModel.ensure_csv_exists()
        data = request.get_json(silent = True)
        if not data:
            return jsonify({"error": "No JSON data received"})

        if isinstance(data,dict):
            data = [data]
            DataModel.append_data(data)
            return jsonify({"message": "Data received and saved successfully!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500











