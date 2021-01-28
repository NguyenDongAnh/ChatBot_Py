file_company_name = open(r'/ChatBot_Py/Crawl_data/s.cafef/list_company_name.txt','r+', encoding="utf-8")
file_stock_code = open(r'/ChatBot_Py/Crawl_data/s.cafef/list_stock_code.txt','r+',encoding='utf-8')
file_stock_keyword = open(r'/ChatBot_Py/Bot/keyword/stock_keyword.json','w+',encoding='utf-8')

list_company_name = file_company_name.read().split("\n")
list_stock_code = file_stock_code.read().split("\n")

print(len(list_company_name))


# intents = """{
#     "tag": "{}",
#     "patterns": [
#         {},
#         {}
#     ],
#     "responses": [
#         {}
#     ]
# },""".format(list_stock_code[0],list_stock_code[0],list_company_name[0],list_stock_code[0])

intents = """{{
    "tag": "{}",
    "patterns": [
        "{}",
        "{}"
    ],
    "responses": [
        "{}"
    ] 
}},"""

print(intents)
# print(list_company_name[0])
file_stock_keyword.write("""{\n"intents":[""")
for i in range (10):
    file_stock_keyword.write(intents.format(list_stock_code[i],list_stock_code[i],list_company_name[i],list_stock_code[i])+'\n')
file_stock_keyword.write("""\n]\n}""")
