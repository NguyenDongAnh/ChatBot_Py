from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import socketio
import sys,json
import numpy as np
sys.path.append(r'H:\ChatBot\Bot')
sys.path.append(r'H:\ChatBot\Algorithm')
# import training_bot
from chat import bot_message
from MaxFlow import Graph

###############################
app = Flask(__name__,static_url_path='',static_folder="H:/ChatBot/web_chat/static")
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

##############################

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))

@socketio.on('connect')
def test_connect():
    emit("new message",{'message' : 'Chào bạn, muốn biết mình có thể làm gì thì gõ \"help\" nhé !','tag':""})

@socketio.on('disconnect')
def disconect():
    print("user disconneted!")

@socketio.on('reconnect')
def reconnect():
    print("user reconnected!")

@socketio.on('input')
def input_message(data):
    print(data["data"])
    tag,message = bot_message(data["data"])
    emit("new message",{'message' : message,'tag':tag})

@socketio.on('input_N')
def input_N(data):
    try:
        N = int(data['data'])
        check = True
    except:
        emit("input_N",{'message' : 'Bạn nhập sai rồi, vui lòng nhập lại:','tag':"max_flow"})
        check = False
    if(check):
        emit("input_N",{'message' : 'Nhập dữ liệu cho lần lượt từng hàng của ma trận nhé, mỗi số cách nhau \" \" nhé, hông mình không tính được đâu:','tag':"input_row", 'N':N})

@socketio.on('input_row')
def input_row(data):
    if(int(data['count'])<int(data['N'])):
        try:
            a = data['data'].split()
            if(len(a)!= int(data['N'])): raise Exception()
            emit("input_row",{'message' : '','tag':"input_row",'count':'1','row':a})
        except:
            emit("input_row",{'message' : 'Bạn nhập sai rồi, vui lòng nhập lại','tag':"input_row"})
    if(int(data['count'])==int(data['N'])):
        graph = np.array(data['graph']).astype(int)
        graph = np.array(graph).reshape(int(data['N']),int(data['N']))
        emit("input_row",{'message' : 'Kết quả luồng cực đại là: {}'.format(Graph(graph).FordFulkerson(0,int(data['N'])-1)),'tag':"new message"})

################################
if __name__ == '__main__':
    socketio.run(app,host = "192.168.2.170", port = 3000, debug=True)
