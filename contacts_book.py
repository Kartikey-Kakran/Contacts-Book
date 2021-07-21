#First create a dictionary

contact ={
    'Kartikey':[4547614241,'kk154@gmail.com','India'],
    'Abhishek':[7989242245,'abhishek123@gmail.com', 'England'],
    'Ashwani':[4562111885,'assWani@gmail.com', 'Bangladesh'],
    'Parveen':[266547132,'pkhaikya@gmail.com', 'Syria']    
}

# class is blueprint of objects 
# defining a class 
class contacts():
    def add_contact(self):
        name = input("Name: ").title()
        number = input("No.: ")
        Email = input("E-mail: ").lower()
        location = input("Location: ").title()

        self.name = name
        self.number = number
        self.Email = Email
        self.location = location 

        contact[self.name]= self.number, self.Email, self.location
        print("\nContact Added\n")

    def show_contacts(self):
        for key,value in contact.items():
            print(key ," ", value)

    def delete_contact(self):
        self.name = input("Name: ").title()
        if self.name in contact:
            del contact[self.name]
        else:
            print("Contact does not exist")

    def find_contact(self):
        self.name = input("Name").title()
        for key,value in contact.items():
            if key == self.name:
                print(key ," ", value)
            else:
                print("Enter a Valid Contact")
            break
print("\nEnter 1: To add Contact\t\t\tEnter 2: To show Contacts""\nEnter 3: TO delete\t\t\tEnter 4: To find\n")
choice = int(input("Enter:"))

# defining object 

c = contacts()
if choice == 1:
    c.add_contact()
    choose = input("Want to Add Contact? Press Y: ").lower()
    if choose == 'y':
        c.show_contacts()
elif choice == 2:
    c.show_contacts()
elif choice == 3:
    c.delete_contact()
    choose = input("Want to delete Contact: Press Y").lower()
    if choose == 'y':
        c.show_contacts()
elif choice == 4:
    c.find_contact()
else:
    print("Invalid choice")