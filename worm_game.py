
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = {}
        self.exits = {}
    def add_exit(self, direction, room):
        self.exits[direction] = room
    def has_exit(self, direction):
        return direction in self.exits
    def add_item(self, item):
        self.items[item.name] = item

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Player:
    def __init__(self):
        self.inventory = {}
    def add_item(self, item):
        self.inventory[item.name] = item
    def has_item(self, item_name):
        return item_name in self.inventory

player = Player()
attic = Room("Attic", "A dusty attic with cobwebs in the corners.")
bedroom = Room("Bedroom", "A cozy bedroom with a large bed and a wardrobe.")
attic.add_exit("FORWARD", bedroom)
bedroom.add_exit("BACK", attic)
hallway = Room("Hallway", "A long hallway with several doors leading to other rooms.")
bedroom.add_exit("RIGHT", hallway)
hallway.add_exit("LEFT", bedroom)
bathroom = Room("Bathroom", "A small bathroom with a shower and a sink.")
hallway.add_exit("RIGHT", bathroom)
bathroom.add_exit("LEFT", hallway)
kitchen = Room("Kitchen", "A kitchen with a stove, a fridge, and a sink.")
hallway.add_exit("FORWARD", kitchen)
kitchen.add_exit("BACK", hallway)
garage = Room("Garage", "A garage with a car and some tools.")
kitchen.add_exit("RIGHT", garage)
garage.add_exit("LEFT", kitchen)
front_door = Room("Front Door", "The front door of the house. This is your way out! The door is locked though.")
garage.add_exit("FORWARD", front_door)
front_door.add_exit("BACK", garage)

chocolate = Item("CHOCOLATE", "A delicious bar of chocolate.")
bedroom.add_item(chocolate)
key = Item("KEY", "A small key that might open a door.")
bathroom.add_item(key)
shoe = Item("SHOE", "A single shoe. It looks like it belongs to a child.")
hallway.add_item(shoe)
corwbar = Item("CROWBAR", "A sturdy crowbar that could be used to pry things open.")
garage.add_item(corwbar)


command_instructions = """
Commands:
GO *drection* - move in the direction (back, forward, left, right)
SEEK - look around the room
TAKE *item name* - take an item from the room
QUIT - quit the game
"""
current_room = attic
while True:
    command = input(command_instructions).strip().upper()
    if command == "QUIT":
        print("Thanks for playing!")
        break
    elif command.startswith("GO"):
        direction = command.split()[1]
        if direction in ["BACK", "FORWARD", "LEFT", "RIGHT"]:
            if current_room.name == "Front Door" and direction == "FORWARD":
                if player.has_item("KEY"):
                    print("You use the key to unlock the front door and escape! You win!")
                    break
                else:
                    print("The front door is locked. You need a key to open it.")
            elif current_room.has_exit(direction):
                current_room = current_room.exits[direction]
                print(f"You move {direction.lower()} to the {current_room.name}.")
            else:
                print("You can't go that way.")
    elif command == "SEEK":
        # Print out what is in the room
        # If there is nothing, print that the room is empty
        # If there are items, print their names and descriptions
        if current_room.items != {}:
            print("You see the following items:")
            for item in current_room.items.values():
                print(f"  - {item.name}: {item.description}")
        else:
            print("The room is empty.")
    elif command.startswith("TAKE"):
        item_name = command.split()[1]
        # Check if the item is in the room
        # If it is, add it to the player's inventory
        # If it isn't, print a message saying the item isn't there
        if item_name in current_room.items:
                item = current_room.items.pop(item_name)
                player.add_item(item)
                print(f"You take the {item.name}.")
        else:
            print(f"There is no {item_name} here.")
    else:
        print("Invalid command. Please try again.")








   
       

       
        

        


