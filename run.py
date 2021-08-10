# imports
import sys
import pip
try:
    from flask import Flask, render_template, redirect
    from flask_wtf import FlaskForm
    from wtforms import SubmitField, TextAreaField, SelectField
    from wtforms.fields.simple import TextAreaField
    from wtforms.validators import data_required
    from gtts import gTTS

except:
    choice = input('''This application need some additional packages
    do you want to install them? (y/n)''')

    if choice=='y' or choice=='Y':
    # installing additional packages
        print('Installing...')
        pip.main(['install','flask', 'flask-wtf', 'gTTS'])
    else: 
        print('Aborting...')

finally:
    #imports
    from flask import Flask, render_template, redirect
    from flask_wtf import FlaskForm
    from wtforms import SubmitField, TextAreaField, SelectField
    from wtforms.fields.simple import TextAreaField
    from wtforms.validators import data_required
    from gtts import gTTS

    # configaretion
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '#include<iostream>'

    # form models
    class InputForm(FlaskForm):
        voice = SelectField('Select voice', choices=['female', 'male'])
        speed = SelectField('speed', choices=['fast', 'slow'])
        text = TextAreaField('Input Text', validators=[data_required()])
        generate = SubmitField('generate')

    # app routes
    @app.route('/', methods=['GET', 'POST'])
    def index():
        filename=''
        extension=''     # default .mp3
        tts = ''
        form = InputForm()
        if form.validate_on_submit():
            filename = 'output'
            # data binding
            tts = gTTS(form.text.data, slow = (form.speed.data == 'slow'))
            tts.save('./static/'+filename+'.mp3')     # default .mp3

            redirect('index.html')

        return render_template('index.html', form = form, output=filename)

    # entry point
    if __name__ == '__main__':
        app.run(debug = True)