from uuid import uuid4
import json

class User:
    def __init__(self,fname,lname,dob,username,email,phone, password):
        self.user_id = str(uuid4())
        self.fname = fname
        self.lname = lname
        self.dob = dob
        self.username = username
        self.email = email
        self.phone = phone
        self.password = password
        self.newUser()
        
    
    def getUserID(self):
        return self.user_id
    
    # adds a new user to the json file
    def newUser(self):
        user = {
            "user_id": self.user_id,
            "fname": self.fname,
            "lname": self.lname,
            "dob": self.dob,
            "username": self.username,
            "email": self.email,
            "phone": self.phone,
            "password": self.password
        }
        
        # Step 1: Load existing JSON data (if any)
        try:
            with open("data.json", "r") as json_file:
                existing_data = json.load(json_file)
        except FileNotFoundError:
            existing_data = []

        # Step 2: Append new data to existing data
        existing_data.append(user)
        
        # Step 3: Write JSON data to file
        with open("data.json", "w") as json_file:
            json.dump(existing_data, json_file, indent=4)
        
    def deleteUser(self):
        pass
        
    