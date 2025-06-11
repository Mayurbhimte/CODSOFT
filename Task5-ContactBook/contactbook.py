contacts = []

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    contact = {"Name": name, "Phone": phone, "Email": email}
    contacts.append(contact)
    print("Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts available.\n")
        return
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}")
    print()

def search_contact():
    search_name = input("Enter name to search: ").strip().lower()
    found = False
    for contact in contacts:
        if contact["Name"].lower() == search_name:
            print(f"Found: Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}\n")
            found = True
            break
    if not found:
        print("Contact not found.\n")

def update_contact():
    name_to_update = input("Enter the name of the contact to update: ").strip().lower()
    for contact in contacts:
        if contact["Name"].lower() == name_to_update:
            print("What do you want to update?")
            print("1. Name")
            print("2. Phone")
            print("3. Email")
            choice = input("Enter choice (1/2/3): ")

            if choice == '1':
                new_name = input("Enter new name: ").strip()
                contact["Name"] = new_name
            elif choice == '2':
                new_phone = input("Enter new phone number: ").strip()
                contact["Phone"] = new_phone
            elif choice == '3':
                new_email = input("Enter new email: ").strip()
                contact["Email"] = new_email
            else:
                print("Invalid choice.\n")
                return

            print("Contact updated successfully!\n")
            return
    print("Contact not found.\n")

def delete_contact():
    delete_name = input("Enter name to delete: ").strip().lower()
    for contact in contacts:
        if contact["Name"].lower() == delete_name:
            contacts.remove(contact)
            print("Contact deleted successfully!\n")
            return
    print("Contact not found.\n")

def main():
    while True:
        print("==== Contact Book ====")
        print("1. Add Contact")
        print("2. View Contacts")
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
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Start the contact book
main()