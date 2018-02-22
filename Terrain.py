class Terrain:
    def __init__(self, number_name):
        switcher = {
            1: "Countryside",
            2: "Farmland",
            3: "Hills",
            4: "Forest",
            5: "Swamp",
            6: "Mountains",
            7: "Desert"
        }
        self.name = switcher.get(number_name)
