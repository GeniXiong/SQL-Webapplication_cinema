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

@app.route('/selection', methods = ['POST'])
def select_cinema():
   if request.method == 'POST':
       received_data = request.form
       if 'rate' in received_data:
           rate = received_data['rate']
       else:
           rate = ''
       date = request.form['date']
       m_type = request.form['type']
       price = request.form['price']
       result_list = con.check_movie(date, m_type, rate, price)
       #result_list = [date, m_type, rate, price]
       return render_template("index.html", content = result_list)
   return ''
    
    
if __name__ == '__main__':
    app.run()