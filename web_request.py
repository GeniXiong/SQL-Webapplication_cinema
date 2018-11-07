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
	return render_template('index.html', content = '')

@app.route('/selection', methods = ['POST', 'GET'])
def select_cinema():
    return render_template("index.html", content = [{'num':'1','url':'movie/1.jpg'},{'num':'2','url':'movie/2.jpg'},{'num':'3','url':'movie/3.jpg'}])
   # if request.method == 'POST':
   #     received_data = request.form
   #     if 'rate' in received_data:
   #         rate = received_data['rate']
   #     else:
   #         rate = 0
   #     if 'date' in received_data:
   #         date = request.form['date']
   #     else:
   #         date = ''
   #     if 'type' in received_data:
   #         m_type = request.form['type']
   #     else:
   #         m_type = ''
   #     if 'price' in received_data:
   #         price = request.form['price']
   #     else:
   #         price = 0
   #
   #     result_list = con.check_movie(date, m_type, rate, price)
   #     #result_list = [date, m_type, rate, price]
   #     return render_template("index.html", content = return_list)
   # return ''

@app.route('/movie')
def movie_detail():
    #schedule_list = find_schedule(movie)
    return render_template('movie_detail.html')

@app.route('/special_date')
def special_date():
    return render_template('special_date.html')


if __name__ == '__main__':
    app.run()