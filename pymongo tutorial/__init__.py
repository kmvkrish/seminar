from pymongo import MongoClient
import datetime

class connect():
    def __init__(self,client,port):
        self.client = client
        self.port = port

    def get_param(self):
        return self.client,self.port

    def get_connect(self):
        return MongoClient(self.client,self.port)

    def get_database(self,connobj,database):
        return connobj[database]

    def get_collection(self,dbobj,collection):
        return dbobj[collection]

    def fetchRecord(self,collobj,slug):
        return collobj.find_one({"slug":slug})

    def fetchAll(self,collobj):
        return collobj.find()

    def deletePost(self,collobj,slug):
        return collobj.remove({"slug":slug})

    def insertPost(self,collobj,title,slug,body,comments=[]):
        return collobj.insert({"title":title,"slug":slug,"body":body,"comments":comments})

if __name__ == '__main__':
    mongo = connect("localhost",27017)
    print mongo
    connect = mongo.get_connect()
    print connect
    database = mongo.get_database(connect,'my_tumble_log')
    print database
    collection = mongo.get_collection(database,'post')
    print collection
    posts = mongo.fetchAll(collection)
    for post in posts:
        print post['title']
    insert = mongo.insertPost(collection,"I have got an offer for Data Scientist","i-have-got-an-interview-for-data-scirntist","Welcome to all!. I have got an interview call for data scientist position",[])
    print insert
