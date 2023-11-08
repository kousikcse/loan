#import Error
import connectdb
from members import members
from loans import loans
from payments import payments

while True:
    print('''
    Welcome Loan Management System 1.0
    **********************************
    Input a number for entering to module:
    1: Member
    2: Loan
    3: Payments
    Default: Quit
    ''')
    try:
        i=int(input('Enter Input (1/2/3):'))
    except ValueError:
        i=-1
    if i==1:
        members()
    elif i==2:
        loans()
    elif i==3:
        payments()
    else:
        print('Good bye !')
        break
    


