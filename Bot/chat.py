import sys
sys.path.append(r'/ChatBot_Py/Bot/keyword')
sys.path.append(r'/ChatBot_Py/Crawl_data/database')
from model import NeuralNet_time as nnet_t
from model import NeuralNet_stock as nnet_st
from model import NeuralNet as nnet
import random
import json
import torch
import re
from nltk_utils import bag_of_words, tokenize, bag_of_words1
from flask_socketio import emit
from db import db, cursor, Error
# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
device = torch.device('cpu')
with open(r'/ChatBot_Py/Bot/intents.json', 'r', encoding='utf8') as json_data:
    intents = json.load(json_data)

with open(r'/ChatBot_Py/Bot/keyword/stock_keyword.json', 'r', encoding='utf8') as json_data:
    intents_stock_keyword = json.load(json_data)

with open(r'/ChatBot_Py/Bot/keyword/time_keyword.json', 'r', encoding='utf8') as json_data:
    intents_time_keyword = json.load(json_data)

# print(intents_stock_keyword)
FILE = r"/ChatBot_Py/Bot/data.pth"
FILE_STOCK_KEYWORD = r"/ChatBot_Py/Bot/data_stock_keyword.pth"
FILE_TIME_KEYWORD = r"/ChatBot_Py/Bot/data_time_keyword.pth"


data = torch.load(FILE)
data_stock_keyword = torch.load(FILE_STOCK_KEYWORD)
data_time_keyword = torch.load(FILE_TIME_KEYWORD)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = nnet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

# print(model)

input_size_stock_keyword = data_stock_keyword["input_size"]
hidden_size_stock_keyword = data_stock_keyword["hidden_size"]
output_size_stock_keyword = data_stock_keyword["output_size"]
all_words_stock_keyword = data_stock_keyword['all_words']
tags_stock_keyword = data_stock_keyword['tags']
model_state_stock_keyword = data_stock_keyword["model_state"]

model_stock_keyword = nnet_st(
    input_size_stock_keyword, hidden_size_stock_keyword, output_size_stock_keyword).to(device)
model_stock_keyword.load_state_dict(model_state_stock_keyword)
model_stock_keyword.eval()

# print(model_stock_keyword)

input_size_time_keyword = data_time_keyword["input_size"]
hidden_size_time_keyword = data_time_keyword["hidden_size"]
output_size_time_keyword = data_time_keyword["output_size"]
all_words_time_keyword = data_time_keyword['all_words']
tags_time_keyword = data_time_keyword['tags']
model_state_time_keyword = data_time_keyword["model_state"]

model_time_keyword = nnet_t(
    input_size_time_keyword, hidden_size_time_keyword, output_size_time_keyword).to(device)
model_time_keyword.load_state_dict(model_state_time_keyword)
model_time_keyword.eval()

# print(model_time_keyword)
# bot_name = "Sam"
# print("Let's chat! (type 'quit' to exit)")
# while True:
#     sentence = input("You: ")
#     if sentence == "quit":
#         break

#     sentence = tokenize(sentence)
#     X = bag_of_words(sentence, all_words)
#     X = X.reshape(1, X.shape[0])
#     X = torch.from_numpy(X).to(device)

#     output = model(X)
#     _, predicted = torch.max(output, dim=1)

#     tag = tags[predicted.item()]

#     probs = torch.softmax(output, dim=1)
#     prob = probs[0][predicted.item()]
#     if prob.item() > 0.9:
#         for intent in intents['intents']:
#             if tag == intent["tag"]:
#                 print(f"{bot_name}: {random.choice(intent['responses'])}")
#     else:
#         print(f"{bot_name}: Tôi không hiểu bạn nói gì.")

# def bot_message(sentence):
#     sentence = tokenize(sentence)
#     X = bag_of_words(sentence, all_words)
#     X = X.reshape(1, X.shape[0])
#     X = torch.from_numpy(X).to(device)


#     output = model(X)

#     _, predicted = torch.max(output, dim=1)

#     tag = tags[predicted.item()]

