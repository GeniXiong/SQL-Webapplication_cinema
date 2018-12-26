# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, url_for, render_template, request
import connector as con

app = Flask(__name__)

# =============================================================================
# root address to show the fancy webpage design for cinema schedule
# ip address: http://127.0.0.1:5000/ 
# =============================================================================
@app.route('/')
def index():
	return render_template('movie_detail.html', content = '')

@app.route('/selection', methods = ['POST', 'GET'])
def select_cinema():
    return render_template("index.html", content = [{'num':'1','url':'movie/1.jpg'},{'num':'2','url':'movie/2.jpg'},{'num':'3','url':'movie/3.jpg'}])


#display every movie detail
@app.route('/movie', methods = ['POST', 'GET'])
def movie_detail():
    detail = {}
    if request.method == 'POST':
        mid = request.form['movie_id']
        detail = con.check_movie_detail(mid)
        print(detail)
    return render_template('movie_detail.html', content = detail)

@app.route('/special_date')
def special_date():
    return render_template('special_date.html')

@app.route('/test', methods = ['POST', 'GET'])
def print_date():
    received_data = request.form
    print (received_data)
    return render_template('special_date.html')

@app.route('/tes', methods = ['POST', 'GET'])
def test():
    return render_template("test1.html", content = [{'num':'1','url':'movie/1.jpg'},{'num':'2','url':'movie/2.jpg'},{'num':'3','url':'movie/3.jpg'}])

if __name__ == '__main__':
    app.run()