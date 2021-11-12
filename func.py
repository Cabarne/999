import requests
import json


user = 'apuUo-UF6yhfoNVVTKWrb5Z8ecru:'
link1 = 'https://partners-api.999.md/adverts/'

resp = requests.get('https://partners-api.999.md/adverts/', auth=(user, ''))
data = resp.json()
def full_adv():
    with open('full_adverts.json', 'w') as f:
        json.dump(data, f, indent=4)


def load(): # read file
        with open("full_adverts.json", "r", encoding='utf-8-sig') as file_read:
                data = json.load(file_read)
        return(data)
a = load() 

def id_list(): # data id adverts
        res = []
        for i in a["adverts"]:
                res.append(i["id"]) 
        return res
t = id_list()  


def track_file(): # get file for tracking

        list_data2 = []
    
        for adver in range (0, 13):

                siteExtension = t[adver] # add adverts id 

                res = requests.get(link1 + siteExtension, auth=(user, ''))

                dat_4 = res.json()

                list_data2.append(dat_4)
                                   
        with open("track_f.json", "w") as f:
                json.dump(list_data2, f, indent=4)
        list_data2 = []
# track_file()

def data_5(): # file rec if there were changes on the site

        list_data5 = []

        for adver in range (0, 13):

                siteExtension = t[adver] # add adverts id 

                resp = requests.get(link1 + siteExtension, auth=(user, ''))

                dat5 = resp.json()

                list_data5.append(dat5)
            
                            
        with open('data5.json', 'w') as f:
                json.dump(list_data5, f, indent=4)




