from flask import Flask, redirect, url_for, request
from flask import render_template

app = Flask(__name__)
def checkAuth(name,password):
    if(name == 'anket11' and password == '123'):
        return True
    else:
        return False

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       name = request.form.get("name")
       # getting input with name = lname in HTML form
       password = request.form.get("password")
       valid = checkAuth(name,password)
       if(valid):
                return 'Welcome ' + name 
       else:
          return 'Incorrect Username or Password' 
    return render_template("index.html")

	

if __name__ == '__main__':
	app.run(debug=True)
