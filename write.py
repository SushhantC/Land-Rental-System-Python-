from datetime import datetime

# Open the file "Land.txt" for reading
file = open("Land.txt", "r")
# Create an empty dictionary to store available lands
available_lands = {}
# Initialize a serial number counter
sn = 1

# Loop through each line in the file
for line in file:
    # Remove the newline character from each line
    line = line.replace("\n", "")
    # Split the line into a list of data using comma and space as separators
    data = line.split(", ")
    # Store the data in the dictionary with the serial number as key
    available_lands[sn] = data
    # Increment the serial number counter
    sn = sn + 1

# Close the file after reading
file.close()

# Function to generate invoice for renting land
def invoice(sn, name, months, buyer_phone):
    # Retrieve land details using the serial number from the available_lands dictionary
    kitta_no = available_lands[sn][0]
    location = available_lands[sn][1]
    direction = available_lands[sn][2]
    aana = available_lands[sn][3]
    price = available_lands[sn][4]
    # Calculate total amount based on price and duration
    total_amount = int(price) * int(months)
    # Get the current date and format it
    current_date = datetime.now().strftime("%B %d, %Y")

    # Print invoice details
    print("==============================================================================")
    print("|                     INVOICE FOR RENTING LAND                               |")
    print("|                  TechnoPropertyNepal Pvt. Ltd.                             |")
    print("|                    Invoice Date: ", datetime.now().strftime("%B %d, %Y"), )
    print("==============================================================================")
    print("Name:", name)
    print("Phone Number:", buyer_phone)
    print("Date:", current_date)
    print("Kitta no: ", kitta_no)
    print("Location:", location)
    print("Direction:", direction)
    print("Aana:", aana)
    print("Price:", price)
    print("TotalAmount:", total_amount)
    print("Duration:", months, "months")
    print("Thank you for renting from TechnoPropertyNepal!")
    print("=============================================================================")

    # Create invoice text for writing to file
    invoice_text = "================================================================================\n"
    invoice_text += "                     INVOICE FOR RENTING LAND                                  \n"
    invoice_text += "                  TechnoPropertyNepal Pvt. Ltd.                                \n"
    invoice_text += "                     Invoice Date: " + datetime.now().strftime("%B %d, %Y") + "\n"
    invoice_text += "===============================================================================\n"
    invoice_text += "Name: " + name + "\n"
    invoice_text += "Phone Number: " + str(buyer_phone) + "\n"
    invoice_text += "Date: " + current_date + "\n"
    invoice_text += "Kitta no: " + kitta_no + "\n"
    invoice_text += "Location: " + location + "\n"
    invoice_text += "Direction: " + direction + "\n"
    invoice_text += "Aana: " + aana + "\n"
    invoice_text += "Price: " + price + "\n"
    invoice_text += "Total Amount: " + str(total_amount) + "\n"
    invoice_text += "Duration: " + str(months) + " months\n"
    invoice_text += "Thank you for renting from TechnoPropertyNepal!\n"
    invoice_text += "==============================================================================\n"

    # Generate invoice file name
    invoice_file_name = "Invoice_" + str(sn) + "_" + name + ".txt"
    # Open the invoice file for writing
    invoice_file = open(invoice_file_name, "w")
    # Write the invoice text to the file
    invoice_file.write(invoice_text)
    # Close the invoice file
    invoice_file.close()

    # Print success message with invoice file name
    print("Invoice generated successfully. Filename: " + invoice_file_name)


# Function to update the land file with available lands information
def update_land_file(available_lands):
    # Open the file "Land.txt" for writing
    file = open("Land.txt", "w")
    # Loop through available lands and write them to the file
    for land_info in available_lands.values():
        file.write(str(land_info[0]) + ", " + str(land_info[1]) + ", " + str(land_info[2]) + ", " + str(
            land_info[3]) + ", " + str(land_info[4]) + ", " + str(land_info[5]))
        file.write("\n")
    # Close the file after writing
    file.close()


# Function to generate return invoice
def invoice_return(sn, name, return_date, duration, total_amount, late_fee, return_phone):
    # Retrieve land details using the serial number from the available_lands dictionary
    kitta_no = available_lands[sn][0]
    location = available_lands[sn][1]
    direction = available_lands[sn][2]
    aana = available_lands[sn][3]
    price = available_lands[sn][4]

    # Print return invoice details
    print("================================================================")
    print("|                     RETURN INVOICE                           |")
    print("|                   TechnoPropertyNepal Pvt. Ltd.              |")
    print("|                 Return Date: ", return_date, "               |")
    print("================================================================")
    print("Name:", name)
    print("Phone Number:", return_phone)
    print("Return Date:", return_date)
    print("Kitta no: ", kitta_no)
    print("Location:", location)
    print("Direction:", direction)
    print("Aana:", aana)
    print("Price:", price)
    print("Duration:", duration, "months")
    print("Total Amount:", total_amount)
    if late_fee > 0:
        print("Late Fee:", late_fee)
    print("Thank you for renting from TechnoPropertyNepal!")
    print("===============================================================")

    # Create return invoice text for writing to file
    invoice_text = "===============================================================\n"
    invoice_text += "                     RETURN INVOICE                           \n"
    invoice_text += "                   TechnoPropertyNepal Pvt. Ltd.              \n"
    invoice_text += "                 Return Date: " + return_date + "             \n"
    invoice_text += "==============================================================\n"
    invoice_text += "Name: " + name + "\n"
    invoice_text += "Phone Number: " + str(return_phone) + "\n"
    invoice_text += "Return Date: " + return_date + "\n"
    invoice_text += "Kitta no: " + kitta_no + "\n"
    invoice_text += "Location: " + location + "\n"
    invoice_text += "Direction: " + direction + "\n"
    invoice_text += "Aana: " + aana + "\n"
    invoice_text += "Price: " + price + "\n"
    invoice_text += "Duration: " + str(duration) + " months\n"
    invoice_text += "Total Amount: " + str(total_amount) + "\n"
    if late_fee > 0:
        invoice_text += "Late Fee: " + str(late_fee) + "\n"
    invoice_text += "Thank you for renting from TechnoPropertyNepal!\n"
    invoice_text += "===============================================================\n"

    # Generate return invoice file name
    invoice_file_name = "Return_Invoice_" + str(sn) + "_" + name + ".txt"
    # Open the return invoice file for writing
    invoice_file = open(invoice_file_name, "w")
    # Write the return invoice text to the file
    invoice_file.write(invoice_text)
    # Close the return invoice file
    invoice_file.close()

    # Print success message with return invoice file name
    print("Return Invoice generated successfully. Filename: " + invoice_file_name)
