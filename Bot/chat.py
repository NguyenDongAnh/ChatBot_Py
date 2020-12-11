import random
import json
import sys
import torch
# sys.path.append(r'H:\ChatBot\Bot')
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

from flask_socketio import emit
# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
device = torch.device('cpu')
with open(r'H:\ChatBot\Bot\intents.json', 'r',encoding='utf8') as json_data:
    intents = json.load(json_data)

FILE = r"H:\ChatBot\Bot\data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

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


device = torch.device('cpu')
with open(r'/ChatBot/Bot/intents.json', 'r',encoding='utf8') as json_data:
    intents = json.load(json_data)

FILE = r"/ChatBot/Bot/data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

def bot_message(sentence):
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.9:
        for intent in intents['intents']:
            if (tag == intent["tag"] and intent["tag"] == "help" ):
                for res in intent['responses']:
                    emit('new message',{'message':res,'tag':tag})
                return tag,""
            elif (tag == intent["tag"] and intent["tag"] == "max_flow" ):
                return tag,random.choice(intent['responses'])
            elif tag == intent["tag"]:
                return tag,random.choice(intent['responses'])
    else:
        return "unknown","Tôi không hiểu bạn nói gì."
