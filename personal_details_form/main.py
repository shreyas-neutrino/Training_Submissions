# this is the global list in which l the person details are saved
# ths list stores the objects of Person class
person_list = []

#person class structure of person objects
class Person:
    def __init__(self,name,age,address,mobileNumber):
        self.name = name
        self.age = age
        self.address = address
        self.mobileNumber = mobileNumber
    def __str__(self):
        return f"\nname : {self.name}\n age : {self.age}\n address : {self.address}\n mobilenumber : {self.mobileNumber}\n"


#main class to start the program
def main():
    # person_list = []
    print("welcome user plaese select from the below options!!\n")
    interface()

#  add_new_user fucton asks user to input personal details and creates
#  a new person object which is then appended to the person_list
def add_new_user():
    name = input("enter name : ")  
    age = int(input("enter users age : ")) 
    address = input("enter users address : ")
    mobileNumber = input("enter users mobile numer : ")
    person = Person(name,age,address,mobileNumber)
    person_list.append(person)
    print("new user added successfully\n")

#  this function searches for the person in the person_list for a record with the same name
def find_existing_user():
    print("enter name of the person to find....")
    name = input()
    for person in person_list:
        if person.name == name:
            return person
        else:
            print(f"no user with name {name} present in the database")
            


    
#  this defines the command line interface the user interacts with            
def interface():
    print("[1]  add new person/user!\n[2]  find existing Person/User!\n[3]  exit the iterface\n")
    option = int(input("enter option number\n"))

    match option:
         case 1:
             add_new_user()
             interface()
         case 2:
             person = find_existing_user()
             print(person)
             interface()
         case 3:
             print("okay then byeeee!!!!")
         case _:
             print("enter appropriate option number")
             interface()

main()