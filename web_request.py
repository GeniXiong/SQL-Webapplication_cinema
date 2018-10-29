# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, url_for, render_template, request
import connector as con

app = Flask(__name__)

# =============================================================================
# root address to shwo the fancy webpage design for cinema schedule
# ip address: http://127.0.0.1:5000/ 
# =============================================================================
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login', methods = ['POST'])
def login():
    if con.check_login(request.form['username'] , request.form['password']):
        return('successful login!')
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    else:
        return('Failed, please try again!')
    
if __name__ == '__main__':
    app.run()