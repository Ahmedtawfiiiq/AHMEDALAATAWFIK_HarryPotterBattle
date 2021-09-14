from Wizard import Wizard


class Voldemort(Wizard):
    def __init__(self):
        self._name = "Voldemort"
        self._voldemortSpells = {
            "Taboo": 80,
            "Expulso": 60,
            "Confringo": 55
        }
        super().__init__(self._name, self._voldemortSpells)
