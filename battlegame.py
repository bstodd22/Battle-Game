wizard = "Wizard"
wizard_hp = 70
wizard_damage = 150

elf = "Elf"
elf_hp = 100
elf_damage = 100

human = "Human"
human_hp = 150
human_damage = 20

orc = "Orc"
orc_hp = 115
orc_damage = 100

dragon_hp = 300
dragon_damage = 50

while True:
    print(
        """
1) Wizard
2) Elf
3) Human
4) Orc
5) Exit
      """
    )
    choice = input("Choose your character: ")
    choice = int(choice)
    if choice == 1:
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif choice == 2:
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif choice == 3:
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    elif choice == 4:
        character = orc
        my_hp = orc_hp
        my_damage = orc_damage
        break
    elif choice == 5:
        exit()
    else:
        print("Unknown character")

print(
    f"""
You have chosen the character: {character}
Health: {my_hp}
Damage: {my_damage}
      """
)

while True:
    dragon_hp -= my_damage
    print(f"The {character} damaged the Dragon!")
    print(f"The Dragon's hitpoints are now: {dragon_hp}\n")

    if dragon_hp <= 0:
        print("The Dragon has lost the battle")
        break

    my_hp -= dragon_damage
    print(f"The Dragon has damaged the {character}!")
    print(f"The {character}'s hitpoints are now: {my_hp}\n")

    if my_hp <= 0:
        print(f"The {character} has lost the battle")
        break
