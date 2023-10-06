from uuid import uuid4

class User:
    def __init__(self,fname,lname,dob,uuid,username,email,phone):
        self.fname = fname
        self.lname = lname
        self.dob = dob
        self.username = username
        self.email = email
        self.phone = phone
    def uuid_creation(username):
    # Check if uuid exists
    uuid = uuid3(NAMESPACE_OID.NAMESPACE_OID, username)
    # if exists recrea