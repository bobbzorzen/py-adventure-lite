"""
sdf
"""
class Item():
    """
    sdf
    """
    def __init__(self, d):
        """
        sdf
        """
        self.name = d['name']
        self.description = d['description']
        self.indestructable = d['indestructable'] == "True"
        self.heavy = d['heavy'] == "True"

    def kick(self):
        """
        sdf
        """
        if self.indestructable:
            print("The " + self.name + " seems to be made by dwarfs from outer space. " + 
                  "It seems to be some sort of adamantium - mithril alloy. " + 
                  "Unfortunately you cannot kick it as it will probably break your foot!")
            return False
        else:
            print("The kick was so hard the " + self.name + " turned into a miniature black hole and dissapeared!")
            return self.name

    def pickup(self):
        """
        sdf
        """
        if self.heavy:
            print("The " + self.name + " has apearantly watched the latest avengers movie as it yelles at you:" +
                  "\n\"You are neither Thor nor are you an elevator! You are not worthy enough to lift me!\"\n" + 
                  "The item refuses to budge.")
            return False
        else:
            print("You're amazingly strong enough to lift " + self.name + "! You stick it in your inventory")
            return self.name
