"""
    Author: Nick
    Date: Nov 19th, 2022
    Description: This module will contain classes that I create so that they can be easily reused in different programs.
"""

import random

class Person:
    '''This class is used to model a Person object (with a name and age).'''
    
    def __init__(self, name, age):
        '''This initializer method accepts a name (string) and age (int) 
        for a new Person object, and sets its instance variables.
        This method returns nothing.'''
        self.name = name
        self.age = age

    def introduceSelf(self):
        '''This method will *display* the Person's name and 
        age as if introducing him/herself to someone. 
        This method has no parameters, and returns nothing.'''
        print("My name is", self.name, "and I am", self.age,"years old.")

    def giveRandomAdvice(self):
        '''This method will *return* one of 3 random pieces of advice;
        e.g., "Don't give up!", "Always work hard!", or "Floss everyday!". 
        This method has no parameters, and returns nothing.'''
        advice = [ "Don't give up!", "Always work hard!", "Floss everyday!" ]
        return advice[random.randint(0,2)]

    def getName(self):
        '''This accessor method returns the value of the name instance variable.'''
        return self.name

    def getAge(self):
        '''This accessor method returns the value of the age instance variable.'''
        return self.age

    def setName(self, name):
        '''This mutator method accepts a name (string) as a parameter 
        and sets the value of the name instance variable for the Person object.  
        If an empty string is given, the default name will be set to <No name given!>. '''
        if name:
            self.name = name
        else:
            self.name = "<No name given!>"

    def setAge(self, age):
        '''This mutator method accepts a age (int) as a parameter 
        and sets the value of the name instance variable for the Person object.  
        If age is invalid (i.e., < 1 or > 121), the default age will be set to 29. '''
        if age < 1 or age > 121 :
            self.age = 29
        else:
            self.age = age
                  
    def __str__(self):
        '''This method returns a string representation of a Person object.'''
        return "Person object with name = " + self.name + " and age = " + str(self.age)


class Student(Person):
    '''This class is used to model a Student object (with a student id).'''
    
    def __init__(self, name, age, student_id):
        # ADD a proper docstring and code for this initializer
        # Hint #1: Don't forget to call __init__() method in Person class to set name and age for you.
        # Hint #2: student_id is a unique instance variable for Student objects
        '''This initializer method accepts a name (string), age (int), and student_id (int)'''
        # inhwerit from the Person class
        Person.__init__(self, name, age)
        self.student_id = student_id


    def giveRandomAdvice(self):
        '''This method will *return* one of 3 random pieces of advice'''
        advice = [ "Don't give up!", "Always work hard!", "Floss everyday!" ]
        return advice[random.randint(0,2)]

    # ADD a mutator method here for the student_id instance varaible.
    def setStudentId(self, student_id):
        '''This mutator method accepts a student_id (int) as a parameter 
        and sets the value of the student_id instance variable for the Student object.  
        If student_id is invalid (i.e., < 1000 or > 9999), the default student_id will be set to 9999. '''
        if student_id < 1000 or student_id > 9999 :
            self.student_id = 9999
        else:
            self.student_id = student_id

    # ADD an accessor method here for the student_id instance varaible.
    def getStudentId(self):
        '''This accessor method returns the value of the student_id instance variable.'''
        return self.student_id
    
    def __str__(self):
        '''This method returns a string representation of a Student object.'''
        return "Student object with name = " + self.name + " and age = " + str(self.age) + " and id = " + str(self.student_id)
