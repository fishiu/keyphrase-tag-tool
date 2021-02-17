from flask import Flask
from flask import request, jsonify, render_template
from db.db_util import *

app = Flask(__name__)
db_util = DbUtil()


@app.route('/')
def article():
    return render_template('index.html')


@app.route('/get_record')
def get_record():
    record_id = request.args.get('record_id')
    record_info = db_util.get_record(record_id)
    return jsonify(record_info)


@app.route('/upload_record', methods=["POST"])
def upload_record():
    tagged_label = request.form.get('tag_kp')
    record_id = request.form.get('record_id')
    print(record_id, tagged_label)
    if any(tagged_label):
        db_util.modify_kp_tag(record_id, tagged_label)
    else:
        print("any skip")
    return jsonify({"code": 0})


if __name__ == '__main__':
    app.run()
