from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
#map_file = "maps/test_cross.txt"
#map_file = "maps/test_loop.txt"
#map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

visited = set()

backwards_path = []

backwards_directions = {
    "n" : "s",
    "s" : "n", 
    "w" : "e",
    "e" : "w"
}


# run while visited is less than the number of rooms in the world
while len(visited) < len(world.rooms):
    # print('current room', player.current_room.id)
    next_move = None
    possible_exits = []

    for direction in player.current_room.get_exits():
        if player.current_room.get_room_in_direction(direction) not in visited:
            possible_exits.append(direction)
        
    for direction in possible_exits:
            next_move = random.choice(possible_exits)
            break

    if next_move is not None:
        traversal_path.append(next_move)
        backwards_path.append(backwards_directions[next_move])
        player.travel(next_move, True)
        visited.add(player.current_room)
    
    else:
        next_move = backwards_path.pop()
        traversal_path.append(next_move)
        player.travel(next_move)


# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
