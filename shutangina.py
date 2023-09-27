# tawagin nyo si pip install mysql-connector-python at python-dateutil mga be

import mysql.connector
from dateutil import parser
import re

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root", #name
    password="hatdog", #password nyo sa mysql
    database="haha" #database name
)
cursor = db.cursor()


# Function to pause screen
def pause_system():
    print("\nPress any key to continue...")
    input()


# Function to classify data
def classify_data(input_string):
    if '@' in input_string or '.' in input_string:
        if validate_email(input_string):
            return 'Email Address'
        else:
            print("Invalid email address!")
            pause_system()
            return 'Unknown'
    elif input_string.isdigit():
        if len(data_value) != 11:
            print("Invalid cellphone number! It must be 11 digits.")
            pause_system()
            return 'Unknown'
        else:
            return 'Cellphone Num'
    elif input_string.replace(" ", "").isalpha(): #spaces are also read
        return 'Name         '
    else:
        try:
            parser.parse(input_string) #dateutil format
            return 'Date of Birth'
        except:
            print("Invalid!")
            pause_system()
            return 'Unknown'


# Function to validate email
def validate_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(regex, email):
        return email
    else:
        return False


# Function to insert data
def insert_data(data_type, data_value):
    sql = "INSERT INTO User_Data (Type, Value) VALUES (%s, %s)"
    val = (data_type, data_value)
    cursor.execute(sql, val)
    db.commit()
    return cursor.lastrowid, data_type


# Function to update data
def update_data(id, data_type, data_value):
    sql = "UPDATE User_Data SET Type = %s, Value = %s WHERE ID = %s"
    val = (data_type, data_value, id)
    cursor.execute(sql, val)
    db.commit()
    return id, data_type


# Function to view all records
def view_all_records():
    sql = "SELECT * FROM User_Data"
    cursor.execute(sql)
    records = cursor.fetchall()
    if len(records) == 0:
        print("No records found.")
    else:
        print("ID\tType\tValue")
        for record in records:
            print(f"{record[0]}\t{record[1]}\t{record[2]}")


def delete_data():
    print("1. Delete a record")
    print("2. Delete all record")
    delete_option = input("Enter your choice: ")
    if delete_option == "1":
        view_all_records()
        record_id = input("Enter the ID of the record you want to delete: ")
        sql = f"DELETE FROM User_Data WHERE ID = '{record_id}'"
        print("Record deleted successfully.")
        cursor.execute(sql)
        db.commit()
    elif delete_option == "2":
        confirm = input(
            "Are you sure you want to delete all records? This action cannot be undone. Enter 'yes' to confirm: ")
        if confirm.lower() == "yes":
            sql = "DELETE FROM User_Data"
            cursor.execute(sql)
            db.commit()
            print("All records deleted successfully.")
        else:
            print("Deletion canceled.")
    else:
        print("Invalid option. Please try again.")


# Function to filter records by data type
def filter_records_by_type(data_type):
    sql = "SELECT * FROM User_Data WHERE Type = %s"
    val = (data_type,)
    cursor.execute(sql, val)
    records = cursor.fetchall()
    if len(records) == 0:
        print(f"No records found for data type: {data_type}")
    else:
        print("ID\tType\tValue")
        for record in records:
            print(f"{record[0]}\t{record[1]}\t{record[2]}")


# Main program
while True:
    print("1. Insert Record")
    print("2. Edit Record")
    print("3. View All Record")
    print("4. Group Records by Data Type")
    print("5. Delete record")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        data_value = input("Enter the data: ")
        data_type = classify_data(data_value)
        if data_type == 'Email Address':
            inserted_id, inserted_type = insert_data(data_type, data_value)
            print("Inserted data with ID:", inserted_id)
            print("Type:", inserted_type)
            pause_system()

        if data_type == 'Cellphone Num':
            inserted_id, inserted_type = insert_data(data_type, data_value)
            print("Inserted data with ID:", inserted_id)
            print("Type:", inserted_type)
            pause_system()

        if data_type == 'Name         ':
            inserted_id, inserted_type = insert_data(data_type, data_value)
            print("Inserted data with ID:", inserted_id)
            print("Type:", inserted_type)
            pause_system()

        if data_type == 'Date of Birth':
            inserted_id, inserted_type = insert_data(data_type, data_value)
            print("Inserted data with ID:", inserted_id)
            print("Type:", inserted_type)
            pause_system()

    elif choice == '2':
        view_all_records()
        id = input("Enter the ID of the data to edit: ")
        data_value = input("Enter the new data: ")
        data_type = classify_data(data_value)

        if data_type == 'Email Address':
            updated_id, updated_type = update_data(id, data_type, data_value)
            print("Inserted data with ID:", updated_id)
            print("Type:", updated_type)
            pause_system()

        if data_type == 'Cellphone Num':
            updated_id, updated_type = update_data(id, data_type, data_value)
            print("Updated data with ID:", updated_id)
            print("Type:", updated_type)
            pause_system()

        if data_type == 'Name         ':
            updated_id, updated_type = update_data(id, data_type, data_value)
            print("Updated data with ID:", updated_id)
            print("Type:", updated_type)
            pause_system()

        if data_type == 'Date of Birth':
            updated_id, updated_type = update_data(id, data_type, data_value)
            print("Inserted data with ID:", updated_id)
            print("Type:", updated_type)
            pause_system()

    elif choice == '3':
        view_all_records()
        pause_system()

    elif choice == '4':
        print("\nSelect a data type:")
        print("1. Name")
        print("2. Date of Birth")
        print("3. Cellphone Number")
        print("4. Email Address")
        data_type_choice = input("Enter your choice: ")
        if data_type_choice == '1':
            filter_records_by_type('Name')
        elif data_type_choice == '2':
            filter_records_by_type('Date of Birth')
        elif data_type_choice == '3':
            filter_records_by_type('CellNum')
        elif data_type_choice == '4':
            filter_records_by_type('Email Address')
        else:
            print("Invalid choice!")
        pause_system()

    elif choice == '5':
        delete_data()
        pause_system()

    elif choice == '6':
        break
    else:
        print("Invalid! Try Again \n")

# Close the connection to the MySQL database
db.close()
