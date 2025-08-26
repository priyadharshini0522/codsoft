contacts = []

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("\n Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("\nNo contacts found!\n")
        return
    print("\n📒 Contact List:")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
    print()

def search_contact():
    keyword = input("Enter Name or Phone to search: ")
    found = False
    for contact in contacts:
        if contact['name'] == keyword or contact['phone'] == keyword:
            print("\n Contact Found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")
            found = True
    if not found:
        print("\n  No contact found!\n")

def update_contact():
    keyword = input("Enter the Name of the contact to update: ")
    for contact in contacts:
        if contact['name'] == keyword:
            print("\nEnter new details (leave blank to keep old):")
            new_name = input(f"Name ({contact['name']}): ") or contact['name']
            new_phone = input(f"Phone ({contact['phone']}): ") or contact['phone']
            new_email = input(f"Email ({contact['email']}): ") or contact['email']
            new_address = input(f"Address ({contact['address']}): ") or contact['address']

            contact['name'] = new_name
            contact['phone'] = new_phone
            contact['email'] = new_email
            contact['address'] = new_address

            print("\n Contact updated successfully!\n")
            return
    print("\n Contact not found!\n")

def delete_contact():
    keyword = input("Enter the Name of the contact to delete: ")
    for contact in contacts:
        if contact['name'] == keyword:
            contacts.remove(contact)
            print("\n Contact deleted successfully!\n")
            return
    print("\n Contact not found!\n")

def menu():
    while True:
        print("=====  Contact Management System =====")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("\n Exiting Contact Management System. Goodbye!")
            break
        else:
            print("\n Invalid choice! Please try again.\n")


menu()
