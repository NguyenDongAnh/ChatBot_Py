import re
file_company_name = open(r'/ChatBot_Py/Crawl_data/s.cafef/list_company_name.txt','r+', encoding="utf-8")
file_stock_code = open(r'/ChatBot_Py/Crawl_data/s.cafef/list_stock_code.txt','r+',encoding='utf-8')
file_stock_keyword = open(r'/ChatBot_Py/Bot/keyword/stock_keyword.json','w+',encoding='utf-8')

list_company_name = file_company_name.read().split("\n")
list_stock_code = file_stock_code.read().split("\n")

print(len(list_company_name))

intents = """{{
    "tag": "{}",
    "patterns": [
        "{}",
        "{}",
        "{}"
    ],
    "responses": [
        "{}"
    ],
    "name_company": [
        "{}"
    ]
}},"""
intents_last = """{{
    "tag": "{}",
    "patterns": [
        "{}",
        "{}",
        "{}"
    ],
    "responses": [
        "{}"
    ],
    "name_company": [
        "{}"
    ]
}}"""
n = len(list_company_name)
# n = 30
file_stock_keyword.write("""{\n"intents":[""")
for i in range (n-1):
    if(re.search(r"\((.*?)\)",list_company_name[i])):
        str1 = re.findall(r"\((.*?)\)",list_company_name[i])[0]
        str2 = re.split(r"\(",list_company_name[i])[0]
        file_stock_keyword.write(intents.format(list_stock_code[i],list_stock_code[i],str2,str1,list_stock_code[i],str2)+'\n')
    else:
        file_stock_keyword.write(intents.format(list_stock_code[i],list_stock_code[i],list_company_name[i],'',list_stock_code[i],str2)+'\n')

if(re.search(r"\((.*?)\)",list_company_name[n-1])):
    str1 = re.findall(r"\((.*?)\)",list_company_name[n-1])[0]
    str2 = re.split(r"\(",list_company_name[n-1])[0]
    file_stock_keyword.write(intents_last.format(list_stock_code[n-1],list_stock_code[n-1],str2,str1,list_stock_code[n-1],str2))
else:
    file_stock_keyword.write(intents_last.format(list_stock_code[n-1],list_stock_code[n-1],list_company_name[n-1],'',list_stock_code[n-1],str2))
file_stock_keyword.write("""\n]\n}""")
 