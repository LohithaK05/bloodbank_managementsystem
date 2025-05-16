import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect("blood_bank.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS donors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        gender TEXT,
        blood_group TEXT,
        contact TEXT
    )
''')
conn.commit()

# Function to add donor
def add_donor():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")
    blood_group = input("Enter blood group: ")
    contact = input("Enter contact: ")
    cursor.execute("INSERT INTO donors (name, age, gender, blood_group, contact) VALUES (?, ?, ?, ?, ?)",
                   (name, age, gender, blood_group, contact))
    conn.commit()
    print("Donor added successfully.")

# Function to view all donors
def view_donors():
    cursor.execute("SELECT * FROM donors")
    donors = cursor.fetchall()
    print("\n--- Donor List ---")
    for donor in donors:
        print(f"ID: {donor[0]}, Name: {donor[1]}, Age: {donor[2]}, Gender: {donor[3]}, Blood Group: {donor[4]}, Contact: {donor[5]}")
    print()

# Function to search donors by blood group
def search_by_blood_group():
    bg = input("Enter blood group to search: ")
    cursor.execute("SELECT * FROM donors WHERE blood_group = ?", (bg,))
    results = cursor.fetchall()
    if results:
        print("\n--- Matching Donors ---")
        for donor in results:
            print(f"ID: {donor[0]}, Name: {donor[1]}, Contact: {donor[5]}")
    else:
        print("No donors found with that blood group.")

# Menu-driven interface
def menu():
    while True:
        print("\n=== Blood Bank Management System ===")
        print("1. Add Donor")
        print("2. View Donors")
        print("3. Search by Blood Group")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_donor()
        elif choice == '2':
            view_donors()
        elif choice == '3':
            search_by_blood_group()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

# Run the menu
menu()

# Close the database connection
conn.close()