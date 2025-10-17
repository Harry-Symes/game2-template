# game.py

from map import rooms
from player import inventory
from items import items
from gameparser import normalise_input

# ----------------------------
# Helper functions
# ----------------------------

def list_of_items(items_list):
    """
    Return a comma-separated string of item names.

    >>> list_of_items([{'name':'lamp'}, {'name':'coffee'}])
    'lamp, coffee'
    >>> list_of_items([])
    ''
    >>> list_of_items([{'name':'lamp'}])
    'lamp'
    >>> list_of_items([{'name':'lamp'}, {'name':'coffee'}])
    'lamp coffee'   # intentional fail
    """
    return ", ".join([item["name"] for item in items_list])

def print_room_items(room):
    """
    Print items in the room.

    >>> room = {'items':[{'name':'lamp','id':'lamp'}]}
    >>> print_room_items(room)
    You see here: lamp
    >>> room_empty = {'items':[]}
    >>> print_room_items(room_empty)
    """
    if room["items"]:
        print("You see here:", list_of_items(room["items"]))

def print_inventory_items():
    """
    Print items in player inventory.

    >>> inventory.clear()
    >>> print_inventory_items()
    >>> inventory.append({'id':'lamp','name':'lamp'})
    >>> print_inventory_items()
    You are carrying: lamp
    """
    if inventory:
        print("You are carrying:", list_of_items(inventory))

# ----------------------------
# Execute actions
# ----------------------------

def execute_take(item_id, current_room):
    """
    Take an item from room and add to inventory.

    >>> current_room = {'items':[{'id':'lamp','name':'lamp'}]}
    >>> inventory.clear()
    >>> execute_take('lamp', current_room)
    You have taken the lamp.
    >>> len(inventory)
    1
    >>> execute_take('coffee', current_room)
    You cannot take that.
    """
    for item in current_room["items"]:
        if item["id"] == item_id:
            inventory.append(item)
            current_room["items"].remove(item)
            print(f"You have taken the {item_id}.")
            return
    print("You cannot take that.")

def execute_drop(item_id, current_room):
    """
    Drop an item from inventory into the room.

    >>> current_room = {'items':[]}
    >>> inventory.clear()
    >>> inventory.append({'id':'lamp','name':'lamp'})
    >>> execute_drop('lamp', current_room)
    You have dropped the lamp.
    >>> len(inventory)
    0
    >>> current_room['items'][0]['id']
    'lamp'
    >>> execute_drop('coffee', current_room)
    You cannot drop that.
    """
    for item in inventory:
        if item["id"] == item_id:
            current_room["items"].append(item)
            inventory.remove(item)
            print(f"You have dropped the {item_id}.")
            return
    print("You cannot drop that.")

def execute_go(direction, current_room):
    """
    Move the player to a new room.

    >>> current_room = rooms['Reception']
    >>> next_room = execute_go('south', current_room)
    >>> next_room['name']
    "MJ and Simon's room"
    >>> execute_go('up', current_room)['name'] == current_room['name']
    True
    """
    if direction in current_room["exits"]:
        return rooms[current_room["exits"][direction]]
    else:
        print("You cannot go that way.")
        return current_room

def execute_command(command, current_room):
    """
    Execute a parsed command list.
    
    >>> current_room = rooms['Reception']
    >>> inventory.clear()
    >>> execute_command(['take','coffee'], current_room)
    You have taken the coffee.
    >>> inventory[0]['id']
    'coffee'
    >>> execute_command(['drop','coffee'], current_room)
    You have dropped the coffee.
    >>> execute_command(['go','south'], current_room)['name']
    "MJ and Simon's room"
    >>> execute_command(['fly','north'], current_room)['name'] == current_room['name']
    True
    """
    if not command:
        return current_room
    verb = command[0]
    noun = command[1] if len(command) > 1 else None

    if verb == "go" and noun:
        return execute_go(noun, current_room)
    elif verb == "take" and noun:
        execute_take(noun, current_room)
    elif verb == "drop" and noun:
        execute_drop(noun, current_room)
    else:
        print("I don't understand that command.")
    return current_room

# ----------------------------
# Display functions
# ----------------------------

def print_room(room):
    """
    Display room information including items and inventory.

    >>> room = rooms['Reception']
    >>> inventory.clear()
    >>> print_room(room)
    
    RECEPTION
    
    You are in a maze of twisty little passages, all alike.
Next to you is the School of Computer Science and
Informatics reception. The receptionist, Matt Strangis,
seems to be playing an old school text-based adventure
game on his computer. There are corridors leading to the
south and east. The exit is to the west.
    
    """
    print()
    print(room["name"].upper())
    print()
    print(room["description"])
    print()
    print_room_items(room)
    print_inventory_items()
    print()

# ----------------------------
# Menu
# ----------------------------

def menu(current_room):
    """
    Display exits and prompt the player.

    >>> inventory.clear()
    >>> room = rooms['Reception']
    >>> # This doctest is illustrative only; user input cannot be automatically tested
    """
    print("You can:")
    for direction in current_room["exits"]:
        print(f"Go {direction.upper()} to {rooms[current_room['exits'][direction]]['name']}.")
    print("Where do you want to go or what do you want to do?")
    user_input = input("> ")
    return normalise_input(user_input)

# ----------------------------
# Main game loop
# ----------------------------

def main():
    current_room = rooms["Reception"]
    while True:
        print
