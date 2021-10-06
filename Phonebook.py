phoneNumbers = {'Amal': '1111111111', 'Mohammed': '2222222222',
                'Khadijah': '3333333333', 'Abdullah': '4444444444',
                'Rawan': '5555555555','Faisal': '6666666666',
                'Layla': '7777777777'}
def findNumber(num):
    if num.isdigit() and len(num) == 10:
        for name,num in phoneNumbers.items():
            if val == num:
                print(name,':',phoneNumbers[name])
                break
        else:
            print("Sorry,this number is not found")
    else:
        print("this invalid number")
def findName(name):
        for name, number in phoneNumbers.items():
            if val.lower() == name.lower():
                print(number)
                break
        else:
            print("Sorry,this name is not found")
def newUser(dic):
    while True:
        name = input("Enter the name of the new user:\n")
        if name.isalpha():
            break
        else:
            print('Enter valid name')
    number = input("Enter the number of new user:\n")
    while len(number) != 10 or (not number.isdigit()):
        number = input('Please enter 10 digit\n')
    if number in phoneNumbers:
        print(' Number already in phonebook\n')
    else:
        phoneNumbers.update({name : number})
    return dic
i = int(input("For search Phone number :1\n"
              "For search name :2\n"
              "To add new contact :3\n"
              "To exit :4\n"))

while i != 4:
    if i == 1:
        val = input("Enter number of user:")
        findNumber(val)
    elif i == 2:
        val = input("Enter name of user:")
        findName(val)
    elif i == 3:
        print(newUser(phoneNumbers))
    else:
        print("Choose one of 1,2,3,4")
        break
    i = int(input("For search Phone number :1\nFor search name :2\nTo add new contact :3\nTo exit :4\n"))