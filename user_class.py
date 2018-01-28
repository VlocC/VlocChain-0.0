import time as timestamp
import os
from PIL import Image
from __future__ import print_function
class User():
    def __init__(self, username, file_path):
        self.username = username
        self.file_path = file_path
        numb_sent = 0
        numb_received = 0
        wallet_size = 3

    def get_transactions(self, total_exchanges):
        curated_list = []
        for exchange_index in range (0, len(total_exchanges)):
            exchange_inst = total_exchanges[exchange_index]
            if (self.username in exchange_inst):
                curated_list.append(exchange_inst)
        user_list_length = len(curated_list)
        index = 0
        if (user_list_length >= 5):
            print ("Here are your last 5 transactions: ")
            while(index < 5):
                print (curated_list[user_list_length-1-index])
                index += 1
        else:
            print ("Here are your past transactions: ")
            while (index < user_list_length):
                print (curated_list[user_list_length-1-index])
                index += 1
        return curated_list

    def view_local_files(self):
        for file in os.listdir(self.file_path):
            if (os.path.isfile(os.path.join(self.file_path, file))):
                print(file)

    def store_image(self, file_name):
        path = self.file_path + "\\" + file_name
        uploaded_im = Image.open(path)
        uploaded_im.load()
        print(uploaded_im.format, uploaded_im.size, uploaded_im.mode)








    def view_wallet(self):
        return self.wallet_size

    def get_address(self):
        return self.username

    def get_file_path(self):
        return self.file_path

    def send(self, receiver, vid):
        if (self.view_wallet() > 0):
            message = vid.attachment
            receiver_name = receiver.username
            transact_time = timestamp.timestamp.now()
            receiver.receive(self, message, transact_time)
            self.numb_sent += 1
            self.wallet_size -= 1
        else:
            print("You don't have any"
                  "money in your wallet.\n")



    def receive(self, sender, vid, time):
        message = vid.attachment
        time_mark = time
        self.wallet_size += 1
        self.numb_received += 1



