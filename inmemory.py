from contact import Contact
from beautifultable import BeautifulTable
class InMemoryImpl:
    contact_list=[]
    @classmethod
    def addContact(cls):
        name=input("Enter the name:")
        email=input("Enter the email:")
        mobile=input("Enter the mobile:")
        address=input("Enter the address:")
        cls.contact_list.append(Contact(name,email,mobile,address))
        print(f"Contact is added successfully with the name {name}")
    @classmethod 
    def deleteContact(cls):
        name=input("Enter the name to delete:")
        contact=cls.get_contact_by_name(name)
        if contact:
            cls.contact_list.remove(contact)
            print(f"Contact {name} is deleted successfully...")
            InMemoryImpl._paint(cls.contact_list)
        else:
            print(f"Contact with name")
    @classmethod 
    def viewContact(cls):
        
        InMemoryImpl._paint(cls.contact_list)
    @classmethod
    def search(cls): 
        if len(cls.contact_list)>0:
            name=input("Enter the name to search:")
            s_list = list(filter(lambda x:name.lower() in x.get__name().lower(),cls.contact_list))
            if len(s_list)>0:
                InMemoryImpl._paint(s_list)
            else:
                print(f"there is no data found with the given search")
        else:
           print("Contact book is empty!...you can't do search...")

    @classmethod 
    def updateContact(cls):
        name = input("Enter the name to update:")
        contact = cls.get_contact_by_name(name)
        if contact:
            print("1.name 2.Email 3.Mobile 4.Address")
            ch=int(input("Enter your choice:"))
            if ch == 1:
                print(f"Old Name :{contact.get__name()}")
                name= input("Enter the new Name:")
                if name:
                    contact.set__name(name)
            elif ch == 2:
                print(f"Old Email :{contact.get__email()}")
                email= input("Enter the new Email:")
                if email:
                    contact.set__email(email)
            elif ch == 3:
                print(f"Old Mobile :{contact.get__mobile()}")
                mobile= input("Enter the new Mobile:")
                if mobile:
                    contact.set__mobile(mobile)
            else:
                print(f"Old Address :{contact.get__address()}")
                address= input("Enter the new Address:")
                if address:
                    contact.set__address(address)
        else:
            print(f"Contact is not found with the given name:{name}")
            
            
    @staticmethod 
    def _paint(lst):
        if len(lst) != 0:
            table = BeautifulTable()
            table.column_headers = ["Name", "Email", "Mobile", "Address"]
            for c in lst:
                table.append_row([c.get__name(),c.get__email(),c.get__mobile(),c.get__address()])
            print(table)
        else:
            print(f"contact table is empty!...")
    @classmethod
    def get_contact_by_name(cls,name):
       if len(cls.contact_list)>0:
          contact = list(filter(lambda x:x.get__name().lower() == name.lower(),cls.contact_list))
          return contact[0] if contact else None
    
    
