from user_class import *
# from vlocc import *

def send_to():
	recieve = input("Please enter VlocC address of other user: ")
	attachment = input("Please enter what you want to send: ")
	User.send(recieve, attachment)

def main():
	print("Welcome to VlocC!")
	contin = "y"
	while contin == "y":
		while True:
			# user_exchanges = User.get_transactions(exchanges)
			userinput = input("What would you like to do today? ('help' for all options) ")
			if userinput == "help":
				print("send, view, last, wallet")
			else:
				break
		if userinput == "send":
			send_to()
		elif userinput == "view":
			print(user_exchanges)
		elif userinput == "last":
			print(user_exchanges[-1])
		elif userinput == "wallet":
			print(User.view_wallet())
		contin = input("Would you like to continue? (y/n): ") 

if __name__ == '__main__':
	main()

