class PokeScan:
    def __init__(self, name, lvl, type):
        self.name = name
        self.level = lvl
        self.pkmntype = type
    
    def info(self):
        if self.level > 50:
            lvl = "strong"
        elif self.level > 20:
            lvl = "fair"
        else:
            lvl = "weak"
        
        if self.pkmntype == "water":
            type = "wet"
        elif self.pkmntype == 'fire':
            type = 'fiery'
        else:
            type = 'grassy'
        
        return f"{self.name}, a {type} and {lvl} Pokemon."
        