#     probs = torch.softmax(output, dim=1)
#     prob = probs[0][predicted.item()]
#     if prob.item() > 0.9:
#         for intent in intents['intents']:
#             if (tag == intent["tag"] and intent["tag"] == "help" ):
#                 for res in intent['responses']:
#                     emit('new message',{'message':res,'tag':tag})
#                 return tag,""
#             elif (tag == intent["tag"] and intent["tag"] == "max_flow" ):
#                 return tag,random.choice(intent['responses'])
#             elif tag == intent["tag"]:
#                 return tag,random.choice(intent['responses'])
#     else:
#         return "unknown","Tôi không hiểu bạn nói gì."
# def bot_message(sentence):
#     keyword1 = catch_stock_keyword(sentence)
#     keyword2 = catch_time_keyword(sentence)
    
#     return "message", "keyword1 :" + keyword1 + "<br>"+"keyword2 :" + keyword2


def bot_message(sentence):
    keyword1,name_company = catch_stock_keyword(sentence)
    keyword2,message = catch_time_keyword(sentence)
    if(keyword1 != "None"):
        try:
            sql_select_Query = f"select * from {keyword1} where NGAY between date_sub(now(),INTERVAL 1 {keyword2}) and now() ORDER BY NGAY DESC;"
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            print(records)
            print("Total number of rows in AAA is: ", cursor.rowcount)
            print("+---------------------------------------------+")
            print("| NGAY        | GIA DIEU CHINH | GIA DONG CUA |")
            for row in records:
                print("|",row[0]," "*(9-len(str(row[0]))),
                    "|",row[1]," "*(13-len(str(row[1]))),
                    "|",row[2]," "*(11-len(str(row[2]))),"|")
            print("+---------------------------------------------+")
        except Error as e:
            print("Error reading data from MySQL table", e)
            return [],"",""
        # finally:
        #     if (db.is_connected()):
        #         cursor.close()
        #         db.close()
        #         print("MySQL connection is closed !")
        return records,name_company,message
    return [],"",""

# def bot_message(sentence):
#     keyword1, name_company = catch_stock_keyword(sentence)
#     keyword2 = catch_time_keyword(sentence)
#     return "message", keyword1, keyword2
def catch_stock_keyword(sentence):
    if(re.search(r"aaa\b",sentence.lower())):
        return "AAA","Công ty Cổ phần Nhựa An Phát Xanh"
    if(re.search(r"aam\b",sentence.lower())):
        return "AAM","Công ty Cổ phần Thủy sản Mekong"
    if(re.search(r"abs\b",sentence.lower())):
        return "ABS","Công ty Cổ phần nông nghiệp Bình Thuận"
    if(re.search(r"abt\b",sentence.lower())):
        return "ABT","Công ty Cổ phần Xuất nhập khẩu Thủy sản Bến Tre"
    if(re.search(r"acb\b",sentence.lower())):
        return "ACB","Ngân hàng Thương mại Cổ phần Á Châu"
    else:
        sentence = tokenize(sentence)
        X = bag_of_words(sentence, all_words_stock_keyword)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model_stock_keyword(X)

        _, predicted = torch.max(output, dim=1)
        # print(predicted.item())
        tag = tags_stock_keyword[predicted.item()]
        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        # print(prob.item())
        if prob.item() > 0.95:
            for intent in intents_stock_keyword['intents']:
                if tag == intent["tag"]:
                    return random.choice(intent['responses']),random.choice(intent['name_company'])
        else:
            return "None","None"


def catch_time_keyword(sentence):
    sentence = tokenize(sentence)
    X = bag_of_words1(sentence, all_words_time_keyword)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model_time_keyword(X)

    print(intents_time_keyword['intents'][0]['responses'][0])

    _, predicted = torch.max(output, dim=1)
    # print(predicted.item())
    tag = tags_time_keyword[predicted.item()]
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    print(prob.item())
    if prob.item() > 0.97:
        for intent in intents_time_keyword['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses']),intent['message']
    return intents_time_keyword['intents'][0]['responses'][0],intents_time_keyword['intents'][0]['message']
