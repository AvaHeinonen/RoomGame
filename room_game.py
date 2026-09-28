
command_instructions = """
    You can use the following commands:
    LEFT: go left,
    RIGHT: go right,
    BACK: go back,
    FORWARD: go forward,
    QUIT: quit the game
"""

class Room:
    """Represents a room in the game map.

    The class stores the name and description of each room, and the exists from the room
    to other rooms. 
    It allows for checking if a room has an exit to a specific direction, and 
    getting the next room in a direction.

    Attributes:
        name (str): Name of the room.
        description (str): Description of the room.
        exits (dict): A dictionary mapping directions to other Room objects.
    """
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
    def add_exit(self, direction, room):
        self.exits[direction] = room
    def has_exit(self, direction):
        return direction in self.exits
    def get_next_room(self, direction):
        return self.exits.get(direction)

class Map:
    """Represents the game map.
    
        The class stores the rooms in the game map, and the player's current room.
        It allows for generating the rooms at the beginning of the game, and moving between rooms. 
    
        Attributes:
            rooms (dict): rooms on the game map
            current_room (Room): player's current room
        """
    def __init__(self):
        self.rooms = self.generate_map()
        self.current_room = self.rooms["attic"] 
    def generate_map(self):
        """Generates the game map with rooms and their exits."""
        rooms = {}
        rooms["attic"] = Room("Attic", "A dusty attic with cobwebs in the corners.")
        rooms["bedroom"] = Room("Bedroom", "A cozy bedroom with a large bed and a wardrobe.")
        rooms["hallway"] = Room("Hallway", "A long hallway with several doors leading to other rooms.")
        rooms["bathroom"] = Room("Bathroom", "A small bathroom with a shower and    a sink.")
        rooms["kitchen"] = Room("Kitchen", "A kitchen with a stove, a fridge, and a sink.")
        rooms["garage"] = Room("Garage", "A garage with a car and some tools.")
        rooms["front_door"] = Room("Front Door", "The front door of the house. This is your way out! The door is locked though.")

        rooms["attic"].add_exit("FORWARD", rooms["bedroom"])
        rooms["bedroom"].add_exit("RIGHT", rooms["hallway"])
        rooms["bedroom"].add_exit("BACK", rooms["attic"])

        rooms["hallway"].add_exit("LEFT", rooms["bedroom"])
        rooms["hallway"].add_exit("RIGHT", rooms["bathroom"])
        rooms["hallway"].add_exit("FORWARD", rooms["kitchen"])

        rooms["bathroom"].add_exit("LEFT", rooms["hallway"])
     
        rooms["kitchen"].add_exit("BACK", rooms["hallway"])
        rooms["kitchen"].add_exit("RIGHT", rooms["garage"])

        rooms["garage"].add_exit("LEFT", rooms["kitchen"])
        rooms["garage"].add_exit("FORWARD", rooms["front_door"])
        return rooms
    def move(self, direction):
        if self.current_room.has_exit(direction):
            self.current_room = self.current_room.get_next_room(direction)
            print(f"You move {direction} to {self.current_room.name}")
        else:
            print(f"Cannot move that way")
  
      

## Main program
## Generates the game map, and runs the game loop
map = Map()

## Game loop
## Asks the user for commands repeatedly until user reaches the front door, or they
## decide to quit the game
while True:
    command = input(command_instructions).strip().upper()
    if command == "QUIT":
        print("Thanks for playing!")
        break
    elif command in {"LEFT", "RIGHT", "BACK", "FORWARD"}:
            map.move(command)
            if map.current_room.name == "Front Door":
                print("You have reached the front door! You win!")
                break
    else:
        print("Invalid command. Please try again.")








   
       

       
        

        


