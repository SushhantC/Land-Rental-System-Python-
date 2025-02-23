import read
from datetime import datetime, timedelta
import write

file = open("Land.txt", "r")
available_lands = {}
sn = 1
for line in file:
    line = line.replace("\n", "")
    available_lands.update({sn: line.split(", ")})
    sn = sn + 1
file.close()


def rent_land():
    while True:
        try:
            # Display the available lands
            read.read_txt()

            # Get the serial number of the land the user wants to rent
            symbol_no = int(input("Enter the SN of the land you want to rent: "))

            # Check if the entered serial number exists in the available lands
            if symbol_no in available_lands:
                # Check if the selected land is available for rent
                if available_lands[symbol_no][5] == "Not Available":
                    print("This land is already rented. Please choose another land.")
                else:
                    try:
                        # Prompt user for rent duration, phone number and customer name
                        rent_duration = int(input("Enter the duration of rent (in months): "))
                        customer_name = input("Enter your name: ")
                        buyer_phone = int(input("Ënter your Phone number:"))

                        # Prompt the user for "aana" 
                        aana = input("Enter the total aana value of the land: ")

                        if available_lands[symbol_no][3] != aana:
                            print("The entered aana value does not match the land's information. Please enter a valid "
                                  "aana.")
                        else:
                            # Generate invoice and update land status
                            write.invoice(symbol_no, customer_name, rent_duration,buyer_phone)
                            available_lands[symbol_no][5] = "Not Available"  # Update availability status
                            write.update_land_file(available_lands)  # Update Land.txt file with modified status
                            print("Land rented successfully!")
                    except ValueError:
                        print("Invalid input. Please enter a valid number for rent duration.")

                    # Check if the user wants to rent another land
                    more_land = input("Do you want to rent another land? (yes/no): ")
                    if more_land.lower() == "no":
                        break  # Exit the loop if the user doesn't want to rent another land
            else:
                print("Invalid Symbol Number or land not available for rent.")
        except KeyError:
            print("Invalid input. Please enter a valid serial number.")

def return_land():
    while True:
        try:
            # Display the available lands
            read.read_txt()

            # Get the serial number of the land the user wants to return
            symbol_no = int(input("Enter the SN of the land you want to return: "))

            # Check if the entered serial number exists in the available lands
            if symbol_no in available_lands:
                # Check if the selected land is already available
                if available_lands[symbol_no][5].replace(" ", "") == "Available":
                    print("This land is already available. Please choose another land.")
                else:
                    try:
                        # Prompt user for necessary information
                        customer_name = input("Enter your name: ")
                        return_phone = int(input("Enter your Phone number: "))
                        ask_no_month_after_rent = int(input("Enter the number of months that you exceeded after rent: "))
                        no_month_before_rent = int(input("Enter the number of months mentioned while renting: "))
                        rent_price_per_month = int(available_lands[symbol_no][4])
                        
                        total_amount = rent_price_per_month * no_month_before_rent
                        total_fine = max(0, ask_no_month_after_rent - no_month_before_rent) * 1000
                        total_amount += total_fine

                        if ask_no_month_after_rent > no_month_before_rent:
                            print("Since the rented number of months has been exceeded, the extra number of months is ", ask_no_month_after_rent - no_month_before_rent)
                            print("So, The total amount after fine is ", total_amount)
                        else:
                            print("The total amount is ", total_amount)

                        return_date = datetime.now().strftime("%Y-%m-%d")

                        # Generate invoice and update land status
                        write.invoice_return(symbol_no, customer_name, return_date, ask_no_month_after_rent,
                                             total_amount, total_fine, return_phone)
                        available_lands[symbol_no][5] = "Available"  # Update availability status
                        write.update_land_file(available_lands)  # Update Land.txt file with modified status
                        print("Land returned successfully!")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")

                    # Check if the user wants to return another land
                    more_land = input("Do you want to return another land? (yes/no): ")
                    if more_land.lower() == "no":
                        break  # Exit the loop if the user doesn't want to return another land
            else:
                print("Invalid Symbol Number or land not rented.")
        except KeyError:
            print("Invalid input. Please enter a valid serial number.")
