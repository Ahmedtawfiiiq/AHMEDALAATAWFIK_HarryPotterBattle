class Wizard:
    def __init__(self, name, special_spells):
        self._name = name
        self._health = 100
        self._energy = 150
        self._wizardShield = 1
        self._spellsDictionary = {
            "AvadaKedavra": 100,
            "Crucio": 40,
            "Imperio": 20,
            "shield": 0
        }
        self._spellsDictionary.update(special_spells)
        self._spellEnergy = 0

    # Search for spell in dictionary
    # behave in two ways if the spell is normal spell or if it is a shield
    def cast_spell(self, spell_name):
        # Search
        self._spellEnergy = self._spellsDictionary.get(spell_name, "Not Found!")
        if self._spellEnergy == "Not Found!":
            print(f"{self._name} spell is not found (Enter one spell only)")
            # Recursive call if the spell is not found in dictionary
            self.cast_spell(input())
        else:
            # If the spell is shield
            if self._spellEnergy == 0:
                self.set_wizardShield()
            # If the spell is a normal spell
            else:
                self.set_energy()

    # Decreases the spell energy form the wizards energy
    def set_energy(self):
        if self._spellEnergy <= self._energy:
            self._energy -= self._spellEnergy
        else:
            print(f"{self._name} doesn't have energy to cast this spell (Enter one spell only)")
            # Recursive call if the wizard does not have energy to cast this spell
            self.cast_spell(input())

    # Decreases the number of shield after being used
    def set_wizardShield(self):
        if self._wizardShield >= 1:
            self._wizardShield -= 1
        else:
            print(f"{self._name} doesn't have shields to use (Enter one spell only)")
            # Recursive call if the wizard does not have shields to use
            self.cast_spell(input())

    # Decreases the wizard health according to who has higher spell energy
    # Works only if no wizard is using a shield spell
    def two_players_game(self, other):
        if isinstance(other, Wizard):
            if other._spellEnergy != 0 and self._spellEnergy != 0:
                if self._spellEnergy < other._spellEnergy:
                    self._health -= abs(self._spellEnergy - other._spellEnergy)
                    if self._health < 0:
                        self._health = 0
        self._spellEnergy = 0

    # Decreases the opponent wizard health according to spell energy used by the wizard himself
    def one_player_standing(self, other):
        if isinstance(other, Wizard):
            other._health -= self._spellEnergy
            if self._health < 0:
                self._health = 0
        self._spellEnergy = 0

    # Getters
    def get_energy(self):
        return self._energy

    def get_health(self):
        return self._health

    def get_name(self):
        return self._name

    def get_spells(self):
        return self._spellsDictionary

    def get_shields_number(self):
        return self._wizardShield
