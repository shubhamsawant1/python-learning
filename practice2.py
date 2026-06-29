
contacts = [
    {"name": "sidan", "phone": "8855-4564", "email": "smsepic10100@gmail.com"},
    {"name": "sidharth", "phone": "8855-5485", "email": "nirag0100@gmail.com"},
    {"name": "siara", "phone": "8855-6598", "email": "simaranc10100@gmail.com"},
    {"name": "simaran", "phone": "8855-1462", "email": "surajsira@gmail.com"},
    {"name": "suraj", "phone": "8855-4897", "email": "smserent@gmail.com"},
    {"name": "virag", "phone": "4568-6621", "email": "sirahyt@gmail.com"},
]

print("\nAll Contacts:\n")

for contact in contacts:
    print(
        f"Contact: {contact.get('name', 'N/A')}  "
        f"Phone: {contact.get('phone', 'N/A')}  "
        f"Email: {contact.get('email', 'N/A')}"
    )

# Search for a contact
search_name = input("\nEnter a name: ").lower()
found = False

for contact in contacts:
    if contact.get("name", "").lower() == search_name:
        print(f"\nFound: {contact.get('name', 'N/A')}")
        print(f"Phone: {contact.get('phone', 'N/A')}")
        print(f"Email: {contact.get('email', 'N/A')}")

        choice = input("\nDo you want to remove something? (yes/no): ").lower()

        if choice == "yes":
            remove_this = input(
                "Enter what you want to remove "
                "(name, phone, email, full_contact): "
            ).lower()

            if remove_this in ["name", "phone", "email"]:
                del contact[remove_this]
                print(f"{remove_this.capitalize()} removed successfully!")

            elif remove_this == "full_contact":
                contacts.remove(contact)
                print("Contact removed successfully!")

            else:
                print("Invalid choice.")

        found = True
        break

if not found:
    print(f"\n'{search_name}' not found in contacts.")

print("\nUpdated Contacts:\n")


for contact in contacts:
    print(
        f"Contact: {contact.get('name', 'N/A')}  "
        f"Phone: {contact.get('phone', 'N/A')}  "
        f"Email: {contact.get('email', 'N/A')}"
    )