"""
    Author: Nick
    Date: November 5th, 2024
    Description: Library of functions for my choose your own adventure game.
"""

# Used for the randomness of the game
import random

def showInventory(inventory: list):
    """
    Description:
    Displays the player's current inventory.
    
    Args:
    inventory: list of items the player is carrying

    Returns:
    nothing except a printed list of items
    """
    if inventory:
        print("Your Inventory:")
        for item in inventory:
            print(" • " + item)
    else:
        print("\nYour inventory is empty.")
    print()  # Add a blank line for better readability

def oceanShore(inventory: list):
    """
    Description:
    Starting point of the adventure on the ocean shore. 
    Guides the player to choose a path to proceed with the adventure.
    
    Args:
    inventory: list of items the player is carrying

    Returns:
    str: the next location based on the player's choice
    """
    print("\nYou wake up on a sandy ocean shore. Nobody is quite sure how you got there. Ahead, you see three paths.")
    choice = input("Do you choose the forest trail (1), the cliff path (2), or the shipwreck (3)? ")
    
    if choice.lower() in ["inventory", "i"]:
        showInventory(inventory)
        return "ocean_shore"
    
    # Forest trail: Randomly find an item. Possible items: Mystical Herb, Healing Potion, or nothing
    if choice == "1":
        print("You venture into the misty forest.")
        chance = random.randint(1, 3)
        if chance == 1 and "Mystical Herb" not in inventory:
            print("You find a mystical herb that could come in handy.")
            inventory.append("Mystical Herb")
        elif chance == 2 and "Healing Potion" not in inventory:
            print("You find a Healing Potion hidden under some leaves. Good for you!")
            inventory.append("Healing Potion")
        else:
            print("You find nothing of interest in the forest.")
        return "forest_encounter"
    elif choice == "2":
        if "Ancient Key" not in inventory:
            print("You climb up to the cliff and find an ancient key half-buried in the dirt.")
            inventory.append("Ancient Key")
        else:
            print("You already took the Ancient Key from here before.")
        return "forest_encounter"
    elif choice == "3":
        if "Rusty Dagger" not in inventory:
            print("You search the shipwreck and find a rusty old dagger.")
            inventory.append("Rusty Dagger")
        else:
            print("You already took the Rusty Dagger from here before.")
        return "river_crossing"
    else:
        print("Invalid choice. Try again.")
        return "ocean_shore"

def forestEncounter(name: str, inventory: list):
    """
    Description:
    Forest encounter with a mystical creature blocking the path.
    Provides multiple choices based on the player's inventory.
    
    Args:
    name: the player's name
    inventory: list of items the player is carrying
    
    Returns:
    str: the next location based on the player's choice
    """
    print("\nAs you travel deeper into the forest, the trees grow denser, and a mystical creature blocks your path.")
    available_choices = []
    
    if "Mystical Herb" in inventory:
        print("1. Offer the mystical herb.")
        available_choices.append("1")
    if "Shimmering Amulet" in inventory:
        print("2. Use the shimmering amulet to intimidate the creature.")
        available_choices.append("2")
    if "Rusty Dagger" in inventory:
        print("3. Wield the rusty dagger as a threat.")
        available_choices.append("3")

    if not available_choices:
        print("\nYou realize you have nothing to deal with the creature, " + name + ". With no other choice, you retreat back to the shore.")
        return "ocean_shore"

    print("|^ Here are your option(s); Select wisely. ^|") 
    choice = input("What will you do? ")


    if choice.lower() in ["inventory", "i"]:
        showInventory(inventory)
        return "forest_encounter"
    
    if choice == "1" and "Mystical Herb" in inventory:
        print("The creature sniffs that mystical herb (who knows what it is), nods approvingly, and lets you pass, saying, 'Thank you, " + name + ".'")
        return "mountain_peak"
    elif choice == "2" and "Shimmering Amulet" in inventory:
        print("The creature cowers at the sight of your sick amulet and steps aside, 'Very well, " + name + ", you may proceed.'")
        return "mountain_peak"
    elif choice == "3" and "Rusty Dagger" in inventory:
        if random.randint(1, 2) == 1:
            print("The creature fears your dagger and grudgingly lets you pass, muttering, 'I will remember you, " + name + ".'")
            return "mountain_peak"
        else:
            print("The creature becomes really mad and charges at you. You somehow escape escape, " + name + ".")
            return "ocean_shore"
    else:
        print("You have nothing to offer, " + name + ". The creature chases you away.")
        return "ocean_shore"

def riverCrossing(inventory: list):
    """
    Description:
    River crossing encounter where the player needs a specific item to proceed.

    Args:
    inventory: list of items the player is carrying

    Returns:
    str: the next location based on the player's choice
    """

    print("\nYou arrive at a wide river blocking your path.")
    
    if "Ancient Key" in inventory:
        print("You use the Ancient Key to unlock a small boat and cross the river.")
        return "mysterious_clearing"
    else:
        print("You have no way to cross the river safely, so you decide to return to the shore.")
        return "ocean_shore"

def mysteriousClearing(inventory: list):
    """
    Description:
    Mysterious clearing encounter with a magical barrier blocking the path.
    Requires a specific item to proceed.

    Args:
    inventory: list of items the player is carrying

    Returns:
    str: the next location based on the player's choice
    """

    print("\nYou enter a mysterious creek, but a mystical barrier blocks further progress.")
    
    if "Protection Stone" in inventory:
        print("Your Protection Stone glows, allowing you to pass through the barrier.")
        return "cave_shadows"
    else:
        print("The magical barrier repels you forcefully, sending you back to the forest.")
        return "forest_encounter"

