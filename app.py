from Cars.action import add, delete, search
from Storage.load_save import read, save
from Problems.problems_menu import problems

def menu():
    my_garage = read()  
    while True:
        print('1 - Add')
        print('2 - Delete')
        print('3 - Search')
        print('4 - List')
        print('5 - Exit')
        print('6 - Reach Problems')
        
        selection = input('Choose Command: ')

        if selection == '1':
            add(my_garage)   
        elif selection == '2':
            delete(my_garage)  
        elif selection == '3':
            search(my_garage)
        elif selection == '4':
            print(my_garage)
        elif selection == '5':
            print('ENDED PROGRAM')
            save(my_garage)  
            break
        elif selection == '6':
            my_garage = problems(my_garage)  
            save(my_garage)  
        else:
            print('NOT FOUND')

if __name__ == "__main__":
    menu()
