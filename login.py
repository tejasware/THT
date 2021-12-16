from dbms_project import insert,apply,login, printContracts, printmyContracts
from getpass import getpass

print("The High Table")
print("--------------------------")

id = input("Enter id:")
password = getpass("Enter password:")
result = login(id, password)
if(result[0][0].startswith('H')):
    print('*'*30)
    printContracts()
    print('*'*30)
    choice = input("Do you want to apply? Y=yes, N=no:")
    print('-'*30)
    if(choice == 'Y'):
        apply()
    else:
        print("Thank you")
        print('*'*30)
else:
    print('*'*30)
    printmyContracts()
    print('*'*30)
    choice = input("Do you want to enter new target? Y=yes, N=no:")
    if(choice == 'Y'):
        insert()
    else:
        print("Thank you")
    