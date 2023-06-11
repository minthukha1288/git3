# import pymongo
#
# import random
# connection = pymongo.MongoClient("localhost", 27017)
# database = connection["pop"]
# collection = database["user_info"]
#
#
# if __name__ == '__main__':
#     try:
#         user_id = random.randint(0, 100)
#         email: str = input("Please enter userEmail: ")
#         password = input("Please enter userPass: ")
#         phone: int = int(input("Please enter userphone: "))
#         address: str = input("Please enter userAddress: ")
#
#         data_form = {"User_Email": email, "User_Password": password, "User_Phone": phone, "UserAddress": address}
#         ids = collection.insert_one(data_form)
#
#         print("inserted id:", ids.inserted_id)
#     except Exception as err:
#         print(err)
#

import pymongo
import random

connection = pymongo.MongoClient("localhost", 27017)
database = connection["min_db"]
collection = database["min_1"]

if __name__ == '__main__':
    try:
        user_id = random.randint(0, 100)
        email: str = input("Please enter userEmail: ")
        password = input("Please enter userPass: ")
        phone: int = int(input("Please enter userphone: "))
        address: str = input("Please enter userAddress: ")

        data_form = {"User_Email": email, "User_Password": password, "User_Phone": phone, "UserAddress": address}
        ids = collection.insert_one(data_form)

        print("inserted id:", ids.inserted_id)
    except Exception as err:
        print(err)
