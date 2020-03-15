"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
 
from flask import render_template, request, redirect, url_for, flash
from app.forms import ProfileForm
from app.models import UserProfile
from app import db, app
from werkzeug.utils import secure_filename
import os 

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

@app.route('/profile', methods = ['GET', 'POST'])
def profile():
    """Render the website's profile page."""
    profileform= ProfileForm()
    if request.method=='POST' and profileform.validate_on_submit():
        firstname=profileform.firstname.data
        lastname=profileform.lastname.data
        gender=profileform.gender.data
        email=profileform.email.data
        location=profileform.location.data
        biography=profileform.biography.data
        photo =profileform.photo.data
        flash('Profile has been created', 'success')
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(
            app.config['UPLOAD_FOLDER'], filename
        ))

        userprofile=UserProfile(first_name=firstname,last_name=lastname, gender=gender, email=email,location=location, biography=biography, profilepic=filename)
        db.session.add(userprofile)
        db.session.commit()
        return redirect(url_for('profiles'))
    return render_template('profile.html', form=profileform)

@app.route('/profiles')
def profiles():
    """Render the website's profiles page."""
    userprofiles = UserProfile.query.all()
    return render_template('profiles.html', userprofiles=userprofiles)

@app.route('/profile/<userid>')
def loaduserprofile(userid):
    """Render an individual user profile by the specific user's id."""
    return render_template('loaduserprofile.html')


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
