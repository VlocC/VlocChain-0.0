import time as timestamp

class User():
    def __init__(self, username):
        self.username = username
        numb_sent = 0
        numb_received = 0
        wallet_size = 3

    def get_transactions(self, total_exchanges):
        curated_list = []
        for exchange_index in range (0, len(total_exchanges)):
            exchange_inst = total_exchanges[exchange_index]
            if (self.username in exchange_inst):
                curated_list.append(exchange_inst)
        return curated_list

    def view_wallet(self):
        return self.wallet_size

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



