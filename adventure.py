"""
sasd
"""
import cmd
from Room import get_room
import textwrap
import os
import sys
import getopt

#
# Information about script
#

PROGRAM = os.path.basename(sys.argv[0])
AUTHOR = "Leopold (Bobbzorzen) Olsson"
EMAIL = "bobbzorzen@gmail.com"
VERSION = "1.0.0"
USAGE = """{program} - Interactive fiction in python. By {author} ({email}), version {version}.
Usage:
  {program} [options]
Options:
  -h --help                      Display this help message.
  -i --info                      Prints information about the game
  -v --version                   Print version and exit.
  -a --about                     Prints information about {author}
  -c --cheat                     Prints the shortest way to complete the game
""".format(program=PROGRAM, author=AUTHOR, email=EMAIL, version=VERSION)
MSG_VERSION = "{program} version {version}.".format(program=PROGRAM, version=VERSION)
MSG_USAGE = "Use {program} --help to get usage.\n".format(program=PROGRAM)
MSG_INFO = """A simple interactive fiction written by {author} as a final exam for an introductory python course. 
It takes place in the fictional world of "Discworld" 
where we follow the main character Rincewind and his companion Twoflower""".format(author=AUTHOR)
MSG_ABOUT = """{author} is a third year student at BTH working on his Bachelor's degree 
in software engineering with a focus on web programming""".format(author=AUTHOR)
MSG_CHEAT = """The shortest way through the game is: 
Start by picking up twoflower           ("pickup twoflower")
go west to the swamp                    ("w")
go west to the circumfence              ("w")
pickup the wizards hat                  ("pickup wizards hat")
go east to the swamp                    ("e")
go east to Ankh-Morpork                 ("e")
go east to the forest                   ("e")
pickup the boots of ankle kicking       ("pickup boots of ankle kicking")
go west to Ankh-Morpork                 ("w")
go north to unseen university           ("n")
pickup the octavo                       ("pickup octavo")
go south to Ankh-Morpork                ("s")
go south to the Temple of Bel-Shamharoth("s")
kick Bel-Shamharoth                     ("kick Bel-Shamharoth")
You have now won the game
"""

EXIT_SUCCESS = 0
EXIT_USAGE = 1
EXIT_FAILED = 1


def parseOptions():
    """
    Merge default options with incoming options and arguments and return them as a dictionary.
    """
    # Switch through all options
    try:
        opts, _ = getopt.getopt(
            sys.argv[1:], 
            "hivac", ["help", "info", "version", "about", "cheat"]
            )
        if len(opts) == 0:
            return
        if any(item[0] in ("-h", "--help") for item in opts):
            print(USAGE)
            sys.exit(EXIT_SUCCESS)
        elif any(item[0] in ("-i", "--info") for item in opts):
            print(MSG_INFO)
            sys.exit(EXIT_SUCCESS)
        elif any(item[0] in ("-v", "--version") for item in opts):
            print(MSG_VERSION)
            sys.exit(EXIT_SUCCESS)
        elif any(item[0] in ("-a", "--about") for item in opts):
            print(MSG_ABOUT)
            sys.exit(EXIT_SUCCESS)
        elif any(item[0] in ("-c", "--cheat") for item in opts):
            print(MSG_CHEAT)
            sys.exit(EXIT_SUCCESS)
        if any(item[0] not in ("-h", 
                               "--help", 
                               "-i", 
                               "--info", 
                               "-v", "--version", "-a", "--about", "-c", "--cheat") for item in opts):
            print(MSG_USAGE)
            sys.exit(EXIT_USAGE)
    except Exception as err:
        print(err)
        print(MSG_USAGE)
        # Prints the callstack, good for debugging, comment out for production
        #traceback.print_exception(Exception, err, None)
        sys.exit(EXIT_FAILED)


class Game(cmd.Cmd):
    """
    sasd
    """
    # pylint: disable=R0904
    def __init__(self):
        """
        sasd
        """
        cmd.Cmd.__init__(self)
        self.items = []
        self.destroyedItems = []
        self.loc = get_room(1)
        self.look()

    def move(self, direction):
        """
        sasd
        """
        newroom = self.loc.neighbor(direction)
        if newroom is None:
            print("You can't go that way")
        else:
            tmp = get_room(newroom)
            if tmp.tryToEnter(self.items):
                self.loc = tmp
                self.look()

    def look(self):
        """
        sasd
        """
        print(self.loc.name)
        print("")
        for line in textwrap.wrap(self.loc.description, 72):
            print(line)

    def do_n(self, _):
        """Goes north"""
        self.move('n')

    def do_s(self, _):
        """Goes south"""
        self.move('s')

    def do_w(self, _):
        """Goes west"""
        self.move('w')

    def do_e(self, _):
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
        """Kicks item to try and break it"""
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

    def do_items(self, _):
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

    def do_inventory(self, _):
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

    def do_clue(self, _):
        """Prints a clue for the current room"""
        print("You ask Twoflower for his opinion of your current situation.")
        print(self.loc.clue)

    def do_clear(self, _):
        """Clears the screen"""
        _ = self.loc
        os.system('cls')
        os.system('clear')

    def do_quit(self, _):
        """Quits the game"""
        _ = self.loc
        exit()
    def do_exit(self, _):
        """Quits the game"""
        _ = self.loc
        exit()

    def exit(self):
        """sdfsd"""
        _ = self.loc
        print("thanks for playing")
        return True

if __name__ == '__main__':
    """
    sasd
    """
    parseOptions()
    g = Game()
    g.cmdloop()
    sys.exit(EXIT_SUCCESS)
