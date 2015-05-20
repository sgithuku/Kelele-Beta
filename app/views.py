#all imports
from app import app
from flask import (
    Flask,
    redirect,
    render_template,
    request,
    url_for,
)

from flask.ext.stormpath import (
    StormpathManager,
    User,
    login_required,
    login_user,
    logout_user,
    user,
)

# Import our forms, son
from forms import Locate
from forms import Intro



#set up Stormpath credentials
app.config['SECRET_KEY'] = 'NotifyMe2014@friends'
app.config['STORMPATH_API_KEY_FILE'] = '~/apiKey.properties'
app.config['STORMPATH_APPLICATION'] = 'Stormpath'


# Get stormpath going
stormpath_manager = StormpathManager()
# some code which creates your app
stormpath_manager.init_app(app)

# These are our routes

@app.route('/')
def index():
    user_form = Intro(request.form, prefix="user-form")
    if user_form.validate_on_submit():

        # Your Account Sid and Auth Token from twilio.com/user/account
        account_sid = "AC0a825469aff4344dbf604f43ac9c2e39"
        auth_token  = "553bcc1ed54215ddc5739976ac6c7667"
        client = TwilioRestClient(account_sid, auth_token)
         
        message = client.sms.messages.create(body="Hi "+user.custom_data['contact_name1']+", "+ user.given_name+" just had an accident at "+user_form.location.data+" and may need your help.",
            to=user.custom_data['phone_number1'],    # Replace with your phone number
            from_="+16173000474") # Replace with your Twilio number
        message = client.sms.messages.create(body="Hi "+user.custom_data['contact_name2']+", "+ user.given_name+" just had an accident at "+user_form.location.data+" and may need your help.",
            to=user.custom_data['phone_number2'],    # Replace with your phone number
            from_="+16173000474") # Replace with your Twilio number
        print message.sid
        return redirect('/success')
    return render_template("intro.html",userform=user_form)

@app.route('/success')
def success():
	return render_template("success.html")
