import json
import sys

from UpdateMenu import new_item 
from Review import review

with open('Menu.json', 'r') as f:
    data=json.load(f)

def menuu(filename='Menu.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError: #In case of error
        print(f"!!! Error:{filename} not found.Please ensure the file exists!!!")
        sys.exist(1)
    except json.JSONDecodeError: #in case of error
        print(f"!!!{filename} is corrupted or empty.Check the json synstax.")
        sys.exit(1)        
data=menuu()

items=data.get('items', [])
while True: #displaying all the options
    print("="*50)
    print("The Great Indian Restaurant")
    print("="*50)
    print("1. View Menu")
    print("2. Order Items")
    print("3. Update Menu")
    print("4. Add Review")
    print("5. Exit")
    print("-"*50)
    try:
        ch=int(input("Enter your choice (1-5): ")) #asking the user to enter their choice
        print("-"*50)
    except ValueError:
        print("!!! Please enter a valid number !!!")
        continue #restart the loop if non integer input is given
    
    if(ch==1):# option to view the menu
        print("ID\tName\t\tPrice")
        print("-"*50)
        for item in items: #displaying the item details
            print(f'{item.get("ID")}\t{item.get("Name")}\t\t{item.get("Price")}')
        print('-'*50)

    elif ch==2: #Option to order the items from the menu

        try: 
             order_items=list(map(int, input("Place your order(Enter IDs separated by commas): ").split(','))) #Accepts IDs separated by commas
        except ValueError: #error handling strategy
             print("!!! Invalid Input. Please enter only integrs separated by comma!!!")  
             continue  
        print('-'*50)
        print("ID\tName\t\t\t\tPrice")
        print("-"*50)

        bill=0 #initializing the bill variable with 0
        for order_item in order_items:# Iterate through the order IDs
            
            for item in items:
                if item['ID']==order_item:
                     print(f'{item.get("ID")}\t{item.get("Name")}\t\t\t{item.get("Price")}') #printing the item details
                     bill=bill+ int(item.get("Price", 10)) #calculating the bill 
                     break
        print("-"*50)        
        print(f'\tTotal Amount: Rs{bill}') #printing the bill
        print("-"*50)

    elif ch==3:
        #here we are calling the function to update the menu from UpdateMenu file
        new_item(data,items)

    elif ch==4:
        #calling the function to store and print the review
        review()

    elif ch==5: 
        print("Thank You.")
        break #to exit the while loop

    else: #in case of invalid choice given print  statement will be displayed
        print("!!! Please enter a valid choice between 1 and 5 !!!")
        