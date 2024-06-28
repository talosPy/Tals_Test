# from Problems import problems

from Problems.problems import (
    price_engine, 
    price_breaks, 
    price_5k_treatment, 
    price_10k_treatment, 
    price_filters_oil, 
    price_gear, 
)

def problems():
    print("6 - Engine")
    print("7 - Breaks")
    print("8 - 5k Treatment")
    print("9 - 10k Treatment")
    print("10 - Filters_Oil")
    print("11 - Gear")
    print("12 - Exit")
    prob = input("Choose your problem using 6-11, 12 to exit: ")
    if prob == "6":
        return {'problem': 'Engine', 'price': price_engine()}
    elif prob == "7":
        return {'problem': 'Breaks', 'price': price_breaks()}
    elif prob == "8":
        return {'problem': '5k Treatment', 'price': price_5k_treatment()}
    elif prob == "9":
        return {'problem': '10k Treatment', 'price': price_10k_treatment()}
    elif prob == "10":
        return {'problem': 'Filters Oil', 'price': price_filters_oil()}
    elif prob == "11":
        return {'problem': 'Gear', 'price': price_gear()}
    elif prob == "12":
        print("ENDED PROGRAM")
    else:
        print("Invalid choice, please choose a valid option.")
        return problems()  
