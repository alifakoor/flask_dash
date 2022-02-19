import datetime
import pytz
from . import blueprint
from flask import request, jsonify, current_app
from flask_login import login_user, login_required, current_user
from ..base.models import User, Temperature, PH, EC, ORP, Ammonia, Nitrite, Nitrate, Oxygen


@blueprint.route('/login', methods=['POST'])
def api_login():
    username = request.form['username']
    password = request.form['password']
    if request.method == 'POST':
        user = User.query.filter_by(username=username).first()
        if user:
            if user.checkpw(password):
                login_user(user)
                return jsonify({
                            "success": True,
                            "message": "You logged in successfully.",
                            "data": {
                                "id": user.id,
                                "username": user.username
                            }
                        })
            else:
                return jsonify({
                            "success": False,
                            "message": "Password is not correct."
                        })
        else:
            return jsonify({
                        "success": False,
                        "message": "Username is not correct."
                    })
    return jsonify({
        "success": False,
        "message": "Please Login."
    })


@blueprint.route('/add_data', methods=['POST'])
# @login_required
def add_data():
    # admin_user = current_app.config['ADMIN']['username']
    success = False
    message = "You are not login."
    # if current_user.username == admin_user:

    if request.method == 'POST':
        # if validator(request):
        #
        #
        # else:
        #     message = "Data is not correct."

        temperature = {
            'value': request.form.get('temperature'),
            'timestamp': datetime.datetime.now(pytz.timezone('Asia/Tehran')),
            'user_id': current_user.id
            # 'user_id': 1
        }
        ph = {
            'value': request.form.get('ph'),
            'timestamp': datetime.datetime.now(pytz.timezone('Asia/Tehran')),
            'user_id': current_user.id
            # 'user_id': 1
        }
        ec = {
            'value': request.form.get('ec'),
            'timestamp': datetime.datetime.now(pytz.timezone('Asia/Tehran')),
            'user_id': current_user.id
            # 'user_id': 1
        }
        orp = {
            'value': request.form.get('orp'),
            'timestamp': datetime.datetime.now(pytz.timezone('Asia/Tehran')),
            'user_id': current_user.id
            # 'user_id': 1
        }
        ammonia = {
            'value': request.form.get('ammonia'),
            'timestamp': datetime.datetime.now(pytz.timezone('Asia/Tehran')),
            'user_id': current_user.id
            # 'user_id': 1
        }
        nitrite = {
            'value': request.form.get('nitrite'),
            'timestamp': datetime.datetime.now(pytz.timezone('Asia/Tehran')),
            'user_id': current_user.id
            # 'user_id': 1
        }
        nitrate = {
            'value': request.form.get('nitrate'),
            'timestamp': datetime.datetime.now(pytz.timezone('Asia/Tehran')),
            'user_id': current_user.id
            # 'user_id': 1
        }
        oxygen = {
            'value': request.form.get('oxygen'),
            'timestamp': datetime.datetime.now(pytz.timezone('Asia/Tehran')),
            'user_id': current_user.id
            # 'user_id': 1
        }

        Temperature(**temperature).add_to_db()
        PH(**ph).add_to_db()
        EC(**ec).add_to_db()
        ORP(**orp).add_to_db()
        Ammonia(**ammonia).add_to_db()
        Nitrite(**nitrite).add_to_db()
        Nitrate(**nitrate).add_to_db()
        Oxygen(**oxygen).add_to_db()

        success = True,
        message = "Data has been saved successfully."
    else:
        message = "Request method is not correct."

    return jsonify({
        "success": success,
        "message": message
    })


def validator(request):
    err = False
    for key, value in request.form.items():
        # if not type(value) is float:
        #     err = True
        #     break

        if key == 'temperature':
            if not float(value) >= 0 or not float(value) <= 50:
                err = True
                break

        if key == 'ph':
            if not float(value) >= 0 or not float(value) <= 14:
                err = True
                break

        if key == 'ec':
            if not float(value) >= 0 or not float(value) <= 4000:
                err = True
                break

        if key == 'orp':
            if not float(value) >= 0 or not float(value) <= 400:
                err = True
                break

        if key == 'ammonia':
            if not float(value) >= 0 or not float(value) <= 2000:
                err = True
                break

        if key == 'nitrite':
            if not float(value) >= 0 or not float(value) <= 50:
                err = True
                break

        if key == 'nitrate':
            if not float(value) >= 0 or not float(value) <= 50:
                err = True
                break

        if key == 'oxygen':
            if not float(value) >= 0 or not float(value) <= 100:
                err = True
                break

    return not err
