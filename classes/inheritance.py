class Contact:
    all_contacts = []
    
    def __init__(self,name,email) -> None:
       self.name=name
       self.email=email
       Contact.all_contacts.append(self)
       
       
       
       
       
       
       



contact1 =  Contact('Josh','joshw@gmail.com')     
contact2 =  Contact('Homelander','homelander@hotmail.com')  


class Supplier(Contact):
    def order(self,order):
        print(f"We will send  {order} order to {self.name}")
        
        
        
supplier1 = Supplier('Evan','evan21@gmail.com') 

for contact  in Contact.all_contacts:
    print(contact.name, contact.email)
supplier1.order('chicken')     
