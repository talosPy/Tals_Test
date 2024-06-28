from Problems.problems_menu import problems

def add(my_garage):
    new_car_number = input('New Car Number: ')
    print("Please select the problem for the new car:")
    problem_data = problems()
    
    if problem_data:
        new_car = {
            'number': new_car_number,
            'problem': problem_data['problem'],
            'price': problem_data['price']
        }
        if my_garage is None:  # Ensure my_garage is initialized as a list if it's None
            my_garage = []
        my_garage.append(new_car)
        print('Car Added')
    else:
        print('Failed to add car. No problem selected.')



def delete(my_garage):
    car_select = int(input('Choose the index of which car you wish to remove: '))
    my_garage.pop(car_select)


def search(my_garage):
    search_garage = input('Choose the car you want to search: ')
    found = False
    
    for cars in my_garage:
        if cars['number'].lower() == search_garage.lower():
            print(f"Name: {cars['number']}, Problem: {cars['problem']}", {cars['price']})
            
            found = True
            break
    
    if not found:
        print('INVALID CAR')

def add_problem(my_garage):
    problem_name = input('Enter the problem name: ')
    price = float(input('Enter the price: '))
    my_garage.append({'problem': problem_name, 'price': price})
    print(f'Added problem "{problem_name}" with price {price} to my garage.')
