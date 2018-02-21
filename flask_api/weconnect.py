import os

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, Response, jsonify

from User import User

from Business import Business


app = Flask(__name__)
app.config.from_object(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.before_request
def before_request():
    method = request.form.get('_method', '').upper()
    if method:
        request.environ['REQUEST_METHOD'] = method
        assert request.method == method


@app.route('/')
def home():
    return 'hello'


@app.route('/api/auth/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register_user.html')
    else:
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        session['username'] = request.form.get('username')
        user = User(name, email, password)

        return render_template('home.html', name=name)


@app.route('/api/auth/login', methods=['POST'])
@app.route('/api/auth/logout', methods=['GET'])
# this should be changed to a POST request after, using GET for now
def logout():
    session.pop('username', None)

    return render_template('login.html')


# reset password

@app.route('/api/auth/reset-password', methods=['POST'])
def reset_password():
    return "Reset your password"


# register a business or get all businesses

@app.route('/api/businesses', methods=['POST', 'GET'])
def handle_business():
    if request.method == 'GET':

        return render_template('register_business.html')
    else:
        name = request.form.get('name')
        location = request.form.get('location')
        services = request.form.get('services')
        business = Business(name, location, services)
        data = business.getAll()
        if data:
            return render_template('register_business.html', data=data)
        return render_template('register_business.html')


# update a business or remove a business or get a business


@app.route('/api/businesses/<int:businessid>', methods=['PUT', 'DELETE', 'GET'])
def handle_business_profile(businessid):
    if request.method == 'GET':
        return render_template('business_profile.html')
    elif request.method == 'PUT':
        return 'Updating the business'
    else:
        return 'Deleting the business'

# review a business or get all reviews for a business


@app.route('/api/businesses/<int:businessid>/reviews', methods=['POST', 'GET'])
def test():
    pass
