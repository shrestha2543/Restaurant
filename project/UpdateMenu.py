import json
MENU_FILENAME='Menu.json'

def new_menu(data): #All the changes will be reflected back to the menu json file
   try:
      with open(MENU_FILENAME, 'w') as f:
         json.dump(data, f, indent=4)
      return True
   except Exception as e:
      print(f" !!! Error in saving menu data {e}!!!")
      return False
def new_item(data,items): #asks user to add a new item and then saves the changes in the menu
   print("Add a new item:") 
   try:
      new_id=int(input("Enter the item ID: "))
      new_name=input("Enter the name of the new item")
      new_price=int(input("Enter the price of the item"))
      if any(item.get("ID")==new_id for item in items):
         print(f"!!! Item with ID{new_id} already exists")
         return
      new_item={"ID":new_id,"Name":new_name,"Price":new_price}
      items.append(new_item)
      data["items"]=items
      if new_menu(data):
         print(f"Item '{new_name}' has been added to menu successfully.")
   except ValueError:
      print("!!! Invalid ID or price entered.")            