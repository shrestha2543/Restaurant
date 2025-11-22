# THE GREAT INDIAN RESTAURANT

1) Project Title: VITyarthi- Build Your own project

2) Overview of the Project: This is a Python Project which provides a simple command line interface (CLI) for managing a restauarant's menu, placing orders,updating the menu and collecting reviews.
  
3) Features:
   * View Menu: Displays all available items,their IDs and their prices.
   * Place Order: Calculate and display the bill on the basis of IDs entered by user.
   * Update Menu: Add new items to the menu (requires external function new_item from UpdateMenu.py)
   * Add Review: Stores customer feedback (requires external function review from Review.py)
   * Error Handling: Robust error handling for file operations(Menu.json) and user input
     
4) Steps to install and run the project:
   * Python 3.x must be installed to run this application.
   * The following external files must be present in the same directory as the main script:-
     - Menu.json ( This file must contain array of items under the key "items")
     - UpdateMenu.py (This file should have a function to add new items and update the Menu.json file)
     - Review.py (This file should contain a function to submit reviews)
   * How to Run:
     - Ensure the files(Menu.json,Review.py, UpdateMenu.py) are in place.
     - Open terminal or command prompt
     - Navigate to the directory containing files.
     - Run the main script( cafe.py ) using Python Interpreter.
  