def mountainPeak(inventory: list):
    """
    Description:
    Mountain peak encounter where the player finds ancient relics and clues about the island's secrets.
    Provides two unique items that influence the final ending.
    
    Args:
    inventory: list of items the player is carrying

    Returns:
    str: the next location based on the player's choice
    """
    print("\nAfter a strenuous climb, you reach the peak of a mountain.")
    print("Funny enough, you see an altar with two artifacts: a Sacred Feather and a Mystical Stone.")
    
    choice = input("Do you take the Sacred Feather (1) or the Mystical Stone (2)? ")

    if choice == "1" and "Sacred Feather" not in inventory:
        print("You pick up the Sacred Feather. It feels light and powerful in your hand.")
        inventory.append("Sacred Feather")
    elif choice == "2" and "Mystical Stone" not in inventory:
        print("You pick up the Mystical Stone. It hums with some odd energy.")
        inventory.append("Mystical Stone")
    else:
        print("Invalid choice or item already taken. Try again.")
        return "mountain_peak"
    
    return "cave_shadows"

def caveShadows(inventory: list):
    """
    Description:
    Cave of Shadows encounter with multiple possible endings based on the player's inventory.

    Args:
    inventory: list of items the player is carrying

    Returns:
    str: "end" to signify the conclusion of the adventure
    """
    print("\nYou enter a cave. It's kind of scary, but you're brave, right?")
    
    # Allow the player to choose an item
    choice = input("Do you pick up the *more different* Glowing Stone (1), The Crystal Orb (2), or The Scroll (3)? ")

    if choice.lower() in ["inventory", "i"]:
        showInventory(inventory)
        return "cave_shadows"
    
    # Glowing Stone: Randomly grants Protection Stone or crumbles to dust
    if choice == "1" and "Protection Stone" not in inventory:
        if random.randint(1, 2) == 1:
            print("The stone grants you protection from future harm.")
            inventory.append("Protection Stone")
        else:
            print("The stone crumbles into dust as you pick it up.")
    # Crystal Orb: Grants Insight Orb
    elif choice == "2" and "Insight Orb" not in inventory:
        print("The orb grants you a vision of future paths, giving you insight.")
        inventory.append("Insight Orb")
    # Scroll: Higher chance to grant Escape Spell
    elif choice == "3" and "Escape Spell" not in inventory:
        if random.randint(1, 3) <= 2:  # 2 in 3 chance to obtain Escape Spell
            print("The scroll reveals a powerful spell to escape the island.")
            inventory.append("Escape Spell")
        else:
            print("The scroll’s writing fades as you read it, becoming unreadable.")
    else:
        print("Invalid choice or item already taken. Try again.")
        return "cave_shadows"
    
    # Final encounter with multiple endings
    print("\nAnd for some unknown reason, you find yourself behind an enchanted spirit that doesn't want to go away specifically for you. (how sad...)")
    
    # Define six possible endings
    if "Escape Spell" in inventory and "Ancient Key" in inventory:
        choice = input("Will you use the Escape Spell and Ancient Key to leave the island? (yes/no): ")
        if choice.lower() == "yes":
            print("\nYou use the Ancient Key to unlock a hidden portal and cast the Escape Spell. You've escaped the mystical island! (Ending: Escaped)")
            return "end"
    
    if "Rusty Dagger" in inventory and "Protection Stone" in inventory:
        choice = input("Will you stay back for the island and protect it using your Dagger and Stone (yes/no): ")
        if choice.lower() == "yes":
            print("\nYou leap into the air like a cartoon or something, wielding the rusty Dagger. You are celebrated as a hero by the island's mystical beings. (Ending: Protector)")
            return "end"
    
    if "Insight Orb" in inventory and "Mystical Herb" in inventory:
        choice = input("Will you use the Insight Orb and Mystical Herb to seek wisdom? (yes/no): ")
        if choice.lower() == "yes":
            print("\nThe Insight Orb reveals secrets of the island's past. In the end, you are super intrigued by these secrets just enough to make you remain at the island. (Ending: Seeker/Educator)")
            return "end"

    # Mini Math Puzzle for Healer Ending
    if "Healing Potion" in inventory and "Rusty Dagger" in inventory:
        print("You have a Healing Potion and Dagger, which could help restore balance to the island.")
        print("You go and fight the spirit with the Healing Potion and Dagger. To do this, you must solve a simple math puzzle.")
        
        # Generate a simple random math puzzle
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        num3 = random.randint(1, 20)
        
        # Calculate the correct answer based on the operator
        correct_answer = num1 + num2 - num3
            
        # Ask the puzzle question
        answer = input("What is " + str(num1) + " + " + str(num2) + " - " + str(num3) + "? ")

        # Check the answer to make sure it's a number and correct
        if answer.isdigit() and int(answer) == correct_answer:
            print("\nYou solve the puzzle correctly! The power of the Healing Potion and Dagger flows into the land, restoring balance to the island. (Ending: Healer of the Land)")
            return "end"
        else:
            print("\nYour answer is incorrect. You lose the fight, and the island remains in distress. (Ending: Failed Healer and notice to go back to Grade 1 math)")
            return "end"
    
    if "Sacred Feather" in inventory and not "Ancient Key" in inventory:
        choice = input("Will you use the Sacred Feather to tickle the spirit? (yes/no): ")
        if choice.lower() == "yes":
            print("\nI'm not exactly sure how you expected to tickle a spirit. It didn't work, you just looked silly. You are still stuck on the island. (Ending: Clown)")
            return "end"

    print("\nWith no other options available, you leave the cave. The secrets of the island remain hidden. (Ending: Departed)")
    return "end"