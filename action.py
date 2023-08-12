import sys

class Action:
    def __init__(self):
        pass
    
    def go(self, direction=None):
        if direction:
            return f"you move to {direction}."
        return "you move but to only god knows where"
    
    def look(self, target=None):
        if target:
            if target.description:
                return target.description
            else:
                return "it seems inconsequential"
        return "you look around"
    
    def take(self, item=None):
        if item:
            if item.grabable:
                return item
            else:
                return "item is not grabable"
        else:
            return "what the hell are you grabbing, Air Yargh!"

    def use(self, item=None, target=None):
        if item and target:
            return f"You used {item} on {target}"
        elif item:
            return f"you used {item}"
        return "You use the air...its ineffective"
    
    def quit(self):
        print("Goodbye")
        sys.exit()

