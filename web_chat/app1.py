from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit
import socketio
import sys,json
import numpy as np
sys.path.append(r'/ChatBot_Py/Bot')
sys.path.append(r'/ChatBot_Py/Algorithm')
# import training_bot
from chat import bot_message,catch_stock_keyword,catch_time_keyword
from MaxFlow import Graph

file_stock_code = open(r'/ChatBot_Py/Crawl_data/s.cafef/list_stock_code.txt','r+')
list_stock_code = file_stock_code.read().split('\n')
###############################
app = Flask(__name__,static_url_path='',static_folder="/ChatBot_Py/web_chat/static")
# static_files = {
#     '/': 'latency.html',
#     '/static/socket.io.js': 'static/socket.io.js',
#     '/static/style.css': 'static/style.css',
# }
app.config.from_mapping(
    TESTING=True,
    SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/',
    ENV = 'development',
    CORS_HEADERS = 'Content-Type',
)
socketio = SocketIO(app)

##################################

@app.route('/',methods=['GET', 'POST'])
def chat():
    return render_template('chatmessage.html')

@app.route('/api/chat/<msg>',methods=['GET','POST'])
def api_chat(msg):
    # print(msg)
    records,name_company,message= bot_message(msg)
    if(records != None):
        return jsonify(records=records,name_company=name_company,message=message)
    return jsonify(records=[])
@app.route('/api/stockcode',methods=['GET'])
def api_stockcode():
    return jsonify(stock_code=list_stock_code)

################################
if __name__ == '__main__':
    socketio.run(app,host = "0.0.0.0", port = 3200, debug=True)