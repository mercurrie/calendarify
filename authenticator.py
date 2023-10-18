from hashlib import sha256
from user_profile import User
import json

class UserAuthentication:
    def __init__(self):
        pass

    # Register a new user
    def registerUser(self, fName, lName, dob, username, email, phone, password):
        # Check if the username is already in use
        try:
            with open("data.json", "r") as jsonFile:
                existingData = json.load(jsonFile)
        except FileNotFoundError:
             existingData = []
    
        usernameExists = any(user.get("username") == username for user in existingData)
        
        if usernameExists:
            return "Username already exists. Please choose another one."

        # Hash the password using a secure hashing algorithm (e.g., SHA-256)
        passwordHash = sha256(password.encode()).hexdigest()

        # Create a new user object
        User(fName, lName, dob, username, email, phone, passwordHash)

        return "Registration successful. You can now log in."

    # Authenticate a user
    def login(self, username, password):
        # Check if the username exists in the database
        if username in self.userDatabase:
            user = self.userDatabase[username]

            # Verify the password by comparing the hashed password
            if user.password == sha256(password.encode()).hexdigest():
                return user  # Successfully authenticated

        return None  # Authentication failed

    
# test
# user = UserAuthentication()
# user.registerUser("John", "Doe", "01/01/2000", "mewfwkjn", "johndoe@ymail.com", "1234567890", "password")