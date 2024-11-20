"""
    Author: Nick
    Date: Nov 18, 2024
    Description: Test program to demonstrate *2* person objects.
"""

import myModule

def main():
    """This function demonstrates the use of 2 Person objects"""
    mr_sam = myModule.Person("Mr. Sam", 50)
    nick = myModule.Person("Nick", 20)
        
    mr_sam.introduceSelf()
    print(mr_sam.getName(), "says \"" + mr_sam.giveRandomAdvice() + "\"")

    nick.introduceSelf()
    print(nick.getName(), "says \"" + nick.giveRandomAdvice() + "\"")

    print("\nprint() calls __str__() method automatically:")
    print(mr_sam)
    print(nick)

    print("\nTrying to set age for mr rao to 150.")
    mr_sam.setAge(150)
    print("Age is now:", mr_sam.getAge())

    print("\nTrying to set age for nick to 25.")
    nick.setAge(25)
    print("Age is now:", nick.getAge())

    print("\nTrying to set name to empty string for both people.")
    mr_sam.setName("")
    nick.setName("")
    print("Name is now: (sam)", mr_sam.getName())
    print("Name is now: (nick)", nick.getName())
    
# Call the main function.
main()
