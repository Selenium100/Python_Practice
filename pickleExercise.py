# import requests
# import pickle
#
# res = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
# list = res.text.split("\n")
#
# list1 = [items.split(",") for items in list if len(items)!=0]
# print(list1)
#
# with open("iris.txt","wb") as data:
#     pickle.dump(list1,data)
import pickle

with open("iris.txt","rb") as data:
    print(pickle.load(data))



