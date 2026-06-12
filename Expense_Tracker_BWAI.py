import json

data = {}
i = True
try:
    with open("data.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    data = {}
while True:
    print("+--------------------------------------------------------+")
    print('Type 1 To Add An Expense \nType 2 To View Expenses \nType 3 To Quit')
    print("+--------------------------------------------------------+")
    user = input('Enter Your Choice: ')
    if user != "1" and user != "2" and user != "3":
        print('Invalid Option!')
    elif user == "3":
        print("+--------------------------------------------------------+")
        print("Goodbye User")
        print("+--------------------------------------------------------+")
        break
    elif user == "1":
        while i == True:
            item = input("Enter The Name Of The Item: ")
            cost = float(input("Enter The Cost Of The Item: "))
            print("+--------------------------------------------------------+")
            data[item] = cost
            with open("data.json", "w") as file:
                json.dump(data, file)
            print("Data Stored!")
            print("+--------------------------------------------------------+")
            again = input("Have More Items? \nType Yes \nType No \n")
            print("+--------------------------------------------------------+")
            with open("data.json", "r") as file:
                data = json.load(file)
            if again == "yes":
                continue
            elif again == "no":
                break
    if user == "2":
        print("+--------------------------------------------------------+")
        for key, value in data.items():
            print(f"{key}: ${value}")
        total = sum(data.values())
        print(f"Total Expenses: ${total}")
