import sys 
# this function will  be the first to run as the main function executes
def initial_phonebook():
      rows, cols = int(input("Please enter initial number of contacts.")), 5
      phone_book = []
      print(phone_book)
      for i in range(rows):
            print("\nEnter contact %d details in the following order (ONLY):" % (i+1))
            print("Note: * indicates mandatory fields")

            print("........................................")
            temp = []
            for j in range(cols):
                   if j == 0:
                        temp.append (str(input("Enter Name*: ")))
                        if temp[j] == '' or temp[j] == '':
                              sys.exit
                              "Name is mandatory field process exiting due to blank field"
                   if j == 1:
                         temp.append (int(input("Enter Number*: ")))
                   if j == 2:
                        temp.append (str(input("Enter E-mail address*: ")))
                        if temp[j] == '' or temp[j] == '':
                              temp[j] = None
                   if j == 3:
                        temp.append (str(input("Enter Date of Birth(dd/mm/yy): ")))
                        if temp[j] == '' or temp[j] == '':
                              temp[j] = None
                   if j == 4:
                         temp.append (
                             str(input("Enter Category(Family,Friends,Work,Others): ")))
                         if temp[j] == '' or temp[j] == '':
                                  temp[j] = None
            phone_book.append(temp)
      print(phone_book)
      return phone_book
                                 
                        
                          
                          
                        

def menu():
      print("**********************************************************************************")
      print("\t\t\tSMARTPHONE DIRECTORY", flush=False)
      print("**********************************************************************************")
      print("\t You can perform the following operations in the phone book\n")
      print("1.Add  a new  contact")
      print("2.Rem ove  an existing contact")
      print("3.Delete all  contacts")
      print("4.Search  for a  contact")
      print("5.Display all contacts")
      print("6.Exit Phonebook")

      choice= int(input("Please enter your  choice"))
      return  choice



def add_contact(pb):
def remove_existing(pb):
def delete_all(pb):
def search_existing(pb):
def display_all(pb):
def thanks():
  print("********************************************************************")
  print("Thank you for using our smartphone directory system")
  print("Please visit again!")
  print("********************************************************************")
  sys.exit("Goodbye have a nice time ahead")
  

print("........................................")
print("Hello dear user welcome to our smarttphone directory system")
print("You may now proceed to explore this directory")
print("........................................")

ch = 1
pb = initial_phonebook()
while ch in (1,2,3,4,5):
 ch = menu()
 if ch == 1: 
   pb = add_contact(pb)
 elif ch == 2:
   pb = remove_existing(pb)
 elif ch == 3:
   pb = delete_all(pb)
 elif ch == 4:
   d = search_existing(pb)
   if d == -1
     print("The contact does not exist please try again")
 elif ch == 5:
   display_all(pb)
 else:
   thanks()
    

        
