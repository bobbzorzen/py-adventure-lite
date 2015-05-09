import cmd
from Room import get_room
import textwrap
import os
class Game(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.items = []
        self.destroyedItems = []
        self.loc = get_room(1)
        self.look()

    """def precmd(self, line):
        os.system('cls')
        os.system('clear')
        print("(Cmd) " + line)
        return cmd.Cmd.precmd(self, line)
    """
    def move(self, dir):
        newroom = self.loc._neighbor(dir)
        if newroom is None:
            print("You can't go that way")
        else:
            tmp = get_room(newroom)
            if tmp.tryToEnter(self.items):
                self.loc = tmp
                self.look()

    def look(self):
        print(self.loc.name)
        print("")
        for line in textwrap.wrap(self.loc.description, 72):
            print(line)

    def do_n(self, args):
        """Goes north"""
        self.move('n')

    def do_s(self, args):
        """Goes south"""
        self.move('s')

    def do_w(self, args):
        """Goes west"""
        self.move('w')

    def do_e(self, args):
        """Goes east"""
        self.move('e')

    def do_pickup(self, args):
        """Picks up the given item"""
        if args == "":
            print("You need to tell me which item i should pick up.")
            return 0
        if args.lower() in (item.lower() for item in self.items):
            print(args + " is already in Twoflower's chest...")
        else:
            item = self.loc.pickup(args)
            if item == None:
                pass
            else:
                self.items.append(item)

    def do_kick(self, args):
        if args == "":
            print("You can't just kick thin air, be more specific!")
            return 0
        if args.lower() in (item.lower() for item in self.destroyedItems):
            print("Don't be too eager.. You've already kicked this item into oblivion")
        else:
            item = self.loc.kick(args)
            if not item:
                pass
            else:
                if item == "Bel-Shamharoth":
                    print("You've defeated the immortal Bel-Shamharoth. You win at life(and this game).")
                    exit(0)
                self.destroyedItems.append(item)

    def do_items(self, args):
        """Displays all the items in the room"""
        items = self.loc.getItems()
        if len(items) == 0:
            print("This room seems to be completely empty")
        else:
            tmpList = []
            for item in items:
                if (item not in self.items) and (item not in self.destroyedItems):
                    tmpList.append(item)
            if len(tmpList) == 0:
                print("This room seems to be completely empty")
            print(", ".join(tmpList))

    def do_inventory(self, args):
        """Prints the current inventory"""
        if len(self.items) == 0:
            print("Your inventory is empty, why not pick up something?")
        else:
            print("Twoflower's chest currently holds: ")
            print(", ".join(self.items))
    def do_look(self, args):
        """Looks around the room or at a specific item"""
        if args == "":
            self.look()
        else:
            item = self.loc.getItem(args)
            if item != False:
                print(item.description)

    def do_clue(self, args):
        """Prints a clue for the current room"""
        print("You ask Twoflower for his opinion of your current situation.")
        print(self.loc.clue)

    def do_clear(self, args):
        """Clears the screen"""
        os.system('cls')
        os.system('clear')

    def do_quit(self, args):
        """Quits the game"""
        exit()
    def do_exit(self, args):
        """Quits the game"""
        exit()

    def exit():
        print("thanks for playing")
        return True

if __name__ == '__main__':
    g= Game()
    g.cmdloop()