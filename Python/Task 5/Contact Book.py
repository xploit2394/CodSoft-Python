contacts = {}

while True:
    print("\nContact Management System")
    print("----------------------------")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contacts[name] = {"phone": phone, "email": email, "address": address}
        print("Contact added successfully!")

    elif choice == "2":
        if not contacts:
            print("No contacts found!")
        else:
            for name, info in contacts.items():
                print(f"{name} - {info['phone']}")

    elif choice == "3":
        search_term = input("Enter name or phone number to search: ")
        for name, info in contacts.items():
            if search_term in [name, info["phone"]]:
                print(f"Found: {name} - {info['phone']} - {info['email']} - {info['address']}")
                break
        else:
            print("Contact not found!")

    elif choice == "4":
        search_term = input("Enter name or phone number to update: ")
        for name, info in contacts.items():
            if search_term in [name, info["phone"]]:
                info["phone"] = input("Enter new phone number: ")
                info["email"] = input("Enter new email: ")
                info["address"] = input("Enter new address: ")
                print("Contact updated successfully!")
                break
        else:
            print("Contact not found!")

    elif choice == "5":
        search_term = input("Enter name or phone number to delete: ")
        for name, info in contacts.items():
            if search_term in [name, info["phone"]]:
                del contacts[name]
                print("Contact deleted successfully!")
                break
        else:
            print("Contact not found!")

    elif choice == "6":
        break

    else:
        print("Invalid choice. Please try again.")