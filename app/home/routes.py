from . import blueprint
from flask import render_template
from flask_login import login_required, current_user
from Dashboard import Dash_App2


@blueprint.route('/')
@login_required
def index():
    # return render_template('index.html')
    return render_template('app1.html', dash_url=Dash_App2.url_base)