# Read a csv file and transform this to a list
    file_path = input("Enter the path to the CSV file: ")
    records = []
    with open(file_path, 'r') as file:
        """
        Opens the csv file and puts the results in a list
        """
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            records.append(row)


# Compute the average grade
    total = sum(float(record['Grade']) for record in records)
    average = total / len(records)

# Filters the grades on being greater than 80
    filtered_records = [record for record in records if float(record['Grade']) >= 80.0]


print(f"Average Grade: {average}")
print("--------------------")
print("Student Report")
print("--------------")
for record in filtered_records:
    print(f"Name: {record['Name']}")
    print(f"Grade: {record['Grade']}")
    print("--------------------")
