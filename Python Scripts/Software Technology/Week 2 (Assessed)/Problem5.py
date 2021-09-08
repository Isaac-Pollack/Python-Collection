"""
Define a business class. Write a constructor (__init__) to set
up the business with initial values including name, address, founding year, email address
and phone number. Write a function called change phone to update the phone number.
"""


class Business:
    def __init__(self, name, address, founded, email, phone):
        self.name = name
        self.address = address
        self.founded = founded
        self.email = email
        self.phone = phone

    def change_phone(self, new_val):  # Override method
        self.phone = new_val
