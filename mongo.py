import pymongo
import requests
from pymongo import MongoClient
from func import*
from curs import *

link = "mongodb+srv://admin:1@johny.qluh3.mongodb.net/testDB?retryWrites=true&w=majority"
client = pymongo.MongoClient(link, serverSelectionTimeoutMS=7000)

db = client.testDB

collection = db["testCollection"]

user = 'apuUo-UF6yhfoNVVTKWrb5Z8ecru:'
link1 = 'https://partners-api.999.md/adverts/'

########## New file json in DB ################

def loadDB():
        collection.drop()
        count = 1
        for adv in range (0, 13):

                siteExtension = t[adv] # add adverts id 
                r = requests.get(link1 + siteExtension, auth=(user, 'pass'))

                data = r.json()

                if data['price']['unit'] == 'eur':
                
                        data['price']['currencies'][2]['value'] = total_exchange * data['price']['currencies'][0]['value']
                
                        data['price']['value'] = total_exchange * data['price']['currencies'][0]['value']
        
                with open('convert.json',  'w') as f:
                        json.dump(data, f, indent=4)
                        post = collection.insert_one({"_id":count, "data": data}) 
                        count += 1
# loadDB()
##########################################





