#all imports
from app import app

from flask.ext.stormpath import StormpathManager

#set up Stormpath credentials
app.config['SECRET_KEY'] = 'NotifyMe2014@friends'
app.config['STORMPATH_API_KEY_FILE'] = '~/apiKey.properties'
app.config['STORMPATH_APPLICATION'] = 'Stormpath'


# Get stormpath going
stormpath_manager = StormpathManager()
# some code which creates your app
stormpath_manager.init_app(app)



@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"