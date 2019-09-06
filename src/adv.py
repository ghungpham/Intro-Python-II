from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

room['foyer'].items = ['medicine', 'letter', 'dagger']
room['treasure'].items = ['coin', 'one_health', 'sword']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Player1", room['outside'])
current_room = player.current_room 
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

print(" \n Welcome to Adventure Game \n")
print(f" {player.name} is currently at {current_room.name} \n {current_room.description} ")

def move_room():
    items = current_room.items
    sep = ', '
    print(f" \n Player enters {current_room.name} \n {current_room.description}")
    if items:
        print(f' Player finds {sep.join(items)}')
def dead_end():
    print(" \n You cannot move in this direction")

quit = False
while not quit:

    dir = input(f" \n {player.name}, Move (n)orth, (s)outh, (e)ast, (w)est or (q)uit the game: ")
    dir = dir.lower().strip()

   
    if dir == 'q':
        quit = True
    
    elif dir == 'n':
        if current_room.n_to is None:
            dead_end()
        else:
            current_room = current_room.n_to
            move_room()
    
    elif dir == 's':
        if current_room.s_to is None:
            dead_end()
        else:
            current_room = current_room.s_to
            move_room()
    
    elif dir == 'w':
        if current_room.w_to is None:
            dead_end()
        else:
            current_room = current_room.w_to
            move_room()
    
    elif dir == 'e':
        if current_room.e_to is None:
            dead_end()
        else:
            current_room = current_room.e_to
            move_room()
           
    else:
        print(' Direction not available')
    

        
        


#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
