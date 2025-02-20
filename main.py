# Marisol Morales & Andreas Moreno, 4/23/24, Lab 11 Decorator Patter

#a role playing character creation program that uses three base types of characters
#(Dwarf, Elf, Halfling). Those characters can then be decorated with four different 
#abilities (Archery, Fighting, Fire, Healing). The program will then display the updated
#stats for the created character

import archery
import check_input
import dwarf
import elf
import fighting
import fire
import halfling
import healing


def main():
    """Main function to create and upgrade RPG characters."""

    print("Character Maker!")

    # Prompt for character type and name
    user_input = check_input.get_int_range(
        "Choose your character:\n1. Dwarf\n2. Elf\n3. Halfling\nEnter Choice: ",1, 3)
    user_name = input("\nWhat is your character's name? ")

    # Create character based on user's choice
    if user_input == 1:
        user_character = dwarf.Dwarf(user_name)
    elif user_input == 2:
        user_character = elf.Elf(user_name)
    else:
        user_character = halfling.Halfling(user_name)

    # Print initial character information
    print(user_character)

    # Initialize remaining ability points
    n = 5

    # Loop to allow user to spend points and upgrade character abilities
    while n != 0:
        abilityChoice = check_input.get_int_range(
            f"\nYou have {n} points to spend:\n"
            "Choose an ability: \n"
            "1. Archery\n"
            "2. Fighting\n"
            "3. Fire Magic\n"
            "4. Healing\n"
            "Enter Ability: ", 1, 4)

        # Upgrade character with chosen ability
        if abilityChoice == 1:
            user_character = archery.Archery(user_character)
        elif abilityChoice == 2:
            user_character = fighting.Fighting(user_character)
        elif abilityChoice == 3:
            user_character = fire.Fire(user_character)
        else:
            user_character = healing.Healing(user_character)

        # Print updated character information
        print("\n")
        print(user_character)

        # Decrement remaining ability points
        n -= 1

    # Check if character creation is successful
    if user_character.constitution() > 0 and user_character.strength() > 0 and user_character.wisdom() > 0:
        print("\nYou have completed your character!")
    else:
        print("\nYou have failed to complete your character!\nAll stats must be greater than 0.\nPlease try again.")

if __name__ == "__main__":
    main()