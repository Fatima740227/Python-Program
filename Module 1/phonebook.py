# this function will  be the first to run as the main function executes
def initial_phonebook():

def menu():
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
    

        
