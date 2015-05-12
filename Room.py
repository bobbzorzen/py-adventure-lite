"""
sdf
"""
import json
from Item import Item

def get_room(room_id):
    """
    sdf
    """
    ret = None
    filename = "rooms/" + str(room_id) + ".json"
    with open(filename, "r") as f:
        jsontext = f.read()
        d = json.loads(jsontext)
        d['id'] = room_id
        ret = Room(d)
    return ret

class Room():
    """
    sdf
    """
    def __init__(self, d):
        """
        sdf
        """
        self.id = d['id']
        self.name = d['name']
        self.description = d['description']
        self.clue = d['clue']
        self.neighbors = d['neighbors']
        self.items = {}
        d['items'] = d['items'] if 'items' in d else []
        for item in d['items']:
            itm = Item(item)
            self.items[itm.name.lower()] = itm
        self.requiredItems = d['requiredItems'] if 'requiredItems' in d else []
        self.deniedText = d['deniedText'] if 'deniedText' in d else []

    def neighbor(self, direction):
        """
        sdf
        """
        if direction in self.neighbors:
            return self.neighbors[direction]
        else:
            return None

    def tryToEnter(self, inventory):
        """
        sdf
        """
        if set(self.requiredItems).issubset(inventory):
            return True
        else:
            print(self.deniedText)
            return False

    def getItems(self):
        """
        sdf
        """
        retArr = []
        for item in self.items:
            retArr.append(self.items[item].name)
        return retArr

    def getItem(self, item):
        """
        sdf
        """
        if item.lower() in (i.lower() for i in self.items):
            return self.items[item.lower()]
        else:
            print("No such item in this room.")
            return False

    def pickup(self, item):
        """
        sdf
        """
        if item.lower() in (i.lower() for i in self.items):
            return self.items[item.lower()].pickup()
        else:
            print("No such item in this room.")

    def kick(self, item):
        """
        sdf
        """
        if item.lower() in (i.lower() for i in self.items):
            return self.items[item.lower()].kick()
        else:
            print("No such item in this room.")

    def north(self):
        """
        sdf
        """
        return self._neighbor('n')
    def south(self):
        """
        sdf
        """
        return self._neighbor('s')
    def east(self):
        """
        sdf
        """
        return self._neighbor('e')
    def west(self):
        """
        sdf
        """
        return self._neighbor('w')
