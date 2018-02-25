from __future__ import print_function
from PIL import Image
import time as timestamp
import os

#Testing variable, if it sent
message = ""


class User():
    def __init__(self, username, file_path, email_address):
        self.username = username
        self.file_path = file_path
        self.email_address = email_address
        numb_sent = 0
        numb_received = 0
        wallet_size = 3

    def set_message(self,msg):
        self.message = msg


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

    def load_image(self, file_name):
        if (self.linux):
            path = self.file_path + "/" + file_name
        else:
            path = self.file_path + "\\" + file_name
        uploaded_im = Image.open(path)
        return uploaded_im

    def write_image(self, folder_path, image_name, img):
        if (self.linux):
            img.save(folder_path + "/" + image_name)
        else:
            img.save(folder_path + "\\" + image_name)




    def view_wallet(self):
        return self.wallet_size

    def get_address(self):
        return self.username


    def send(self, receiver, message_name):
        if (self.view_wallet() > 0):
            response = input("Is your message a text, or an image? t/i")
            if (response == "t" or response == "T"):
                message = message_name
            else:
                message = self.loadImage(message_name)
            receiver_name = receiver.username
            transact_time = timestamp.timestamp.now()
            receiver.receive(self, message, message_name, transact_time)
            self.numb_sent += 1
            self.wallet_size -= 1
        else:
            print("You don't have any"
                  "money in your wallet.\n")



    def receive(self, sender, fd, file_name, time):
        time_mark = time
        ## if-else chain will need to be changed if
        ## more datatypes are implemented
        if (isinstance(fd, Image)):
            self.write_image(self.file_path, file_name, fd)
        else:
            print(fd)
        self.wallet_size += 1
        self.numb_received += 1
