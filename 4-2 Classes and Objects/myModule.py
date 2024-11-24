"""
    Author: Nick
    Date: Nov 18, 2024
    Description: Test module used by main to demonstrate the person class.
"""

import random

class Person:
    '''This class is used to model a Person object (with a name and age).'''
    
    def __init__(self, new_name, new_age):
        '''This initializer method accepts a new_name (string) and new_age (int) 
        for a new Person object, and sets its instance variables.
        This method returns nothing.'''
        self.name = new_name
        self.age = new_age

    def introduceSelf(self):
        '''This method will *display* the Person's name and 
        age as if introducing him/herself to someone. 
        This method has no parameters, and returns nothing.'''
        print("Hello, my name is", self.name, "and I am", self.age, "years old.")

    def giveRandomAdvice(self):
        '''This method will *return* one of 3 random pieces of advice;
        e.g., "Don't give up!", "Always work hard!", or "Floss everyday!". 
        This method has no parameters and returns an advice string.'''
        advice = ["Don't give up!", "Always work hard!", "Floss everyday!"]
        return random.choice(advice)

    def getName(self):
        '''This accessor method returns the value of the name instance variable.'''
        return self.name

    def getAge(self):
        '''This accessor method returns the value of the age instance variable.'''
        return self.age

    def setName(self, new_name):
        '''This mutator method accepts a new_name (string) as a parameter 
        and sets the value of the name instance variable for the Person object.  
        If an empty string is given, the default name will be set to <No name given!>. '''
        if new_name != "":
            self.name = new_name
        else:
            self.name = "<No name given!>"

    def setAge(self, new_age):
        '''This mutator method accepts a new_age (int) as a parameter 
        and sets the value of the age instance variable for the Person object.  
        If age is invalid (i.e., < 1 or > 121), the default age will be set to 29. '''
        if new_age > 0 and new_age < 121:
            self.age = new_age
        else:
            self.age = 29
                  
    def __str__(self):
        '''This method returns a string representation of a Person object.'''
        return "Person object with name = " + self.name + " and age = " + str(self.age)
