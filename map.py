# map.py

from items import lamp, notebook, coffee

room_reception = {
    "name": "Reception",
    "description": "You are in the reception. Matt is here.",
    "exits": {"south": "Admins", "east": "Tutor", "west": "Parking"},
    "items": [coffee]
}

room_admins = {
    "name": "MJ and Simon's room",
    "description": "Inside the systems managers' room.",
    "exits": {"north": "Reception"},
    "items": [notebook]
}

room_tutor = {
    "name": "your personal tutor's office",
    "description": "Your tutor is here staring at his monitor.",
    "exits": {"west": "Reception"},
    "items": []
}

room_parking = {
    "name": "the parking lot",
    "description": "The Queen's Buildings parking lot.",
    "exits": {"south": "Reception", "east": "Office"},
    "items": []
}

room_office = {
    "name": "the general office",
    "description": "Next to the cashier's till.",
    "exits": {"west": "Parking"},
    "items": [lamp]
}

rooms = {
    "Reception": room_reception,
    "Admins": room_admins,
    "Tutor": room_tutor,
    "Parking": room_parking,
    "Office": room_office
}
