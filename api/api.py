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
    return 'Home Page'


@app.route('/api/auth/register', methods=['POST'])
def register():
    name = 'User name'
    email = 'User email'
    password = 'User password'
    user = User()
    user.register(name, email, password)
    return jsonify(user.get_name())


@app.route('/api/auth/login', methods=['POST'])
def login():
    user = User()
    return user.login()


@app.route('/api/auth/logout', methods=['POST'])
# this should be changed to a POST request after, using GET for now
def logout():
    user = User()
    return user.logout()


# reset password

@app.route('/api/auth/reset-password', methods=['POST'])
def reset_password():
    new_password = 'updated password'
    user = User()
    user.reset_pass(new_password)
    return jsonify(user.get_name())


# register a business or get all businesses

@app.route('/api/businesses', methods=['POST', 'GET'])
def handle_business():
    if request.method == 'GET':
        business = Business()
        data = business.getAll()
        return jsonify(data)
    else:
        name = 'some business name'
        location = 'the business location'
        services = 'services offered'
        business = Business()
        business.register_business(name, location, services)
        data = business.getAll()
        if data:
            return jsonify(data)
        return 'No data'


# update a business or remove a business or get a business


@app.route('/api/businesses/<int:businessid>', methods=['PUT', 'DELETE', 'GET'])
def handle_business_profile(businessid):
    if request.method == 'GET':
        business = Business()
        data = business.getOne()
        return jsonify(data)
    elif request.method == 'PUT':
        name = 'some business name'
        location = 'updated location'
        services = 'updated services'
        new_business = Business()
        new_business.update_business(name, location, services)
        return jsonify(new_business.getAll())
    else:
        name = 'some business name'
        business = Business()
        business.delete_business(name)
        return jsonify(business.getAll())


# review a business or get all reviews for a business


@app.route('/api/businesses/<int:businessid>/reviews', methods=['POST', 'GET'])
def test():
    pass
