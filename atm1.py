import sys
def pin_number():
    password = 1234
    for attempts in range(3):
        pin_code = int(input('Enter your pin: '))
        if password == pin_code:
            print('correct')
            Balance()
        if password != pin_code:
             print ("Try Again!")
    else:
         print('Wrong pin')


def Balance():
    try:
        Account_balance = 100
        withdrawal = int(input('how much would you like to withdraw?: '))
        Remaining_balance = Account_balance - withdrawal
        if withdrawal > Account_balance:
            sys.exit("Error")
        if withdrawal < 0:
            raise ValueError
    except ValueError as e:
        print ('please enter a positive number')
    else:
        print(Remaining_balance)




pin_number()




