import json
import pymongo
from mongo import *
from curs import *
from func import *
import time

link = "mongodb+srv://admin:1@johny.qluh3.mongodb.net/testDB?retryWrites=true&w=majority"
client = pymongo.MongoClient(link, serverSelectionTimeoutMS=9000)
db = client.testDB
collection = db["testCollection"]
user = 'apuUo-UF6yhfoNVVTKWrb5Z8ecru:'
link1 = 'https://partners-api.999.md/adverts/'

while True:

    time.sleep(5) # verification period sec.

    # track_file() # recording the result

    with open("track_f.json", "r") as f: # opening for comparison 
        text_data4 = json.load(f) 

    with open("data5.json", "r") as d: # opening for comparison
        text_data5 = json.load(d) 


    if text_data4 == text_data5:
        print('ok')
    if text_data4 != text_data5:
        full_adv()
    if text_data4 != text_data5:
        loadDB()
    if text_data4 != text_data5:
        data_5()


