from flask import Flask, request, render_template, app
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']


class FirstName:
    pass


class LastName:
    pass


class Confirm:
    pass


class Password:
    pass


class ConfirmPassword:
    pass


@app.route('/signin', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['FirstName']
        username1 = request.form['LastName']
        password = request.form['password']
        password = request.form['ConfirmPassword']
        db.users.insert_one({'username': FirstName, 'username1':LastName , 'password': password, 'password1':ConfirmPassword})
        return 'User created successfully!'
    return render_template('registration.html')
if __name__ == "__main__":
    app.run()

