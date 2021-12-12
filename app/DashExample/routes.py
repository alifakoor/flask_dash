import datetime
import pytz
from . import blueprint
from flask import render_template, request, redirect, current_app, jsonify
from flask_login import login_required, current_user
from .forms import AddDataForm
from ..base.models import User, Temperature, PH, EC, ORP, Ammonia, Nitrite, Nitrate, Oxygen
from Dashboard import Dash_App1, Dash_App2


@blueprint.route('/app1')
@login_required
def app1_template():
    return render_template('app1.html', dash_url = Dash_App1.url_base)


@blueprint.route('/app2')
@login_required
def app2_template():
    return render_template('app2.html', dash_url = Dash_App2.url_base)


@blueprint.route('/add_data', methods=['GET', 'POST'])
@login_required
def add_data():
    admin_user = current_app.config['ADMIN']['username']
    if current_user.username == admin_user:
        form = AddDataForm(request.form, meta={'csrf': False})
        status = ''
        if request.method == 'POST':
            if form.validate():
                temperature = {
                    'value': request.form.get('temperature'),
                    'timestamp': datetime.datetime.now(pytz.timezone('Asia/Tehran')),
                    'user_id': current_user.id
                }
                ph = {
                    'value': request.form.get('ph'),
                    'timestamp': datetime.datetime.now(pytz.timezone('Asia/Tehran')),
                    'user_id': current_user.id
                }
                ec = {
                    'value': request.form.get('ec'),
                    'timestamp': datetime.datetime.now(pytz.timezone('Asia/Tehran')),
                    'user_id': current_user.id
                }
                orp = {
                    'value': request.form.get('orp'),
                    'timestamp': datetime.datetime.now(pytz.timezone('Asia/Tehran')),
                    'user_id': current_user.id
                }
                ammonia = {
                    'value': request.form.get('ammonia'),
                    'timestamp': datetime.datetime.now(pytz.timezone('Asia/Tehran')),
                    'user_id': current_user.id
                }
                nitrite = {
                    'value': request.form.get('nitrite'),
                    'timestamp': datetime.datetime.now(pytz.timezone('Asia/Tehran')),
                    'user_id': current_user.id
                }
                nitrate = {
                    'value': request.form.get('nitrate'),
                    'timestamp': datetime.datetime.now(pytz.timezone('Asia/Tehran')),
                    'user_id': current_user.id
                }
                oxygen = {
                    'value': request.form.get('oxygen'),
                    'timestamp': datetime.datetime.now(pytz.timezone('Asia/Tehran')),
                    'user_id': current_user.id
                }
                Temperature(**temperature).add_to_db()
                PH(**ph).add_to_db()
                EC(**ec).add_to_db()
                ORP(**orp).add_to_db()
                Ammonia(**ammonia).add_to_db()
                Nitrite(**nitrite).add_to_db()
                Nitrate(**nitrate).add_to_db()
                Oxygen(**oxygen).add_to_db()
                status = 'All Good.'
            else:
                status = 'All field must be correct.'
        return render_template('add_data.html', form=form, status=status)
    return redirect('/page_403')
