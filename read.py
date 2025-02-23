def read_txt():
    # Initialize serial number
    sn = 1
    # Open the file in read mode
    file = open("Land.txt", "r")
    available_lands = {}  # Dictionary to store available lands
    # Print header for the available lands list
    print("Available Lands:")
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("S.N\t    Kitta No.\t     City/District\t     Direction\t   Area (Anna)\t    Price (NPR)\t         Status")
    print("--------------------------------------------------------------------------------------------------------------------------")

    for line in file:
        # Remove newline character from the line and split by comma
        data = line.strip().split(",")  # Using strip() to remove trailing whitespace
        # Store data in the dictionary with serial number as key
        available_lands.update({sn: line.split(", ")})
        # Print formatted data for each land
        print(str(sn) + "\t\t" + data[0] + "\t\t" + data[1] + "\t\t" + data[2] + "\t\t" + data[3] + "\t\t" + data[4] + "\t\t" + data[5])
        sn = sn + 1
    file.close()  # Close the file after reading
