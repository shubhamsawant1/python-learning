contacts = [

        {"name": "sidan", "phone": "8855-4564", "email": "smsepic10100@gmail.com"},
        {"name": "sidharth", "phone": "8855-5485", "email": "nirag0100@gmail.com"},
        {"name": "siara", "phone": "8855-6598", "email": "simaranc10100@gmail.com"},
        {"name": "simaran", "phone": "8855-1462", "email": "surajsira@gmail.com"},
        {"name": "suraj", "phone": "8855-4897", "email": "smserent@gmail.com"},
        {"name": "virag", "phone": "4568-6621", "email": "sirahyt@gmail.com"},
       

    ]

print("\nAll contacts: \n")

for contact in contacts:
    print(f"     Contact:{contact["name"]}  Phone:{contact["phone"]} Email:{contact["email"]} ")

# search for a contact

search_name = str(input("Enter a name: "))
found = False
for contact in contacts:
    if contact["name"] == search_name:
        print(f"\nFound: {search_name}")
        print(f"  Phone: {contact['phone']}")
        print(f"  email: {contact["email"]}")
        choise = str(input("do you want to remove this name(yes / no): "))
        if choise == "yes":
            remove_this = str(input("Enter what you want to remove(name, phone, mail , full_contact): ")).lower()
            if remove_this in ["name" , "phone" , "email"]:
                del contact[remove_this]
                print(f"{remove_this} this successfully!")
            elif remove_this == "full_contact": 
             contacts.remove(contact)
            else: 
                print("remove choise is not valid: ")
          

        found = True
        break

if not found:
    print(f"\n{search_name} not found in contacts")

for contact in contacts:
    print(f"     {contact["name"]}  {contact["phone"]} {contact["email"]}")
