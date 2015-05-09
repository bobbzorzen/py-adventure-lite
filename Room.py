import json
from Item import Item

def get_room(id):
    ret = None
    filename = "rooms/" + str(id) + ".json"
    with open(filename, "r") as f:
        jsontext = f.read()
        d = json.loads(jsontext)
        d['id'] = id
        ret = Room(**d)
    return ret

class Room():
    def __init__(self, id=0, name="A Room", description="An empty room", clue="This rooms seems useless", neighbors={}, items=[], requiredItems=[], deniedText="The path is blocked"):
        self.id = id
        self.name = name
        self.description = description
        self.clue = clue
        self.neighbors = neighbors
        self.items = {}
        for item in items:
            itm = Item(**item)
            self.items[itm.name.lower()] = itm
        self.requiredItems = requiredItems
        self.deniedText = deniedText

    def _neighbor(self, direction):
        if direction in self.neighbors:
            return self.neighbors[direction]
        else:
            return None

    def tryToEnter(self, inventory):
        if set(self.requiredItems).issubset(inventory):
            return True
        else:
            print(self.deniedText)
            return False

    def getItems(self):
        retArr = []
        for item in self.items:
            retArr.append(self.items[item].name)
        return retArr

    def getItem(self, item):
        if item.lower() in (i.lower() for i in self.items):
            return self.items[item.lower()]
        else:
            print("No such item in this room.")
            return False

    def pickup(self, item):
        if item.lower() in (i.lower() for i in self.items):
            return self.items[item.lower()].pickup()
        else:
            print("No such item in this room.")

    def kick(self, item):
        if item.lower() in (i.lower() for i in self.items):
            return self.items[item.lower()].kick()
        else:
            print("No such item in this room.")

    def north(self):
        return self._neighbor('n')
    def south(self):
        return self._neighbor('s')
    def east(self):
        return self._neighbor('e')
    def west(self):
        return self._neighbor('w')