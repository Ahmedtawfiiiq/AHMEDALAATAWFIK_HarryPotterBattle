from Wizard import Wizard


class HarryPotter(Wizard):
    def __init__(self):
        self._name = "HarryPotter"
        self._harrySpells = {
            "Reducto": 60,
            "Fiendfyre": 50,
            "Nebulus": 40
        }
        super().__init__(self._name, self._harrySpells)
