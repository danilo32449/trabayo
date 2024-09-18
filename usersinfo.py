import requests
import json

class usersinfo:

    def __init__(self):
        pass


    def getUsers(self):
        responseUser= requests.get("https://datos.gov.co/resource/jtnk-dmga.json")
        dataJson = responseUser.json()
        for ind in range(len(dataJson)):
            print (dataJson[ind]['email_address'])

    def validateUsers(self):
        for email inf self,listUsers:




prueba = usersinfo()
prueba.getUsers()









