import os
import sys
from flask_migrate import Migrate
from configs.config import config_dict
from app import create_app, db

get_config_mode = os.environ.get('APP_CONFIG_MODE', 'Debug')

try:
    config_mode = config_dict[get_config_mode.capitalize()]
except KeyError:
    sys.exit('Error: Invalid APP_CONFIG_MODE environment variable entry.')

app = create_app(config_mode)
Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
