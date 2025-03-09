class Profile:
    def __init__(self, name, base_att, att_mods=[0, 0, 0]):
        self.name = name
        self.attitude = base_att
        self.modifiers = {
            "pos":att_mods[0],
            "neut":att_mods[1],
            "neg":att_mods[2]
        }

    def update_attitude(self, change):
        if change > 0:
            self.attitude += change + self.modifiers["pos"]
        elif change < 0:
            self.attitude += change + self.modifiers["neg"]
        else:
            self.attitude += change + self.modifiers["neut"]

        return self.attitude
    
