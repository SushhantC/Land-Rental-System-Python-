import Operation

# Display system header
print("                 ╦ ╦╔═╗╦  ╔═╗╔═╗╔╦╗╔═╗  ")
print("                 ║║║║╣ ║  ║  ║ ║║║║║╣   ")
print("                 ╚╩╝╚═╝╩═╝╚═╝╚═╝╩ ╩╚═╝  ")



print("╔╦╗╔═╗╔═╗╦ ╦╔╗╔╔═╗  ╔═╗╦═╗╔═╗╔═╗╔═╗╦═╗╔╦╗╦ ╦  ╔╗╔╔═╗╔═╗╔═╗╦    ")
print(" ║ ║╣ ║  ╠═╣║║║║ ║  ╠═╝╠╦╝║ ║╠═╝║╣ ╠╦╝ ║ ╚╦╝  ║║║║╣ ╠═╝╠═╣║    ")
print(" ╩ ╚═╝╚═╝╩ ╩╝╚╝╚═╝  ╩  ╩╚═╚═╝╩  ╚═╝╩╚═ ╩  ╩   ╝╚╝╚═╝╩  ╩ ╩╩═╝  ")
print("  ╦  ╔═╗╔╗╔╔╦╗  ╦═╗╔═╗╔╗╔╔╦╗╦╔╗╔╔═╗  ╔═╗╦ ╦╔═╗╔╦╗╔═╗╔╦╗        ")
print("  ║  ╠═╣║║║ ║║  ╠╦╝║╣ ║║║ ║ ║║║║║ ╦  ╚═╗╚╦╝╚═╗ ║ ║╣ ║║║        ")
print("  ╩═╝╩ ╩╝╚╝═╩╝  ╩╚═╚═╝╝╚╝ ╩ ╩╝╚╝╚═╝  ╚═╝ ╩ ╚═╝ ╩ ╚═╝╩ ╩        ")                                                                          
                                                                           

# Function to manage the main program logic

def main():
    while True:
        try:
            # Display menu options
            print("1. Rent a land")
            print("2. Return a rented land")
            print("3. Exit")

            # Prompt user for choice
            choice = input("Enter your choice: ")

            # Perform actions based on user choice
            if choice == "1":
                Operation.rent_land()  # Call the function to rent a land
            elif choice == "2":
                Operation.return_land()  # Call the function to return a rented land 
            elif choice == "3":
                print("Exiting the program...")
                print("Thank you for using the System , Have a good day")
                break  # Exit the loop and end the program
            else:
                print("Invalid choice. Please Enter number 1 or 2 or 3 only.")
        except Exception as e:
            # Exception handling for invalid inputs
            print("________________________________________________________________________")
            print("(Invalid Input) Please Enter number 1 or 2 or 3 only", e)
            print("________________________________________________________________________")


# Call the main function to start the program
main()
