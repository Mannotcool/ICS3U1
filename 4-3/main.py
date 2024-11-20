"""
    Author: Nick
    Date: Nov 19, 2024
    Description: Test program to demonstrate a Student object.
"""

import myModule

def main():
    """This function demonstrates the use of 1 Student object"""   
    # ADD code here to demonstrate all of the methods inherited from the Person class
    nick = myModule.Student("Nick", 20, 123)
        
    nick.introduceSelf()
    print(nick.getName(), "says \"" + nick.giveRandomAdvice() + "\"")

    print("\nTrying to set age for nick to 25.")
    nick.setAge(25)
    print("Age is now:", nick.getAge())

    print("\nTrying to set name to James..")
    nick.setName("James")
    print("Name is now: (nick)", nick.getName())

    # ADD code here to demonstrate all of the methods unique to student objects
    print("\nTrying to set student number to 12345.")
    nick.setStudentId(12345)
    print("Student number is now:", nick.getStudentId())
    
    # get student id
    print("\nTrying to get student id.")
    print("Student id is:", nick.getStudentId())
    
    # ADD code here to demonstrate the overridden methods giveRandomAdvice() and __str__() in the Student class
    print("\nOverridden giveRandomAdvice() method:")
    print(nick.giveRandomAdvice())

    print("\nprint() calls __str__() method automatically:")
    print(nick)


# Call the main function.
main()
